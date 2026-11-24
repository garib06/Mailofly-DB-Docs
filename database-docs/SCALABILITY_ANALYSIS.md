# Database Scalability & Growth Analysis

## High-Velocity Table Growth Model
Mailofly's transaction volume is heavily concentrated in four tables:
1. `public.emails` (Outbound queuing & status)
2. `public.ses_event_log` (SNS delivery/bounce/complaint log)
3. `public.ses_send_attempts` (Raw AWS API attempt log)
4. `public.received_emails` (Inbound message store)

## Scalability Bottlenecks
1. **Autovacuum Bloat**: As `emails` exceeds millions of rows, autovacuum takes longer to complete, leading to dead tuple accumulation and table bloat.
2. **Buffer Cache Eviction**: Monolithic indexes on high-velocity tables eventually exceed available RAM (`shared_buffers`), forcing disk reads on recent campaign queries.
3. **Retention Deletions**: Deleting expired emails via `delete_expired_email_records()` using `DELETE FROM emails WHERE ...` creates massive WAL generation and row lock contention.

## Strategic Solution: Declarative Range Partitioning
Partitioning `emails` and `ses_event_log` by monthly `created_at` intervals allows:
- **Partition Pruning**: Queries for recent campaigns scan only the current month's partition.
- **Zero-Downtime Data Expiry**: Dropping an expired month partition via `DROP TABLE emails_2025_01;` takes 1 millisecond with zero WAL bloat.
