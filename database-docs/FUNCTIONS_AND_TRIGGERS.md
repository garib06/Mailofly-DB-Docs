# Functions, Stored Procedures & Triggers Audit

## Function Overview
- **Total Functions**: **348** across accessible schemas.
- **SECURITY DEFINER Functions in Public Schema**: **129**
- **Triggers**: **94** active non-internal triggers across the database.

## Critical Security Definer Analysis
SECURITY DEFINER functions run with the privileges of the creator (`supabase_admin` or `postgres`). If they do not pin `search_path`, malicious users can hijack function execution by defining custom objects in temporary schemas.
- Target finding: `FIND-SEC-001` identifies routines requiring explicit `SET search_path = public, pg_temp;`.

## Sample Functions Inventory (Top 50 of 348)
| Schema | Function Name | Kind | Owner | Security Definer | Volatility | Return Type |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `auth` | `email` | `f` | `supabase_auth_admin` | `NO` | `s` | `text` |
| `auth` | `jwt` | `f` | `supabase_auth_admin` | `NO` | `s` | `jsonb` |
| `auth` | `role` | `f` | `supabase_auth_admin` | `NO` | `s` | `text` |
| `auth` | `uid` | `f` | `supabase_auth_admin` | `NO` | `s` | `uuid` |
| `cron` | `alter_job` | `f` | `supabase_admin` | `NO` | `v` | `void` |
| `cron` | `job_cache_invalidate` | `f` | `supabase_admin` | `NO` | `v` | `trigger` |
| `cron` | `schedule` | `f` | `supabase_admin` | `NO` | `v` | `bigint` |
| `cron` | `schedule` | `f` | `supabase_admin` | `NO` | `v` | `bigint` |
| `cron` | `schedule_in_database` | `f` | `supabase_admin` | `NO` | `v` | `bigint` |
| `cron` | `unschedule` | `f` | `supabase_admin` | `NO` | `v` | `boolean` |
| `cron` | `unschedule` | `f` | `supabase_admin` | `NO` | `v` | `boolean` |
| `extensions` | `armor` | `f` | `postgres` | `NO` | `i` | `text` |
| `extensions` | `armor` | `f` | `postgres` | `NO` | `i` | `text` |
| `extensions` | `crypt` | `f` | `postgres` | `NO` | `i` | `text` |
| `extensions` | `dearmor` | `f` | `postgres` | `NO` | `i` | `bytea` |
| `extensions` | `decrypt` | `f` | `postgres` | `NO` | `i` | `bytea` |
| `extensions` | `decrypt_iv` | `f` | `postgres` | `NO` | `i` | `bytea` |
| `extensions` | `digest` | `f` | `postgres` | `NO` | `i` | `bytea` |
| `extensions` | `digest` | `f` | `postgres` | `NO` | `i` | `bytea` |
| `extensions` | `encrypt` | `f` | `postgres` | `NO` | `i` | `bytea` |
| `extensions` | `encrypt_iv` | `f` | `postgres` | `NO` | `i` | `bytea` |
| `extensions` | `gen_random_bytes` | `f` | `postgres` | `NO` | `v` | `bytea` |
| `extensions` | `gen_random_uuid` | `f` | `postgres` | `NO` | `v` | `uuid` |
| `extensions` | `gen_salt` | `f` | `postgres` | `NO` | `v` | `text` |
| `extensions` | `gen_salt` | `f` | `postgres` | `NO` | `v` | `text` |
| `extensions` | `grant_pg_cron_access` | `f` | `supabase_admin` | `NO` | `v` | `event_trigger` |
| `extensions` | `grant_pg_graphql_access` | `f` | `supabase_admin` | `NO` | `v` | `event_trigger` |
| `extensions` | `grant_pg_net_access` | `f` | `supabase_admin` | `NO` | `v` | `event_trigger` |
| `extensions` | `hmac` | `f` | `postgres` | `NO` | `i` | `bytea` |
| `extensions` | `hmac` | `f` | `postgres` | `NO` | `i` | `bytea` |
| `extensions` | `hypopg` | `f` | `supabase_admin` | `NO` | `v` | `SETOF record` |
| `extensions` | `hypopg_create_index` | `f` | `supabase_admin` | `NO` | `v` | `SETOF record` |
| `extensions` | `hypopg_drop_index` | `f` | `supabase_admin` | `NO` | `v` | `boolean` |
| `extensions` | `hypopg_get_indexdef` | `f` | `supabase_admin` | `NO` | `v` | `text` |
| `extensions` | `hypopg_hidden_indexes` | `f` | `supabase_admin` | `NO` | `v` | `TABLE(indexid oid)` |
| `extensions` | `hypopg_hide_index` | `f` | `supabase_admin` | `NO` | `v` | `boolean` |
| `extensions` | `hypopg_relation_size` | `f` | `supabase_admin` | `NO` | `v` | `bigint` |
| `extensions` | `hypopg_reset` | `f` | `supabase_admin` | `NO` | `v` | `void` |
| `extensions` | `hypopg_reset_index` | `f` | `supabase_admin` | `NO` | `v` | `void` |
| `extensions` | `hypopg_unhide_all_indexes` | `f` | `supabase_admin` | `NO` | `v` | `void` |
| `extensions` | `hypopg_unhide_index` | `f` | `supabase_admin` | `NO` | `v` | `boolean` |
| `extensions` | `index_advisor` | `f` | `supabase_admin` | `NO` | `v` | `TABLE(startup_cost_b` |
| `extensions` | `pg_stat_statements` | `f` | `postgres` | `NO` | `v` | `SETOF record` |
| `extensions` | `pg_stat_statements_info` | `f` | `postgres` | `NO` | `v` | `record` |
| `extensions` | `pg_stat_statements_reset` | `f` | `postgres` | `NO` | `v` | `timestamp with time ` |
| `extensions` | `pgp_armor_headers` | `f` | `postgres` | `NO` | `i` | `SETOF record` |
| `extensions` | `pgp_key_id` | `f` | `postgres` | `NO` | `i` | `text` |
| `extensions` | `pgp_pub_decrypt` | `f` | `postgres` | `NO` | `i` | `text` |
| `extensions` | `pgp_pub_decrypt` | `f` | `postgres` | `NO` | `i` | `text` |
| `extensions` | `pgp_pub_decrypt` | `f` | `postgres` | `NO` | `i` | `text` |


## Complete Trigger Inventory (94 Triggers)
| Schema | Table Name | Trigger Name | Function Called | Enabled |
| :--- | :--- | :--- | :--- | :--- |
| `auth` | `users` | `account_lifecycle_confirm` | `record_activity` | `YES` |
| `auth` | `users` | `account_lifecycle_enroll` | `record_activity` | `YES` |
| `auth` | `users` | `mailofly_guard_account_erasure` | `mailofly_guard_account_erasure` | `YES` |
| `auth` | `users` | `on_auth_user_created` | `handle_new_auth_user` | `YES` |
| `auth` | `users` | `on_auth_user_email_updated` | `sync_public_user_email_from_auth` | `YES` |
| `cron` | `job` | `cron_job_cache_invalidate` | `job_cache_invalidate` | `YES` |
| `public` | `admin_roles` | `trg_admin_roles_prevent_system_delete` | `admin_roles_prevent_system_delete` | `YES` |
| `public` | `api_key_request_logs` | `mailofly_plan_api_request_insert` | `mailofly_enforce_api_request_quota` | `YES` |
| `public` | `api_keys` | `account_lifecycle_api_key_create` | `record_activity` | `YES` |
| `public` | `api_keys` | `account_lifecycle_api_key_use` | `record_activity` | `YES` |
| `public` | `api_keys` | `platform_api_key_created` | `capture_product_event` | `YES` |
| `public` | `app_settings` | `app_settings_updated_at` | `set_updated_at` | `YES` |
| `public` | `blog_authors` | `blog_authors_set_updated_at` | `set_updated_at` | `YES` |
| `public` | `blog_categories` | `blog_categories_set_updated_at` | `set_updated_at` | `YES` |
| `public` | `blog_posts` | `blog_posts_broadcast_after_publish` | `mailofly_blog_post_broadcast_notify` | `YES` |
| `public` | `blog_posts` | `blog_posts_set_updated_at` | `set_updated_at` | `YES` |
| `public` | `campaign_runs` | `trg_check_campaign_can_send` | `check_campaign_can_send` | `YES` |
| `public` | `campaigns` | `account_lifecycle_campaign_activity` | `record_activity` | `YES` |
| `public` | `campaigns` | `account_lifecycle_campaign_edit` | `record_activity` | `YES` |
| `public` | `campaigns` | `campaigns_updated_at` | `set_updated_at` | `YES` |
| `public` | `campaigns` | `mailofly_campaigns_automation_delete_cleanup` | `mailofly_cleanup_campaign_automation_before_delete` | `YES` |
| `public` | `campaigns` | `mailofly_plan_campaigns_after_addon` | `mailofly_after_insert_campaign_addon` | `YES` |
| `public` | `campaigns` | `mailofly_plan_campaigns_insert` | `mailofly_enforce_plan_campaigns` | `YES` |
| `public` | `campaigns` | `mailofly_plan_campaigns_update` | `mailofly_enforce_plan_campaigns` | `YES` |
| `public` | `campaigns` | `platform_campaign_finished` | `capture_product_event` | `YES` |
| `public` | `campaigns` | `trg_enforce_campaign_status_transition` | `enforce_campaign_status_transition` | `YES` |
| `public` | `contact_segments` | `contact_segments_updated_at` | `set_updated_at` | `YES` |
| `public` | `contact_segments` | `mailofly_plan_segments_insert` | `mailofly_enforce_plan_segments` | `YES` |
| `public` | `contact_segments` | `managed_segment_guard` | `mailofly_managed_segment_guard` | `YES` |
| `public` | `contact_topics` | `native_subscription_guard` | `mailofly_subscription_guard` | `YES` |
| `public` | `contact_topics` | `native_subscription_projection` | `mailofly_subscription_projection` | `YES` |
| `public` | `contact_topics` | `subscription_deleted` | `mailofly_subscription_deleted` | `YES` |
| `public` | `contacts` | `contact_membership_projection` | `mailofly_contact_membership_projection` | `YES` |
| `public` | `contacts` | `mailofly_plan_contacts_insert` | `mailofly_enforce_plan_contacts` | `YES` |
| `public` | `contacts` | `native_blog_contact_labels` | `mailofly_blog_contact_labels` | `YES` |
| `public` | `emails` | `account_lifecycle_email_activity` | `record_activity` | `YES` |
| `public` | `emails` | `account_lifecycle_email_sent` | `record_activity` | `YES` |
| `public` | `emails` | `mailofly_email_sent_quota` | `mailofly_before_email_sent_quota` | `YES` |
| `public` | `emails` | `mailofly_emails_set_updated_at` | `mailofly_set_emails_updated_at` | `YES` |
| `public` | `emails` | `mailofly_plan_emails_insert` | `mailofly_enforce_plan_emails` | `YES` |
| `public` | `emails` | `preserve_email_outcome` | `mailofly_preserve_email_outcome` | `YES` |
| `public` | `emails` | `trg_prevent_duplicate_campaign_emails` | `prevent_duplicate_campaign_emails` | `YES` |
| `public` | `identities` | `account_lifecycle_sender_activity` | `record_activity` | `YES` |
| `public` | `identities` | `account_lifecycle_sender_edit` | `record_activity` | `YES` |
| `public` | `identities` | `identities_link_orphaned_emails_after_insert` | `mailofly_link_orphaned_emails_after_identity_insert` | `YES` |
| `public` | `identities` | `identities_sync_daily_usage_before_insert` | `mailofly_sync_identity_daily_usage_on_insert` | `YES` |
| `public` | `identities` | `identities_updated_at` | `set_updated_at` | `YES` |
| `public` | `identities` | `mailofly_plan_identities_after_addon` | `mailofly_after_insert_account_addon` | `YES` |
| `public` | `identities` | `mailofly_plan_identities_insert` | `mailofly_enforce_plan_accounts` | `YES` |
| `public` | `mailboxes` | `mailofly_mailbox_seats` | `mailofly_guard_mailbox_seats` | `YES` |
| `public` | `native_template_versions` | `immutable_native_template_version` | `mailofly_immutable_template_version` | `YES` |
| `public` | `newsletter_subscribers` | `legacy_newsletter_bridge` | `mailofly_legacy_newsletter_bridge` | `YES` |
| `public` | `oauth_access_tokens` | `account_lifecycle_oauth_use` | `record_activity` | `YES` |
| `public` | `organization_members` | `mailofly_keep_workspace_owner` | `mailofly_keep_workspace_owner` | `YES` |
| `public` | `organization_sending_protection` | `capture_reputation_notice` | `capture_reputation_notice` | `YES` |
| `public` | `organization_sending_protection` | `rotate_reputation_notice_revision` | `rotate_reputation_notice_revision` | `YES` |
| `public` | `organization_subscriptions` | `mailofly_subscription_apply_locks` | `mailofly_on_subscription_change_apply_locks` | `YES` |
| `public` | `organizations` | `initialize_org_billing_notice_state` | `initialize_org_billing_notice_state` | `YES` |
| `public` | `organizations` | `mailofly_guard_workspace_erasure` | `mailofly_guard_workspace_erasure` | `YES` |
| `public` | `organizations` | `organizations_updated_at` | `set_updated_at` | `YES` |
| `public` | `segment_contacts` | `managed_membership_guard` | `mailofly_managed_membership_guard` | `YES` |
| `public` | `segment_google_sheets` | `mailofly_plan_google_sheets_insert` | `mailofly_enforce_plan_google_sheets` | `YES` |
| `public` | `segment_google_sheets` | `segment_google_sheets_updated_at` | `set_updated_at` | `YES` |
| `public` | `sending_domains` | `account_lifecycle_domain_activity` | `record_activity` | `YES` |
| `public` | `sending_domains` | `account_lifecycle_domain_edit` | `record_activity` | `YES` |
| `public` | `sending_domains` | `mailofly_plan_domains_after_addon` | `mailofly_after_insert_domain_addon` | `YES` |
| `public` | `sending_domains` | `mailofly_plan_domains_insert` | `mailofly_enforce_plan_sending_domains` | `YES` |
| `public` | `support_ticket_messages` | `trg_support_ticket_message_inserted` | `touch_support_ticket_updated_at` | `YES` |
| `public` | `support_tickets` | `support_tickets_set_updated_at` | `set_updated_at` | `YES` |
| `public` | `template_editor_drafts` | `account_lifecycle_template_draft_edit` | `record_activity` | `YES` |
| `public` | `templates` | `a_native_template_guard` | `mailofly_guard_native_template` | `YES` |
| `public` | `templates` | `account_lifecycle_template_create` | `record_activity` | `YES` |
| `public` | `templates` | `account_lifecycle_template_edit` | `record_activity` | `YES` |
| `public` | `templates` | `mailofly_plan_templates_after_addon` | `mailofly_after_insert_template_addon` | `YES` |
| `public` | `templates` | `mailofly_plan_templates_insert` | `mailofly_enforce_plan_templates` | `YES` |
| `public` | `templates` | `template_editor_revision` | `mailofly_template_editor_revision` | `YES` |
| `public` | `templates` | `templates_updated_at` | `set_updated_at` | `YES` |
| `public` | `topics` | `managed_topic_guard` | `mailofly_managed_topic_guard` | `YES` |
| `public` | `user_onboarding_responses` | `user_onboarding_responses_updated_at` | `set_updated_at` | `YES` |
| `public` | `users` | `trg_users_protect_sensitive_columns` | `users_protect_sensitive_columns` | `YES` |
| `public` | `users` | `trg_users_sync_role_from_admin_role` | `users_sync_role_from_admin_role` | `YES` |
| `realtime` | `subscription` | `tr_check_filters` | `subscription_check_filters` | `YES` |
| `storage` | `buckets` | `enforce_bucket_name_length_trigger` | `enforce_bucket_name_length` | `YES` |
| `storage` | `buckets` | `enforce_versioning_status_transition` | `enforce_versioning_status_transition` | `YES` |
| `storage` | `buckets` | `protect_active_lifecycle_states` | `protect_active_lifecycle_states` | `YES` |
| `storage` | `buckets` | `protect_bucket_control_insert` | `protect_bucket_control_columns` | `YES` |
| `storage` | `buckets` | `protect_bucket_control_update` | `protect_bucket_control_columns` | `YES` |
| `storage` | `buckets` | `protect_bucket_control_update_role` | `enforce_bucket_lifecycle_service_role` | `YES` |
| `storage` | `buckets` | `protect_buckets_delete` | `protect_delete` | `YES` |
| `storage` | `buckets` | `wake_lifecycle_on_policy_write` | `wake_lifecycle_state` | `YES` |
| `storage` | `buckets` | `wake_lifecycle_on_versioning_enable` | `wake_lifecycle_state` | `YES` |
| `storage` | `objects` | `account_lifecycle_upload_activity` | `record_activity` | `YES` |
| `storage` | `objects` | `protect_objects_delete` | `protect_delete` | `YES` |
| `storage` | `objects` | `update_objects_updated_at` | `update_updated_at_column` | `YES` |
