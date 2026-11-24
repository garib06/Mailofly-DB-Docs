# Recommended Target Database Architecture

## 1. Declarative Range Partitioning for High-Velocity Tables
Convert monolithic event tables to range-partitioned tables:
```sql
-- Partitioned Outbound Email Queue
CREATE TABLE public.emails_partitioned (
    id UUID NOT NULL DEFAULT gen_random_uuid(),
    organization_id UUID NOT NULL REFERENCES public.organizations(id) ON DELETE CASCADE,
    campaign_run_id UUID REFERENCES public.campaign_runs(id),
    recipient_email TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'queued',
    created_at TIMESTAMPTZ NOT NULL DEFAULT timezone('utc'::text, now()),
    PRIMARY KEY (id, created_at)
) PARTITION BY RANGE (created_at);

-- Monthly Partitions
CREATE TABLE public.emails_2026_11 PARTITION OF public.emails_partitioned
    FOR VALUES FROM ('2026-11-01 00:00:00+00') TO ('2026-12-01 00:00:00+00');
```

## 2. Foreign Key Supporting Indexes
Deploy B-tree indexes across all active foreign key columns to eliminate sequential scans during parent updates:
```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_ses_event_log_email_id ON public.ses_event_log(email_id);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_ses_recipient_outcomes_email_id ON public.ses_recipient_outcomes(email_id);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_ses_send_attempts_email_id ON public.ses_send_attempts(email_id);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_contact_property_values_contact_id ON public.contact_property_values(contact_id);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_segment_contacts_segment_id ON public.segment_contacts(segment_id);
```

## 3. Function Security Hardening
Apply immutable search paths to all security-definer routines:
```sql
ALTER FUNCTION public.handle_new_user() SET search_path = public, pg_temp;
```
