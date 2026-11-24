# Missing Telemetry & Supabase Dashboard Metrics

## Unobservable Catalog Data
Because database access is restricted to read-only SQL queries via the Supabase Management API, certain host-level OS and hypervisor metrics cannot be measured directly from PostgreSQL system catalogs.

## Required Supabase Dashboard / CloudWatch Metrics
The user should inspect and provide the following metrics from the Supabase Project Dashboard (`aymarrhbnaygxkaorjfl`):
1. **Compute & CPU Utilization**:
   - Host CPU % (User vs System vs Steal)
   - 1-minute, 5-minute, and 15-minute load averages
2. **Disk I/O & Storage Subsystem**:
   - Disk IOPS utilization (Read IOPS vs Write IOPS)
   - EBS Burst Balance % (critical for AWS gp3/gp2 storage volumes)
   - Disk Throughput (MB/s)
3. **Memory & Cache Pressure**:
   - Free RAM vs OS Page Cache vs PostgreSQL `shared_buffers`
   - Swap utilization (any non-zero swap indicates severe memory pressure)
4. **Network & Connection Pool**:
   - PgBouncer active pool client connections vs waiting client queue depth
   - Network egress bandwidth (MB/s) during large marketing campaign bursts
