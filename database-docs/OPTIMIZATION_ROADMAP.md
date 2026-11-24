# Database Optimization Roadmap

## Phase 1: Immediate Wins (Sprint 1)
- [ ] Apply `SET search_path = public, pg_temp;` on `SECURITY DEFINER` functions (`FIND-SEC-001`).
- [ ] Deploy 5 high-priority foreign key indexes using `CREATE INDEX CONCURRENTLY`.
- [ ] Add primary key constraint to `public.test_apply` or drop if obsolete (`FIND-STR-001`).

## Phase 2: Workload & Scheduler Tuning (Sprint 2)
- [ ] Consolidate minutely `pg_cron` jobs (`mailofly_retry_received_email_quota`, `mailofly_reconcile_email_quota`) into a single scheduled worker.
- [ ] Optimize top 3 expensive query execution plans identified in `QUERY_PERFORMANCE.md`.

## Phase 3: Architectural Re-platforming (Sprint 3)
- [ ] Staging validation of declarative range partitioning for `public.emails` and `public.ses_event_log`.
- [ ] Execute zero-downtime table migration with dual-write triggers.
- [ ] Configure automated monthly partition creation via `pg_partman` or `pg_cron`.
