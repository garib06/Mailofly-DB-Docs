# Scheduled Database Jobs (pg_cron)

Total Registered Cron Jobs: **14**
Actively Running Jobs: **10**

| Job ID | Schedule | Command | Active | Database |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `15 3 * * *` | `select public.run_google_sheets_public_sync();` | `ACTIVE` | `postgres` |
| 22 | `30 4 * * *` | `select public.run_google_account_token_refresh();` | `ACTIVE` | `postgres` |
| 42 | `*/5 * * * *` | `SELECT public.mailofly_reap_stale_sending_emails();` | `ACTIVE` | `postgres` |
| 44 | `31 19 27 10 *` | `select public.mailofly_trigger_campaign_automation_http('6e0d39e4-ea5e-447a-ab5f-e43b56996771'::uuid);` | `ACTIVE` | `postgres` |
| 45 | `0 2 * * *` | `SELECT public.delete_expired_email_records()` | `ACTIVE` | `postgres` |
| 49 | `0 9 * * 1` | `select public.mailofly_trigger_platform_email_job('weekly');` | `ACTIVE` | `postgres` |
| 50 | `0 9 1 * *` | `select public.mailofly_trigger_platform_email_job('monthly');` | `ACTIVE` | `postgres` |
| 51 | `0 10 * * 1` | `select public.mailofly_trigger_platform_email_job('blog');` | `ACTIVE` | `postgres` |
| 52 | `*/5 * * * *` | `select public.mailofly_trigger_platform_email_job('confirmations');` | `DISABLED` | `postgres` |
| 55 | `* * * * *` | `select public.mailofly_trigger_platform_email_job('notifications');` | `DISABLED` | `postgres` |
| 56 | `0 * * * *` | `select public.mailofly_trigger_lifecycle_job();` | `DISABLED` | `postgres` |
| 58 | `* * * * *` | `select public.mailofly_trigger_platform_email_job('billing');` | `DISABLED` | `postgres` |
| 63 | `* * * * *` | `select public.mailofly_retry_received_email_quota(100);` | `ACTIVE` | `postgres` |
| 64 | `* * * * *` | `select public.mailofly_reconcile_email_quota(100);` | `ACTIVE` | `postgres` |


## Operational Impact of Minutely Background Jobs
Four jobs execute on a minutely schedule (`* * * * *`):
1. `mailofly_retry_received_email_quota(100)`
2. `mailofly_reconcile_email_quota(100)`
3. `mailofly_reap_stale_sending_emails()` (every 5 mins)

### Performance & Resource Findings
- **Continuous Transaction Overhead**: Minutely scheduled execution generates 1,440 background transactions per day per job, contributing to WAL accumulation and persistent connection pool reservations.
- **Lock Contention**: When campaign volume peaks, quota reconciliation jobs contend for row-level locks on `organization_usage` and `organization_email_periods`.
- **Recommendation**: Transition polling workers to event-driven triggers via `pg_net` or coalesce minutely cron executions into a single unified worker job.
