# Multi-Tenant Security & Isolation Assessment

## Tenant Scoping Architecture
Mailofly enforces multi-tenancy using an `organization_id` discriminator column across application tables:
- **Direct Organization Scoping**: `contacts`, `contact_properties`, `contact_segments`, `topics`, `campaigns`, `emails`, `mailboxes`, `automations`, `api_keys`, `webhooks`.
- **Membership Enforcement**: Policies verify that `auth.uid()` belongs to `organization_members` for the given `organization_id`.

## Cross-Tenant Leakage Risk Assessment
1. **Suppression Lists**:
   - `tenant_suppression_list` is strictly isolated by `organization_id`.
   - `global_suppression_list` is system-wide (read-only for tenants) to prevent spam trap hits across all accounts.
2. **Inbound Mailboxes**:
   - `mailbox_aliases` enforces unique email addresses globally across the platform to prevent alias spoofing across organizations.
3. **Composite Tenant Checks**:
   - Recommendation: Ensure all composite foreign keys enforce consistent `organization_id` between child and parent records.
