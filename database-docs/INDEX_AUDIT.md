# Index Architecture & Coverage Audit

## Summary Metrics
- **Total Indexes**: **702**
- **Unique Indexes**: 438
- **Primary Key Indexes**: 333
- **Index Access Methods**: B-tree (698), GIN (1)

## Foreign Key Index Coverage Analysis
PostgreSQL does NOT automatically index foreign key columns. Lack of a foreign key index causes full sequential table scans whenever a record in the referenced parent table is deleted or updated.

- **Total Foreign Key Columns in Public Schema**: 215
- **Unindexed Foreign Key Columns**: 70
- **High-Priority Unindexed Foreign Keys on Active Tables**: 5

### High-Priority Unindexed Foreign Keys
1. `public.ses_event_log.email_id` -> `public.emails.id`
2. `public.ses_recipient_outcomes.email_id` -> `public.emails.id`
3. `public.ses_send_attempts.email_id` -> `public.emails.id`
4. `public.contact_property_values.contact_id` -> `public.contacts.id`
5. `public.segment_contacts.segment_id` -> `public.contact_segments.id`

### Remediating SQL
```sql
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_ses_event_log_email_id ON public.ses_event_log(email_id);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_ses_recipient_outcomes_email_id ON public.ses_recipient_outcomes(email_id);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_ses_send_attempts_email_id ON public.ses_send_attempts(email_id);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_contact_property_values_contact_id ON public.contact_property_values(contact_id);
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_segment_contacts_segment_id ON public.segment_contacts(segment_id);
```
