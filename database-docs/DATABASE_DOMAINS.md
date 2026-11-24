# Functional Application Domains

All 111 public application tables and views belong to a documented domain. Zero unclassified tables exist.


### Organizations, Tenancy & Users
- **Responsibility**: Multi-tenant boundary enforcement, organization hierarchies, user accounts, invitations, and identity mappings.
- **Tables (8)**: `organizations`, `organization_members`, `organization_invitations`, `users`, `accounts`, `identities`, `roles`, `user_onboarding_responses`
- **Internal Relationships**: 7
- **External Dependencies**: 6
- **Active Triggers**: 14

### Contacts, Audience & CRM
- **Responsibility**: Audience management, contact attributes, dynamic/static segmentation, subscription status, topics, Google Sheets sync, and suppression lists.
- **Tables (16)**: `contacts`, `contact_properties`, `contact_property_values`, `properties`, `contact_segments`, `segment_contacts`, `segment_google_sheets`, `topics`, `contact_topics`, `contact_subscription_events`, `contact_subscription_challenges`, `managed_audience_programs`, `newsletter_subscribers`, `newsletter_signup_windows`, `tenant_suppression_list`, `global_suppression_list`
- **Internal Relationships**: 13
- **External Dependencies**: 15
- **Active Triggers**: 14

### Campaign Management & Templates
- **Responsibility**: Marketing email campaigns, run orchestration, snapshot audience bindings, sending holds, and template draft versioning.
- **Tables (7)**: `campaigns`, `campaign_runs`, `campaign_run_audience`, `campaign_sending_holds`, `templates`, `template_editor_drafts`, `native_template_versions`
- **Internal Relationships**: 8
- **External Dependencies**: 15
- **Active Triggers**: 19

### Email Delivery & AWS SES Pipeline
- **Responsibility**: Outbound email queuing, AWS SES event ingestion, delivery confirmations, send attempts, recipient outcomes, SMTP credentials, and sending domain DKIM/SPF identities.
- **Tables (11)**: `emails`, `email_send_confirmations`, `email_usage_operations`, `ses_event_inbox`, `ses_event_log`, `ses_recipient_outcomes`, `ses_send_attempts`, `ses_organization_tenants`, `sending_domains`, `sending_identities`, `smtp_credentials`
- **Internal Relationships**: 1
- **External Dependencies**: 20
- **Active Triggers**: 11

### Mailboxes, Inbound Email & Stalwart Engine
- **Responsibility**: Inbound email handling, mailbox alias routing, received emails storage, and Stalwart mail server integration.
- **Tables (7)**: `mailboxes`, `mailbox_aliases`, `mailbox_queue_events`, `received_emails`, `stalwart_accounts`, `stalwart_domains`, `stalwart_emails`
- **Internal Relationships**: 1
- **External Dependencies**: 7
- **Active Triggers**: 1

### Automation Workflows & Background Queues
- **Responsibility**: Trigger-based automation state machines, execution step tracking, event receipts, delayed waiting events, and queue worker coordination.
- **Tables (8)**: `automations`, `automation_runs`, `automation_run_steps`, `automation_events`, `automation_event_receipts`, `automation_waiting_events`, `queue_fallback_jobs`, `mailofly_user_mail_queue_cron`
- **Internal Relationships**: 4
- **External Dependencies**: 10
- **Active Triggers**: 0

### Billing, Subscriptions & Ledgers
- **Responsibility**: Tiered plans, add-ons, credit transactions, payment ledgers, Dodo Payments webhook reconciliation, quota period tracking, and sending limits.
- **Tables (20)**: `plans`, `organization_subscriptions`, `organization_billing_plan_state`, `organization_usage`, `organization_email_periods`, `organization_email_days`, `organization_email_policy`, `organization_credit_transactions`, `billing_addons`, `organization_addons`, `organization_addon_subscriptions`, `billing_addon_orders`, `billing_fulfilled_payments`, `billing_payment_ledger`, `billing_dodo_snapshots`, `billing_webhook_inbox`, `organization_billing_notifications`, `organization_billing_notification_policy`, `organization_payment_notice_state`, `organization_sending_protection`
- **Internal Relationships**: 5
- **External Dependencies**: 18
- **Active Triggers**: 3

### Developer API, Webhooks & OAuth 2.0
- **Responsibility**: External API key provisioning, request auditing, egress webhook dispatch, OAuth2 application authentication, and Supabase integration bridges.
- **Tables (10)**: `api_keys`, `api_key_request_logs`, `webhooks`, `webhook_deliveries`, `oauth_clients`, `oauth_access_tokens`, `oauth_refresh_tokens`, `oauth_authorization_codes`, `oauth_authorization_requests`, `supabase_integrations`
- **Internal Relationships**: 7
- **External Dependencies**: 21
- **Active Triggers**: 5

### Referral Program & Content Engine
- **Responsibility**: Affiliate partner referrals, commission earnings, withdrawal requests, and public marketing blog CMS.
- **Tables (6)**: `referral_earnings`, `referral_payout_methods`, `referral_withdrawal_requests`, `blog_posts`, `blog_authors`, `blog_categories`
- **Internal Relationships**: 3
- **External Dependencies**: 6
- **Active Triggers**: 4

### Account Lifecycle & System Notifications
- **Responsibility**: Inactivity tracking, account deletion workflows, automated reminder notices, and multi-channel system notifications.
- **Tables (8)**: `account_lifecycle_state`, `account_lifecycle_policy`, `account_lifecycle_notices`, `account_lifecycle_deletions`, `user_notifications`, `platform_notification_events`, `platform_email_deliveries`, `platform_email_preferences`
- **Internal Relationships**: 0
- **External Dependencies**: 8
- **Active Triggers**: 0

### Admin RBAC, Support & Workspace Auditing
- **Responsibility**: Internal staff RBAC, customer support ticketing, AI assistant queries, unified audit logs, workspace asset uploads, and system settings.
- **Tables (10)**: `admin_roles`, `admin_permissions`, `admin_role_permissions`, `support_tickets`, `support_ticket_messages`, `help_ai_queries`, `app_settings`, `workspace_logs_unified`, `workspace_uploads`, `test_apply`
- **Internal Relationships**: 3
- **External Dependencies**: 7
- **Active Triggers**: 4
