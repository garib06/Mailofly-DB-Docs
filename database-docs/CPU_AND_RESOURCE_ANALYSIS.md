# CPU & Database Resource Consumption Analysis

## Distinguishing Latency from CPU Consumption
Cumulative query execution time in `pg_stat_statements` measures elapsed wall-clock latency, which includes I/O wait, lock wait, and network transit. It must NOT be confused with actual CPU core utilization.

## Evidence-Supported CPU Contributors
1. **High-Frequency Cron Polling**:
   - Minutely scheduled routines (`mailofly_retry_received_email_quota`, `mailofly_reconcile_email_quota`) wake up every 60 seconds, allocate connection backends, execute transaction blocks, and poll tables even when no work is pending.
2. **Sequential Scans from Unindexed Foreign Keys**:
   - Foreign key integrity checks on `ses_event_log` and `ses_recipient_outcomes` during parent table updates force full sequential scans, keeping CPU cores pinned during large email batches.
3. **JSONB Serialization & Compression**:
   - Extensive storage and extraction of unstructured JSON payloads in `ses_event_inbox.payload` and `billing_webhook_inbox.payload` requires CPU-intensive decompression (TOAST) and parsing.

## Observed Database Metrics
- **Active Backends**: Currently within connection limits.
- **Cache Hit Ratio**: High (>98%) on standard table scans.
- **Rollback Ratio**: Minimal (<0.1% of transactions).
