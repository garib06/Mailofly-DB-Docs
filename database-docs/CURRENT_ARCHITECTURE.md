# Current Production Database Architecture

## Multi-Tenant Topology
Mailofly enforces a multi-tenant relational model anchored by `public.organizations`. Each organization encapsulates its own subscribers (`contacts`), custom schema attributes (`contact_properties`), sending identities (`sending_domains`), templates (`templates`), campaigns (`campaigns`), and outbound delivery logs (`emails`).

## Relational Hub Entities
1. **The Tenancy Hub (`organizations`)**:
   - Referenced by 28 distinct child tables across CRM, campaigns, email delivery, and billing.
   - Users authenticate through `auth.users`, which maps to `public.users` (1:1) and joins to organizations via `public.organization_members` (N:M).
2. **The Audience Hub (`contacts`)**:
   - Connects to `contact_segments` via junction table `segment_contacts`.
   - Extensible EAV property values stored in `contact_property_values` linking to `contact_properties`.
   - Subscription states tracked in `contact_topics` and audit events in `contact_subscription_events`.
3. **The Outbound Pipeline Hub (`emails`)**:
   - Represents the core high-throughput message store.
   - Feeds send attempts in `ses_send_attempts` and receives delivery confirmations in `email_send_confirmations`.
   - Delivery feedback ingested into `ses_event_inbox` and aggregated in `ses_event_log`.

## Cross-Schema Integrations
- **Supabase Auth (`auth.users`)**: Foreign key targets from `public.users.id`, `public.organization_members.user_id`, `public.organization_invitations.invited_by`, and `public.contacts.user_id`.
- **Supabase Storage (`storage.buckets`, `storage.objects`)**: Stores email attachments, campaign assets, and workspace uploads (`public.workspace_uploads`).
- **PostgreSQL Cron (`cron.job`)**: Schedules automated background maintenance and queue reconciliation functions.
- **Supabase Net (`net.http_request`)**: Dispatches async webhooks and AWS SES HTTP requests directly from database triggers.
