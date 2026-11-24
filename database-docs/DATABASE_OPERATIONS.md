# Database Operations & Operational Lifecycles

## 1. Outbound Campaign Execution Lifecycle
1. **Campaign Creation**: Stored in `campaigns` with target configuration and template ID.
2. **Audience Snapshotting**: When campaign runs, `campaign_runs` is initialized. Target subscriber set is copied into `campaign_run_audience` from `contact_segments` and `segment_contacts`.
3. **Queue Ingestion**: Outbound email records are batch-inserted into `emails` with `status='queued'` and `campaign_run_id`.
4. **Sending Protections & Holds**: `campaign_sending_holds` and `organization_email_periods` are evaluated against organization sending quotas.
5. **AWS SES Dispatch**: `pg_net` or external worker pulls queued records, issues SES API calls, and logs to `ses_send_attempts`.
6. **Delivery Webhook Processing**: AWS SES SNS webhook posts delivery, bounce, or complaint notifications to `ses_event_inbox` and `billing_webhook_inbox`.
7. **Outcome Recording**: `ses_recipient_outcomes` and `ses_event_log` update status on `emails`. Bounces write to `tenant_suppression_list` and `global_suppression_list`.
8. **Quota Accounting**: `email_usage_operations` and `organization_usage` records are finalized.

## 2. Inbound Email & Stalwart Mailbox Lifecycle
1. **MX Record Ingestion**: Inbound SMTP traffic delivered to Stalwart mail server.
2. **Account Routing**: Stalwart validates against `stalwart_accounts` and `stalwart_domains`.
3. **Message Storage**: Content written to `received_emails` with mailbox association in `mailboxes` and alias mapping in `mailbox_aliases`.
4. **Event Triggering**: `mailbox_queue_events` triggers inbound automation events.

## 3. Automation Engine & State Machine Lifecycle
1. **Trigger Evaluation**: Internal event or webhook writes to `automation_events`.
2. **Idempotency Guard**: `automation_event_receipts` verifies event uniqueness.
3. **Run Creation**: `automation_runs` initializes run instance bound to contact and organization.
4. **Step Execution**: `automation_run_steps` processes sequential DAG steps.
5. **Delayed Execution**: Delay nodes insert into `automation_waiting_events` with target `wake_at` timestamp.
6. **Worker Wakeup**: `cron.job` worker executes `mailofly_trigger_campaign_automation_http()` to process mature waiting events.

## 4. Multi-Tenant Access Lifecycle
1. **User Sign-up**: User registers via Supabase Auth (`auth.users`), trigger creates `public.users` and `accounts`.
2. **Organization Provisioning**: User creates `organizations`; entry inserted into `organization_members` with `role='owner'`.
3. **RLS Authorization**: Organization-scoped queries filter via `organization_members.organization_id = auth.uid()`.
