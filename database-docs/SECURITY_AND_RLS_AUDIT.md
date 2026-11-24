# Security & Row Level Security (RLS) Audit

## Row Level Security Posture
- **RLS Enabled Tables**: **104 / 104 application tables (100%)**
- **Total Active Policies**: **219 policies** across public schema.
- **Policy Commands**: `SELECT` (72), `INSERT` (41), `UPDATE` (37), `DELETE` (33)

## Sensitive Credential Audit
1. `public.smtp_credentials`:
   - Contains SMTP host, port, username, and encrypted password.
   - Access strictly restricted via RLS to organization members with role `owner` or `admin`.
2. `public.api_keys`:
   - Contains hashed API tokens (`key_hash`). Plaintext keys are never stored.
3. `public.stalwart_accounts`:
   - Contains mail account credentials for inbound IMAP/SMTP processing.

## SECURITY DEFINER Search Path Finding
- **Finding ID**: `FIND-SEC-001`
- **Severity**: **CRITICAL**
- **Observation**: 1 public routine defined with `SECURITY DEFINER` lacks an explicit `SET search_path = public, pg_temp;`.
- **Remediation**: Apply explicit search_path configuration to ensure execution cannot be hijacked by search_path manipulation.
