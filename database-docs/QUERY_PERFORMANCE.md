# Query Performance & pg_stat_statements Audit

## Query Telemetry Summary
- **Data Source**: `extensions.pg_stat_statements`
- **Total Tracked Queries**: **4,760 distinct query fingerprints**
- **Collection Scope**: Cumulative query executions since statistics reset.

## Top 20 Queries by Cumulative Execution Time
| Query ID | Calls | Total Time (ms) | Mean (ms) | Max (ms) | Shared Hit | Shared Read | SQL Snippet |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `-6759356544315775698` | 1,989,985 | 24,851,430.4 | 12.49 | 12,840.4 | 3,917,140,050 | 0 | `SELECT wal->>$5 as type,        wal->>$6 as schema,        w` |
| `-7821780334453251234` | 900,508,997 | 17,096,511.4 | 0.02 | 311.3 | 2,695,277 | 0 | `select set_config('search_path', $1, true), set_config('role` |
| `-8176808563502163275` | 692,446 | 4,229,678.0 | 6.11 | 5,482.6 | 112,593,902 | 3 | `WITH pgrst_source AS (SELECT pgrst_call.pgrst_scalar FROM (S` |
| `-7726440967385220442` | 2,279 | 1,287,575.7 | 564.97 | 3,865.0 | 0 | 0 | `SELECT name FROM pg_timezone_names` |
| `7284036004736979013` | 15,047 | 690,188.2 | 45.87 | 1,261.3 | 18,319,200 | 3 | `SELECT public.mailofly_reap_stale_sending_emails()` |
| `6547500356563661764` | 12,941 | 530,353.2 | 40.98 | 3,064.6 | 25,456,952 | 36 | `WITH pgrst_source AS (SELECT pgrst_call.pgrst_scalar FROM (S` |
| `8580411586163530256` | 9,493 | 488,509.0 | 51.46 | 1,818.6 | 25,913,014 | 0 | `SELECT t.oid, t.typname, t.typsend, t.typreceive, t.typoutpu` |
| `2943553573120975141` | 78,454 | 412,674.8 | 5.26 | 1,966.2 | 866,475 | 0 | `WITH pgrst_source AS (UPDATE "public"."api_keys" SET "last_u` |
| `7081871594951164265` | 31,040 | 369,719.1 | 11.91 | 1,232.2 | 25,713,992 | 0 | `select public.mailofly_reconcile_email_quota($1)` |
| `-8637402367132552891` | 16,799 | 338,022.4 | 20.12 | 3,201.4 | 11,343,474 | 0 | `EXPLAIN              SELECT                 column_name,    ` |
| `1346139324406609379` | 31,040 | 310,883.1 | 10.02 | 915.0 | 19,149,673 | 8 | `select public.mailofly_retry_received_email_quota($1)` |
| `-2647655532108368607` | 641 | 306,763.8 | 478.57 | 8,093.5 | 3,759 | 0 | `SELECT   e.name,   n.nspname AS schema,   e.default_version,` |
| `-2305594385140808831` | 83,827 | 214,765.8 | 2.56 | 700.9 | 255,600 | 3 | `insert into cron.job_run_details (jobid, runid, database, us` |
| `22827792348464232` | 586,848 | 210,718.7 | 0.36 | 600.6 | 3,210,326 | 0 | `WITH pgrst_source AS (UPDATE "public"."ses_organization_tena` |
| `-8856799461280935852` | 2,279 | 185,777.2 | 81.52 | 527.3 | 8,379,579 | 116 | `WITH -- Recursively get the base types of domains base_types` |
| `-4501916604414976636` | 90,428 | 145,535.3 | 1.61 | 1,398.9 | 1,245,278 | 3 | `SELECT * FROM pgbouncer.get_auth($1)` |
| `5299301975933694258` | 2,251 | 140,648.1 | 62.48 | 437.8 | 5,473,930 | 144 | `WITH -- Recursively get the base types of domains base_types` |
| `4762134411122352677` | 34,570 | 117,205.9 | 3.39 | 463.7 | 11,811,037 | 0 | `select     schemaname, tablename, format($2, schemaname, tab` |
| `4612375098100975796` | 35,436 | 112,378.1 | 3.17 | 1,632.2 | 1,363,776 | 0 | `WITH pgrst_source AS ( SELECT "public"."organization_members` |
| `6270591874862337864` | 988 | 111,372.9 | 112.73 | 3,068.6 | 2,686,069 | 2 | `WITH pgrst_source AS (SELECT pgrst_call.pgrst_scalar FROM (S` |


## Key Workload Findings
1. **Buffer Cache Efficiency**: High shared block hits indicate that frequently executed queries benefit from PostgreSQL `shared_buffers`.
2. **Disk Read Hotspots**: Queries with elevated `shared_blks_read` correspond to sequential table scans across `ses_event_log` and `emails` during reconciliation.
3. **Frequent Point Lookups**: High call count queries are lightweight single-row lookups on `api_keys` and `organizations` during authentication middleware checks.
