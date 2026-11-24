import json
import os

with open("database-docs/source/tables.json", "r", encoding="utf-8") as f:
    tables_data = json.load(f)["data"]

with open("database-docs/source/relationships.json", "r", encoding="utf-8") as f:
    fks_data = json.load(f)["data"]

with open("database-docs/source/functions.json", "r", encoding="utf-8") as f:
    funcs_data = json.load(f)["data"]

with open("database-docs/source/triggers.json", "r", encoding="utf-8") as f:
    triggers_data = json.load(f)["data"]

with open("database-docs/source/metrics.json", "r", encoding="utf-8") as f:
    metrics_data = json.load(f)["data"]

domain_defs = {
    "tenancy_and_users": {
        "display_name": "Organizations, Tenancy & Users",
        "description": "Multi-tenant boundary enforcement, organization hierarchies, user accounts, invitations, and identity mappings.",
        "tables": [
            "organizations",
            "organization_members",
            "organization_invitations",
            "users",
            "accounts",
            "identities",
            "roles",
            "user_onboarding_responses"
        ],
        "external_tables": ["auth.users", "auth.identities"]
    },
    "contacts_and_crm": {
        "display_name": "Contacts, Audience & CRM",
        "description": "Audience management, contact attributes, dynamic/static segmentation, subscription status, topics, Google Sheets sync, and suppression lists.",
        "tables": [
            "contacts",
            "contact_properties",
            "contact_property_values",
            "properties",
            "contact_segments",
            "segment_contacts",
            "segment_google_sheets",
            "topics",
            "contact_topics",
            "contact_subscription_events",
            "contact_subscription_challenges",
            "managed_audience_programs",
            "newsletter_subscribers",
            "newsletter_signup_windows",
            "tenant_suppression_list",
            "global_suppression_list"
        ],
        "external_tables": []
    },
    "campaigns_and_templates": {
        "display_name": "Campaign Management & Templates",
        "description": "Marketing email campaigns, run orchestration, snapshot audience bindings, sending holds, and template draft versioning.",
        "tables": [
            "campaigns",
            "campaign_runs",
            "campaign_run_audience",
            "campaign_sending_holds",
            "templates",
            "template_editor_drafts",
            "native_template_versions"
        ],
        "external_tables": []
    },
    "email_delivery_and_ses": {
        "display_name": "Email Delivery & AWS SES Pipeline",
        "description": "Outbound email queuing, AWS SES event ingestion, delivery confirmations, send attempts, recipient outcomes, SMTP credentials, and sending domain DKIM/SPF identities.",
        "tables": [
            "emails",
            "email_send_confirmations",
            "email_usage_operations",
            "ses_event_inbox",
            "ses_event_log",
            "ses_recipient_outcomes",
            "ses_send_attempts",
            "ses_organization_tenants",
            "sending_domains",
            "sending_identities",
            "smtp_credentials"
        ],
        "external_tables": []
    },
    "mailboxes_and_inbound": {
        "display_name": "Mailboxes, Inbound Email & Stalwart Engine",
        "description": "Inbound email handling, mailbox alias routing, received emails storage, and Stalwart mail server integration.",
        "tables": [
            "mailboxes",
            "mailbox_aliases",
            "mailbox_queue_events",
            "received_emails",
            "stalwart_accounts",
            "stalwart_domains",
            "stalwart_emails"
        ],
        "external_tables": []
    },
    "automation_and_events": {
        "display_name": "Automation Workflows & Background Queues",
        "description": "Trigger-based automation state machines, execution step tracking, event receipts, delayed waiting events, and queue worker coordination.",
        "tables": [
            "automations",
            "automation_runs",
            "automation_run_steps",
            "automation_events",
            "automation_event_receipts",
            "automation_waiting_events",
            "queue_fallback_jobs",
            "mailofly_user_mail_queue_cron"
        ],
        "external_tables": []
    },
    "billing_and_subscriptions": {
        "display_name": "Billing, Subscriptions & Ledgers",
        "description": "Tiered plans, add-ons, credit transactions, payment ledgers, Dodo Payments webhook reconciliation, quota period tracking, and sending limits.",
        "tables": [
            "plans",
            "organization_subscriptions",
            "organization_billing_plan_state",
            "organization_usage",
            "organization_email_periods",
            "organization_email_days",
            "organization_email_policy",
            "organization_credit_transactions",
            "billing_addons",
            "organization_addons",
            "organization_addon_subscriptions",
            "billing_addon_orders",
            "billing_fulfilled_payments",
            "billing_payment_ledger",
            "billing_dodo_snapshots",
            "billing_webhook_inbox",
            "organization_billing_notifications",
            "organization_billing_notification_policy",
            "organization_payment_notice_state",
            "organization_sending_protection"
        ],
        "external_tables": []
    },
    "developer_api_and_oauth": {
        "display_name": "Developer API, Webhooks & OAuth 2.0",
        "description": "External API key provisioning, request auditing, egress webhook dispatch, OAuth2 application authentication, and Supabase integration bridges.",
        "tables": [
            "api_keys",
            "api_key_request_logs",
            "webhooks",
            "webhook_deliveries",
            "oauth_clients",
            "oauth_access_tokens",
            "oauth_refresh_tokens",
            "oauth_authorization_codes",
            "oauth_authorization_requests",
            "supabase_integrations"
        ],
        "external_tables": []
    },
    "growth_referrals_and_blog": {
        "display_name": "Referral Program & Content Engine",
        "description": "Affiliate partner referrals, commission earnings, withdrawal requests, and public marketing blog CMS.",
        "tables": [
            "referral_earnings",
            "referral_payout_methods",
            "referral_withdrawal_requests",
            "blog_posts",
            "blog_authors",
            "blog_categories"
        ],
        "external_tables": []
    },
    "lifecycle_and_notifications": {
        "display_name": "Account Lifecycle & System Notifications",
        "description": "Inactivity tracking, account deletion workflows, automated reminder notices, and multi-channel system notifications.",
        "tables": [
            "account_lifecycle_state",
            "account_lifecycle_policy",
            "account_lifecycle_notices",
            "account_lifecycle_deletions",
            "user_notifications",
            "platform_notification_events",
            "platform_email_deliveries",
            "platform_email_preferences"
        ],
        "external_tables": []
    },
    "admin_support_and_logging": {
        "display_name": "Admin RBAC, Support & Workspace Auditing",
        "description": "Internal staff RBAC, customer support ticketing, AI assistant queries, unified audit logs, workspace asset uploads, and system settings.",
        "tables": [
            "admin_roles",
            "admin_permissions",
            "admin_role_permissions",
            "support_tickets",
            "support_ticket_messages",
            "help_ai_queries",
            "app_settings",
            "workspace_logs_unified",
            "workspace_uploads",
            "test_apply"
        ],
        "external_tables": []
    }
}

# Verify coverage of all public tables
all_classified_tables = []
for d_key, d in domain_defs.items():
    all_classified_tables.extend(d["tables"])

all_public_tables = [t["table_name"] for t in tables_data if t["table_schema"] == "public"]

unclassified = set(all_public_tables) - set(all_classified_tables)
missing = set(all_classified_tables) - set(all_public_tables)

print(f"Total public tables: {len(all_public_tables)}")
print(f"Total classified tables: {len(all_classified_tables)}")
print(f"Unclassified tables: {unclassified}")
print(f"Missing tables: {missing}")

# Map foreign keys across domains
table_to_domain = {}
for d_key, d in domain_defs.items():
    for t in d["tables"]:
        table_to_domain[("public", t)] = d_key

# Add cross-domain dependency mapping
for d_key, d in domain_defs.items():
    d_tables = set(d["tables"])
    internal_fks = []
    external_fks = []
    for fk in fks_data:
        src = (fk["source_schema"], fk["source_table"])
        tgt = (fk["target_schema"], fk["target_table"])
        if fk["source_schema"] == "public" and fk["source_table"] in d_tables:
            tgt_domain = table_to_domain.get(tgt, fk["target_schema"])
            if tgt_domain == d_key:
                internal_fks.append(fk)
            else:
                external_fks.append({
                    "constraint_name": fk["constraint_name"],
                    "source_table": fk["source_table"],
                    "source_column": fk["source_column"],
                    "target_schema": fk["target_schema"],
                    "target_table": fk["target_table"],
                    "target_column": fk["target_column"],
                    "target_domain": tgt_domain
                })
    d["internal_relationships_count"] = len(internal_fks)
    d["external_relationships"] = external_fks

# Map triggers to domains
for d_key, d in domain_defs.items():
    d_tables = set(d["tables"])
    d_triggers = [t for t in triggers_data if t["schema_name"] == "public" and t["table_name"] in d_tables]
    d["triggers"] = d_triggers

# Save domains classification
output_path = os.path.join("database-docs", "source", "domains.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump({
        "database": "mailofly",
        "domain_count": len(domain_defs),
        "total_public_tables": len(all_public_tables),
        "domains": domain_defs
    }, f, indent=2)

print(f"Saved domains classification to {output_path}")
