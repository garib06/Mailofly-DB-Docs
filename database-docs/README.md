# Mailofly — Database Architecture & Engineering Audit

## Technical Overview
- **Database Name**: `mailofly`
- **Database Engine**: PostgreSQL 17.6 on aarch64-unknown-linux-gnu (compiled by gcc 15.2.0, 64-bit)
- **Supabase Project Reference**: `aymarrhbnaygxkaorjfl`
- **Metadata Extraction Timestamp**: 2026-11-24 07:33:21 UTC
- **Scope**: Reverse-engineering, structural audit, performance telemetry, RLS security audit, Figcraft visual architecture, and recommended future-state design.

## Core Metrics Verified
- **Total Tables & Views**: 169 (104 ordinary public tables, 7 public views, 27 auth, 10 storage, 10 realtime, 2 cron, 2 net, 2 vault)
- **Total Columns**: 1,771
- **Foreign Key Constraints**: 215
- **Indexes**: 702
- **Functions & Routines**: 348
- **Active Non-Internal Triggers**: 94
- **Row Level Security Policies**: 219
- **Scheduled Database Jobs**: 14 (7 actively executing)
- **Recorded Query Fingerprints**: 4,760 in `extensions.pg_stat_statements`

## Documentation Index
1. [EXECUTIVE_SUMMARY.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/EXECUTIVE_SUMMARY.md) — Architectural assessment and priority findings.
2. [DATABASE_INVENTORY.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/DATABASE_INVENTORY.md) — Comprehensive object breakdown across all schemas.
3. [CURRENT_ARCHITECTURE.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/CURRENT_ARCHITECTURE.md) — Production database model and hub topologies.
4. [DATABASE_DOMAINS.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/DATABASE_DOMAINS.md) — Classification of all 111 public tables across 11 functional domains.
5. [COMPLETE_DATA_DICTIONARY.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/COMPLETE_DATA_DICTIONARY.md) — Full data dictionary of all 111 application tables and 1,771 columns.
6. [RELATIONSHIPS.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/RELATIONSHIPS.md) — Complete inventory of 215 declared foreign keys.
7. [DATABASE_OPERATIONS.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/DATABASE_OPERATIONS.md) — Outbound campaign, inbound Stalwart, and automation lifecycle workflows.
8. [FUNCTIONS_AND_TRIGGERS.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/FUNCTIONS_AND_TRIGGERS.md) — Audit of 348 functions and 94 active triggers.
9. [SCHEDULED_JOBS.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/SCHEDULED_JOBS.md) — Analysis of 14 pg_cron background jobs.
10. [INDEX_AUDIT.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/INDEX_AUDIT.md) — Analysis of 702 indexes and foreign-key index coverage.
11. [QUERY_PERFORMANCE.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/QUERY_PERFORMANCE.md) — Workload analysis from `extensions.pg_stat_statements`.
12. [CPU_AND_RESOURCE_ANALYSIS.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/CPU_AND_RESOURCE_ANALYSIS.md) — Analysis of actual CPU contributors and missing host telemetry.
13. [SECURITY_AND_RLS_AUDIT.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/SECURITY_AND_RLS_AUDIT.md) — RLS policy assessment and secret protection.
14. [MULTI_TENANT_SECURITY.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/MULTI_TENANT_SECURITY.md) — Organization boundary enforcement audit.
15. [SCALABILITY_ANALYSIS.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/SCALABILITY_ANALYSIS.md) — High-volume table scaling barriers and bloat risks.
16. [DATABASE_ISSUES.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/DATABASE_ISSUES.md) — Structured catalog of all 16 audit findings.
17. [RECOMMENDED_ARCHITECTURE.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/RECOMMENDED_ARCHITECTURE.md) — Proposed declarative range partitioning and optimizations.
18. [OPTIMIZATION_ROADMAP.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/OPTIMIZATION_ROADMAP.md) — Phased rollout plan and safety rollback procedures.
19. [MISSING_EVIDENCE.md](file:///c:/projects/maiofly_test/supabase_docs/database-docs/MISSING_EVIDENCE.md) — Explicit list of unobservable infrastructure metrics.

## Visual Architecture Files
- **Figcraft Workspace**: [MAILOFLY — Database Architecture & Engineering Audit.figcraft](file:///c:/projects/maiofly_test/supabase_docs/MAILOFLY%20%E2%80%94%20Database%20Architecture%20&%20Engineering%20Audit.figcraft) (10 Pages, 8,297 nodes)
- **High-Resolution PNG Previews**: [previews/](file:///c:/projects/maiofly_test/supabase_docs/previews/)
