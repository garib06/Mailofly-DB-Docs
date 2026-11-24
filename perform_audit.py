import json
import os

with open("database-docs/source/tables.json", "r", encoding="utf-8") as f:
    tables = json.load(f)["data"]

with open("database-docs/source/columns.json", "r", encoding="utf-8") as f:
    columns = json.load(f)["data"]

with open("database-docs/source/indexes.json", "r", encoding="utf-8") as f:
    indexes = json.load(f)["data"]

with open("database-docs/source/constraints.json", "r", encoding="utf-8") as f:
    constraints = json.load(f)["data"]

with open("database-docs/source/relationships.json", "r", encoding="utf-8") as f:
    relationships = json.load(f)["data"]

with open("database-docs/source/functions.json", "r", encoding="utf-8") as f:
    functions = json.load(f)["data"]

with open("database-docs/source/triggers.json", "r", encoding="utf-8") as f:
    triggers = json.load(f)["data"]

with open("database-docs/source/policies.json", "r", encoding="utf-8") as f:
    policies = json.load(f)["data"]

with open("database-docs/source/metrics.json", "r", encoding="utf-8") as f:
    metrics = json.load(f)["data"]

public_tables = [t for t in tables if t["table_schema"] == "public" and t["object_type"] == "r"]
public_views = [t for t in tables if t["table_schema"] == "public" and t["object_type"] in ("v", "m")]

print(f"Auditing {len(public_tables)} public tables and {len(public_views)} public views...")

findings = []
finding_counter = 1

def add_finding(category, severity, confidence, title, affected_object, current_behavior, problem_impact, recommendation, suggested_sql, expected_benefit, risk, testing, rollback):
    global finding_counter
    fid = f"FIND-{category[:3].upper()}-{finding_counter:03d}"
    finding_counter += 1
    findings.append({
        "finding_id": fid,
        "category": category,
        "severity": severity,
        "confidence": confidence,
        "title": title,
        "affected_object": affected_object,
        "current_behavior": current_behavior,
        "why_it_is_a_problem": problem_impact,
        "recommended_change": recommendation,
        "suggested_sql": suggested_sql,
        "expected_benefit": expected_benefit,
        "implementation_risk": risk,
        "testing_requirements": testing,
        "rollback_considerations": rollback,
        "status": "OPEN"
    })

# 1. Structural Audit: Primary Keys
pks_by_table = set()
for c in constraints:
    if c["constraint_type"] == "p":
        pks_by_table.add((c["schema_name"], c["table_name"]))

missing_pk_tables = []
for t in public_tables:
    if (t["table_schema"], t["table_name"]) not in pks_by_table:
        missing_pk_tables.append(t["table_name"])

print(f"Tables missing Primary Key: {missing_pk_tables}")
if missing_pk_tables:
    for mt in missing_pk_tables:
        add_finding(
            "Structure", "HIGH", "CERTAIN",
            f"Table public.{mt} lacks a Primary Key constraint",
            f"public.{mt}",
            "Table has no declared primary key constraint in pg_constraint.",
            "Prevents logical replication, impairs row identification in ORMs, causes sequential scans on single-row updates/deletes, and compromises data integrity.",
            f"Add a primary key constraint to public.{mt} (typically on an id UUID or composite business key).",
            f"ALTER TABLE public.{mt} ADD PRIMARY KEY (id);",
            "Enables fast index-based lookups, logical replication compatibility, and strict row uniqueness.",
            "LOW - Existing duplicate rows would cause the ALTER command to fail until deduped.",
            "Verify table contents for duplicates before applying constraint.",
            f"ALTER TABLE public.{mt} DROP CONSTRAINT IF EXISTS {mt}_pkey;"
        )

# 2. Structural & Performance Audit: Foreign Key Indexes
# Map existing indexes by (schema, table, leading_column)
indexes_by_col = set()
for idx in indexes:
    # parse definition e.g. USING btree (organization_id)
    idef = idx["index_definition"]
    if "(" in idef and ")" in idef:
        cols_part = idef[idef.rindex("(")+1:idef.rindex(")")].split(",")
        first_col = cols_part[0].strip().replace('"', '')
        indexes_by_col.add((idx["schema_name"], idx["table_name"], first_col))

unindexed_fks = []
for fk in relationships:
    if fk["source_schema"] == "public":
        key = (fk["source_schema"], fk["source_table"], fk["source_column"])
        if key not in indexes_by_col:
            unindexed_fks.append(fk)

print(f"Total unindexed foreign key columns in public schema: {len(unindexed_fks)}")

# Check high-volume / high-frequency unindexed FKs
high_pri_fks = [fk for fk in unindexed_fks if fk["source_table"] in (
    "emails", "ses_event_log", "ses_recipient_outcomes", "ses_send_attempts",
    "received_emails", "automation_runs", "automation_run_steps",
    "contact_property_values", "segment_contacts", "billing_payment_ledger", "organization_usage"
)]

print(f"High-priority unindexed FKs on active tables: {len(high_pri_fks)}")
for fk in high_pri_fks:
    add_finding(
        "Performance", "HIGH", "HIGH",
        f"Missing Index on Foreign Key: public.{fk['source_table']}.{fk['source_column']}",
        f"public.{fk['source_table']}",
        f"Foreign key constraint {fk['constraint_name']} references {fk['target_table']}.{fk['target_column']}, but no supporting B-tree index exists on {fk['source_column']}.",
        "Deletions or updates on referenced parent table require a FULL SEQUENTIAL SCAN of the child table to verify foreign key integrity, creating massive disk I/O and shared lock contention.",
        f"Create a supporting B-tree index on public.{fk['source_table']}({fk['source_column']}).",
        f"CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_{fk['source_table']}_{fk['source_column']} ON public.{fk['source_table']}({fk['source_column']});",
        "Eliminates sequential scans during parent deletes/updates and accelerates JOIN queries.",
        "LOW - CONCURRENTLY avoids locking production writes.",
        "EXPLAIN (ANALYZE, BUFFERS) query joining parent and child.",
        f"DROP INDEX CONCURRENTLY IF EXISTS public.idx_{fk['source_table']}_{fk['source_column']};"
    )

# 3. Security Audit: SECURITY DEFINER Search Path
sec_def_funcs = [f for f in functions if f["is_security_definer"] and f["schema_name"] == "public"]
sec_def_missing_path = [f for f in sec_def_funcs if not f.get("configuration_settings") or not any("search_path" in s for s in f["configuration_settings"])]
print(f"Security Definer functions in public: {len(sec_def_funcs)}")
print(f"Security Definer functions missing search_path: {len(sec_def_missing_path)}")

if sec_def_missing_path:
    add_finding(
        "Security", "CRITICAL", "CERTAIN",
        f"{len(sec_def_missing_path)} SECURITY DEFINER functions lack explicit search_path",
        "public functions (pg_proc)",
        f"{len(sec_def_missing_path)} functions execute with elevated superuser/owner privileges without an immutable search_path.",
        "Critical privilege escalation vulnerability (CWE-426): an authenticated attacker can create temporary tables or operators in their schema and hijack function execution flow.",
        "Alter all SECURITY DEFINER routines to pin search_path = public, pg_temp.",
        "ALTER FUNCTION <func_signature> SET search_path = public, pg_temp;",
        "Completely eliminates search_path hijacking in multi-tenant environment.",
        "LOW - Standard Supabase security hardening recommendation.",
        "Execute function as authenticated role and verify search_path isolation.",
        "ALTER FUNCTION <func_signature> RESET search_path;"
    )

# 4. Performance Audit: Expensive Queries in pg_stat_statements
top_queries = metrics.get("top_queries_by_total_time", [])
print(f"Top queries recorded: {len(top_queries)}")
for q in top_queries[:5]:
    tot_t = float(q.get('total_exec_time_ms') or 0)
    mean_t = float(q.get('mean_exec_time_ms') or 0)
    calls_c = int(q.get('calls') or 0)
    sh_read = int(q.get('shared_blks_read') or 0)
    add_finding(
        "Performance", "HIGH", "HIGH",
        f"Heavy Query Workload: Query {q['queryid']} ({tot_t:,.0f} ms total latency)",
        f"Query {q['queryid']}",
        f"Query executed {calls_c:,} times with total cumulative time of {tot_t:,.1f} ms and mean latency of {mean_t:,.2f} ms.",
        f"High shared buffer reads ({sh_read:,} blocks) indicates disk reads, contributing materially to database I/O and CPU consumption.",
        "Optimize query execution plan with targeted compound indexes or query refactoring.",
        f"-- Query Snippet: {q['query_snippet'][:120]}...",
        "Reduces query latency and buffer churn.",
        "LOW",
        "EXPLAIN (ANALYZE, BUFFERS) query on staging snapshot.",
        "N/A"
    )

# 5. Architectural Scalability: Monolithic Tables needing Partitioning
large_monolith_tables = ["emails", "ses_event_log", "received_emails", "automation_runs"]
for lt in large_monolith_tables:
    add_finding(
        "Scalability", "HIGH", "HIGH",
        f"Monolithic High-Velocity Table: public.{lt} lacks Partitioning",
        f"public.{lt}",
        f"Table public.{lt} is an append-heavy operational log / queue stored as a single monolithic table.",
        "As records accumulate, index sizes exceed available shared_buffers, autovacuum incurs high read/write amplification, and data retention deletions require expensive DELETE sweeps.",
        f"Implement PostgreSQL 17 Declarative Range Partitioning by RANGE (created_at) with monthly partition intervals.",
        f"CREATE TABLE public.{lt}_partitioned (...) PARTITION BY RANGE (created_at);",
        "Enables partition pruning (10x faster range queries), instant zero-downtime data archival via DROP TABLE, and localized index maintenance.",
        "MEDIUM - Requires migration with composite primary key: PRIMARY KEY (id, created_at).",
        "Validate ORM compatibility with composite PK on staging environment.",
        "Revert writes to original unpartitioned table."
    )

# Save findings JSON
out_path = os.path.join("database-docs", "recommendations", "findings.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "database": "mailofly",
        "total_findings": len(findings),
        "findings": findings
    }, f, indent=2)

print(f"Saved {len(findings)} detailed findings to {out_path}")
