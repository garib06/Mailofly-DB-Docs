# Database Audit Findings & Issues Catalog


### [FIND-STR-001] Table public.test_apply lacks a Primary Key constraint
- **Category**: `Structure` | **Severity**: `HIGH` | **Confidence**: `CERTAIN` | **Status**: `OPEN`
- **Affected Object**: `public.test_apply`
- **Current Behavior**: Table has no declared primary key constraint in pg_constraint.
- **Why It Is A Problem**: Prevents logical replication, impairs row identification in ORMs, causes sequential scans on single-row updates/deletes, and compromises data integrity.
- **Recommended Change**: Add a primary key constraint to public.test_apply (typically on an id UUID or composite business key).
- **Suggested SQL**:
```sql
ALTER TABLE public.test_apply ADD PRIMARY KEY (id);
```
- **Expected Benefit**: Enables fast index-based lookups, logical replication compatibility, and strict row uniqueness.
- **Implementation Risk**: LOW - Existing duplicate rows would cause the ALTER command to fail until deduped.
- **Testing Requirements**: Verify table contents for duplicates before applying constraint.
- **Rollback Considerations**: ALTER TABLE public.test_apply DROP CONSTRAINT IF EXISTS test_apply_pkey;

---

### [FIND-PER-002] Missing Index on Foreign Key: public.billing_payment_ledger.plan_id
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `public.billing_payment_ledger`
- **Current Behavior**: Foreign key constraint billing_payment_ledger_plan_id_fkey references plans.id, but no supporting B-tree index exists on plan_id.
- **Why It Is A Problem**: Deletions or updates on referenced parent table require a FULL SEQUENTIAL SCAN of the child table to verify foreign key integrity, creating massive disk I/O and shared lock contention.
- **Recommended Change**: Create a supporting B-tree index on public.billing_payment_ledger(plan_id).
- **Suggested SQL**:
```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_billing_payment_ledger_plan_id ON public.billing_payment_ledger(plan_id);
```
- **Expected Benefit**: Eliminates sequential scans during parent deletes/updates and accelerates JOIN queries.
- **Implementation Risk**: LOW - CONCURRENTLY avoids locking production writes.
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query joining parent and child.
- **Rollback Considerations**: DROP INDEX CONCURRENTLY IF EXISTS public.idx_billing_payment_ledger_plan_id;

---

### [FIND-PER-003] Missing Index on Foreign Key: public.emails.api_key_id
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `public.emails`
- **Current Behavior**: Foreign key constraint emails_api_key_id_fkey references api_keys.id, but no supporting B-tree index exists on api_key_id.
- **Why It Is A Problem**: Deletions or updates on referenced parent table require a FULL SEQUENTIAL SCAN of the child table to verify foreign key integrity, creating massive disk I/O and shared lock contention.
- **Recommended Change**: Create a supporting B-tree index on public.emails(api_key_id).
- **Suggested SQL**:
```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_emails_api_key_id ON public.emails(api_key_id);
```
- **Expected Benefit**: Eliminates sequential scans during parent deletes/updates and accelerates JOIN queries.
- **Implementation Risk**: LOW - CONCURRENTLY avoids locking production writes.
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query joining parent and child.
- **Rollback Considerations**: DROP INDEX CONCURRENTLY IF EXISTS public.idx_emails_api_key_id;

---

### [FIND-PER-004] Missing Index on Foreign Key: public.emails.contact_id
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `public.emails`
- **Current Behavior**: Foreign key constraint emails_contact_id_fkey references contacts.id, but no supporting B-tree index exists on contact_id.
- **Why It Is A Problem**: Deletions or updates on referenced parent table require a FULL SEQUENTIAL SCAN of the child table to verify foreign key integrity, creating massive disk I/O and shared lock contention.
- **Recommended Change**: Create a supporting B-tree index on public.emails(contact_id).
- **Suggested SQL**:
```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_emails_contact_id ON public.emails(contact_id);
```
- **Expected Benefit**: Eliminates sequential scans during parent deletes/updates and accelerates JOIN queries.
- **Implementation Risk**: LOW - CONCURRENTLY avoids locking production writes.
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query joining parent and child.
- **Rollback Considerations**: DROP INDEX CONCURRENTLY IF EXISTS public.idx_emails_contact_id;

---

### [FIND-PER-005] Missing Index on Foreign Key: public.received_emails.user_id
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `public.received_emails`
- **Current Behavior**: Foreign key constraint received_emails_user_id_fkey references users.id, but no supporting B-tree index exists on user_id.
- **Why It Is A Problem**: Deletions or updates on referenced parent table require a FULL SEQUENTIAL SCAN of the child table to verify foreign key integrity, creating massive disk I/O and shared lock contention.
- **Recommended Change**: Create a supporting B-tree index on public.received_emails(user_id).
- **Suggested SQL**:
```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_received_emails_user_id ON public.received_emails(user_id);
```
- **Expected Benefit**: Eliminates sequential scans during parent deletes/updates and accelerates JOIN queries.
- **Implementation Risk**: LOW - CONCURRENTLY avoids locking production writes.
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query joining parent and child.
- **Rollback Considerations**: DROP INDEX CONCURRENTLY IF EXISTS public.idx_received_emails_user_id;

---

### [FIND-PER-006] Missing Index on Foreign Key: public.ses_event_log.organization_id
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `public.ses_event_log`
- **Current Behavior**: Foreign key constraint ses_event_log_organization_id_fkey references organizations.id, but no supporting B-tree index exists on organization_id.
- **Why It Is A Problem**: Deletions or updates on referenced parent table require a FULL SEQUENTIAL SCAN of the child table to verify foreign key integrity, creating massive disk I/O and shared lock contention.
- **Recommended Change**: Create a supporting B-tree index on public.ses_event_log(organization_id).
- **Suggested SQL**:
```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_ses_event_log_organization_id ON public.ses_event_log(organization_id);
```
- **Expected Benefit**: Eliminates sequential scans during parent deletes/updates and accelerates JOIN queries.
- **Implementation Risk**: LOW - CONCURRENTLY avoids locking production writes.
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query joining parent and child.
- **Rollback Considerations**: DROP INDEX CONCURRENTLY IF EXISTS public.idx_ses_event_log_organization_id;

---

### [FIND-SEC-007] 1 SECURITY DEFINER functions lack explicit search_path
- **Category**: `Security` | **Severity**: `CRITICAL` | **Confidence**: `CERTAIN` | **Status**: `OPEN`
- **Affected Object**: `public functions (pg_proc)`
- **Current Behavior**: 1 functions execute with elevated superuser/owner privileges without an immutable search_path.
- **Why It Is A Problem**: Critical privilege escalation vulnerability (CWE-426): an authenticated attacker can create temporary tables or operators in their schema and hijack function execution flow.
- **Recommended Change**: Alter all SECURITY DEFINER routines to pin search_path = public, pg_temp.
- **Suggested SQL**:
```sql
ALTER FUNCTION <func_signature> SET search_path = public, pg_temp;
```
- **Expected Benefit**: Completely eliminates search_path hijacking in multi-tenant environment.
- **Implementation Risk**: LOW - Standard Supabase security hardening recommendation.
- **Testing Requirements**: Execute function as authenticated role and verify search_path isolation.
- **Rollback Considerations**: ALTER FUNCTION <func_signature> RESET search_path;

---

### [FIND-PER-008] Heavy Query Workload: Query -6759356544315775698 (24,851,430 ms total latency)
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `Query -6759356544315775698`
- **Current Behavior**: Query executed 1,989,985 times with total cumulative time of 24,851,430.4 ms and mean latency of 12.49 ms.
- **Why It Is A Problem**: High shared buffer reads (0 blocks) indicates disk reads, contributing materially to database I/O and CPU consumption.
- **Recommended Change**: Optimize query execution plan with targeted compound indexes or query refactoring.
- **Suggested SQL**:
```sql
-- Query Snippet: SELECT wal->>$5 as type,
       wal->>$6 as schema,
       wal->>$7 as table,
       COALESCE(wal->>$8, $9) as columns,
...
```
- **Expected Benefit**: Reduces query latency and buffer churn.
- **Implementation Risk**: LOW
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query on staging snapshot.
- **Rollback Considerations**: N/A

---

### [FIND-PER-009] Heavy Query Workload: Query -7821780334453251234 (17,096,511 ms total latency)
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `Query -7821780334453251234`
- **Current Behavior**: Query executed 900,508,997 times with total cumulative time of 17,096,511.4 ms and mean latency of 0.02 ms.
- **Why It Is A Problem**: High shared buffer reads (0 blocks) indicates disk reads, contributing materially to database I/O and CPU consumption.
- **Recommended Change**: Optimize query execution plan with targeted compound indexes or query refactoring.
- **Suggested SQL**:
```sql
-- Query Snippet: select set_config('search_path', $1, true), set_config('role', $2, true), set_config('request.jwt.claims', $3, true), se...
```
- **Expected Benefit**: Reduces query latency and buffer churn.
- **Implementation Risk**: LOW
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query on staging snapshot.
- **Rollback Considerations**: N/A

---

### [FIND-PER-010] Heavy Query Workload: Query -8176808563502163275 (4,229,678 ms total latency)
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `Query -8176808563502163275`
- **Current Behavior**: Query executed 692,446 times with total cumulative time of 4,229,678.0 ms and mean latency of 6.11 ms.
- **Why It Is A Problem**: High shared buffer reads (3 blocks) indicates disk reads, contributing materially to database I/O and CPU consumption.
- **Recommended Change**: Optimize query execution plan with targeted compound indexes or query refactoring.
- **Suggested SQL**:
```sql
-- Query Snippet: WITH pgrst_source AS (SELECT pgrst_call.pgrst_scalar FROM (SELECT $1 AS json_data) pgrst_payload, LATERAL (SELECT "p_org...
```
- **Expected Benefit**: Reduces query latency and buffer churn.
- **Implementation Risk**: LOW
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query on staging snapshot.
- **Rollback Considerations**: N/A

---

### [FIND-PER-011] Heavy Query Workload: Query -7726440967385220442 (1,287,576 ms total latency)
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `Query -7726440967385220442`
- **Current Behavior**: Query executed 2,279 times with total cumulative time of 1,287,575.7 ms and mean latency of 564.97 ms.
- **Why It Is A Problem**: High shared buffer reads (0 blocks) indicates disk reads, contributing materially to database I/O and CPU consumption.
- **Recommended Change**: Optimize query execution plan with targeted compound indexes or query refactoring.
- **Suggested SQL**:
```sql
-- Query Snippet: SELECT name FROM pg_timezone_names...
```
- **Expected Benefit**: Reduces query latency and buffer churn.
- **Implementation Risk**: LOW
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query on staging snapshot.
- **Rollback Considerations**: N/A

---

### [FIND-PER-012] Heavy Query Workload: Query 7284036004736979013 (690,188 ms total latency)
- **Category**: `Performance` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `Query 7284036004736979013`
- **Current Behavior**: Query executed 15,047 times with total cumulative time of 690,188.2 ms and mean latency of 45.87 ms.
- **Why It Is A Problem**: High shared buffer reads (3 blocks) indicates disk reads, contributing materially to database I/O and CPU consumption.
- **Recommended Change**: Optimize query execution plan with targeted compound indexes or query refactoring.
- **Suggested SQL**:
```sql
-- Query Snippet: SELECT public.mailofly_reap_stale_sending_emails()...
```
- **Expected Benefit**: Reduces query latency and buffer churn.
- **Implementation Risk**: LOW
- **Testing Requirements**: EXPLAIN (ANALYZE, BUFFERS) query on staging snapshot.
- **Rollback Considerations**: N/A

---

### [FIND-SCA-013] Monolithic High-Velocity Table: public.emails lacks Partitioning
- **Category**: `Scalability` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `public.emails`
- **Current Behavior**: Table public.emails is an append-heavy operational log / queue stored as a single monolithic table.
- **Why It Is A Problem**: As records accumulate, index sizes exceed available shared_buffers, autovacuum incurs high read/write amplification, and data retention deletions require expensive DELETE sweeps.
- **Recommended Change**: Implement PostgreSQL 17 Declarative Range Partitioning by RANGE (created_at) with monthly partition intervals.
- **Suggested SQL**:
```sql
CREATE TABLE public.emails_partitioned (...) PARTITION BY RANGE (created_at);
```
- **Expected Benefit**: Enables partition pruning (10x faster range queries), instant zero-downtime data archival via DROP TABLE, and localized index maintenance.
- **Implementation Risk**: MEDIUM - Requires migration with composite primary key: PRIMARY KEY (id, created_at).
- **Testing Requirements**: Validate ORM compatibility with composite PK on staging environment.
- **Rollback Considerations**: Revert writes to original unpartitioned table.

---

### [FIND-SCA-014] Monolithic High-Velocity Table: public.ses_event_log lacks Partitioning
- **Category**: `Scalability` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `public.ses_event_log`
- **Current Behavior**: Table public.ses_event_log is an append-heavy operational log / queue stored as a single monolithic table.
- **Why It Is A Problem**: As records accumulate, index sizes exceed available shared_buffers, autovacuum incurs high read/write amplification, and data retention deletions require expensive DELETE sweeps.
- **Recommended Change**: Implement PostgreSQL 17 Declarative Range Partitioning by RANGE (created_at) with monthly partition intervals.
- **Suggested SQL**:
```sql
CREATE TABLE public.ses_event_log_partitioned (...) PARTITION BY RANGE (created_at);
```
- **Expected Benefit**: Enables partition pruning (10x faster range queries), instant zero-downtime data archival via DROP TABLE, and localized index maintenance.
- **Implementation Risk**: MEDIUM - Requires migration with composite primary key: PRIMARY KEY (id, created_at).
- **Testing Requirements**: Validate ORM compatibility with composite PK on staging environment.
- **Rollback Considerations**: Revert writes to original unpartitioned table.

---

### [FIND-SCA-015] Monolithic High-Velocity Table: public.received_emails lacks Partitioning
- **Category**: `Scalability` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `public.received_emails`
- **Current Behavior**: Table public.received_emails is an append-heavy operational log / queue stored as a single monolithic table.
- **Why It Is A Problem**: As records accumulate, index sizes exceed available shared_buffers, autovacuum incurs high read/write amplification, and data retention deletions require expensive DELETE sweeps.
- **Recommended Change**: Implement PostgreSQL 17 Declarative Range Partitioning by RANGE (created_at) with monthly partition intervals.
- **Suggested SQL**:
```sql
CREATE TABLE public.received_emails_partitioned (...) PARTITION BY RANGE (created_at);
```
- **Expected Benefit**: Enables partition pruning (10x faster range queries), instant zero-downtime data archival via DROP TABLE, and localized index maintenance.
- **Implementation Risk**: MEDIUM - Requires migration with composite primary key: PRIMARY KEY (id, created_at).
- **Testing Requirements**: Validate ORM compatibility with composite PK on staging environment.
- **Rollback Considerations**: Revert writes to original unpartitioned table.

---

### [FIND-SCA-016] Monolithic High-Velocity Table: public.automation_runs lacks Partitioning
- **Category**: `Scalability` | **Severity**: `HIGH` | **Confidence**: `HIGH` | **Status**: `OPEN`
- **Affected Object**: `public.automation_runs`
- **Current Behavior**: Table public.automation_runs is an append-heavy operational log / queue stored as a single monolithic table.
- **Why It Is A Problem**: As records accumulate, index sizes exceed available shared_buffers, autovacuum incurs high read/write amplification, and data retention deletions require expensive DELETE sweeps.
- **Recommended Change**: Implement PostgreSQL 17 Declarative Range Partitioning by RANGE (created_at) with monthly partition intervals.
- **Suggested SQL**:
```sql
CREATE TABLE public.automation_runs_partitioned (...) PARTITION BY RANGE (created_at);
```
- **Expected Benefit**: Enables partition pruning (10x faster range queries), instant zero-downtime data archival via DROP TABLE, and localized index maintenance.
- **Implementation Risk**: MEDIUM - Requires migration with composite primary key: PRIMARY KEY (id, created_at).
- **Testing Requirements**: Validate ORM compatibility with composite PK on staging environment.
- **Rollback Considerations**: Revert writes to original unpartitioned table.

---
