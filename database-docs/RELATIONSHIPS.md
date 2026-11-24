# Database Relationships & Foreign Key Inventory

Total Declared Foreign Keys: **215**

| Constraint Name | Source Table | Source Column | Target Table | Target Column | On Delete | On Update |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `identities_user_id_fkey` | `auth.identities` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `mfa_amr_claims_session_id_fkey` | `auth.mfa_amr_claims` | `session_id` | `auth.sessions` | `id` | `CASCADE` | `a` |
| `mfa_challenges_auth_factor_id_fkey` | `auth.mfa_challenges` | `factor_id` | `auth.mfa_factors` | `id` | `CASCADE` | `a` |
| `mfa_factors_user_id_fkey` | `auth.mfa_factors` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `mfa_recovery_code_sets_mfa_factor_id_fkey` | `auth.mfa_recovery_code_sets` | `mfa_factor_id` | `auth.mfa_factors` | `id` | `CASCADE` | `a` |
| `mfa_recovery_code_sets_user_id_fkey` | `auth.mfa_recovery_code_sets` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `mfa_recovery_codes_mfa_recovery_code_set_id_fkey` | `auth.mfa_recovery_codes` | `mfa_recovery_code_set_id` | `auth.mfa_recovery_code_sets` | `id` | `CASCADE` | `a` |
| `oauth_authorizations_client_id_fkey` | `auth.oauth_authorizations` | `client_id` | `auth.oauth_clients` | `id` | `CASCADE` | `a` |
| `oauth_authorizations_user_id_fkey` | `auth.oauth_authorizations` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `oauth_consents_client_id_fkey` | `auth.oauth_consents` | `client_id` | `auth.oauth_clients` | `id` | `CASCADE` | `a` |
| `oauth_consents_user_id_fkey` | `auth.oauth_consents` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `one_time_tokens_user_id_fkey` | `auth.one_time_tokens` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `refresh_tokens_session_id_fkey` | `auth.refresh_tokens` | `session_id` | `auth.sessions` | `id` | `CASCADE` | `a` |
| `saml_providers_sso_provider_id_fkey` | `auth.saml_providers` | `sso_provider_id` | `auth.sso_providers` | `id` | `CASCADE` | `a` |
| `saml_relay_states_flow_state_id_fkey` | `auth.saml_relay_states` | `flow_state_id` | `auth.flow_state` | `id` | `CASCADE` | `a` |
| `saml_relay_states_sso_provider_id_fkey` | `auth.saml_relay_states` | `sso_provider_id` | `auth.sso_providers` | `id` | `CASCADE` | `a` |
| `scim_tokens_sso_provider_id_fkey` | `auth.scim_tokens` | `sso_provider_id` | `auth.sso_providers` | `id` | `CASCADE` | `a` |
| `scim_users_sso_provider_id_fkey` | `auth.scim_users` | `sso_provider_id` | `auth.sso_providers` | `id` | `CASCADE` | `a` |
| `scim_users_user_id_fkey` | `auth.scim_users` | `user_id` | `auth.users` | `id` | `SET NULL` | `a` |
| `sessions_oauth_client_id_fkey` | `auth.sessions` | `oauth_client_id` | `auth.oauth_clients` | `id` | `CASCADE` | `a` |
| `sessions_user_id_fkey` | `auth.sessions` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `sso_domains_sso_provider_id_fkey` | `auth.sso_domains` | `sso_provider_id` | `auth.sso_providers` | `id` | `CASCADE` | `a` |
| `webauthn_challenges_user_id_fkey` | `auth.webauthn_challenges` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `webauthn_credentials_user_id_fkey` | `auth.webauthn_credentials` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `account_lifecycle_notices_user_id_fkey` | `public.account_lifecycle_notices` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `account_lifecycle_state_user_id_fkey` | `public.account_lifecycle_state` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `admin_role_permissions_permission_id_fkey` | `public.admin_role_permissions` | `permission_id` | `public.admin_permissions` | `id` | `CASCADE` | `a` |
| `admin_role_permissions_role_id_fkey` | `public.admin_role_permissions` | `role_id` | `public.admin_roles` | `id` | `CASCADE` | `a` |
| `admin_roles_created_by_fkey` | `public.admin_roles` | `created_by` | `auth.users` | `id` | `SET NULL` | `a` |
| `api_key_request_logs_api_key_id_fkey` | `public.api_key_request_logs` | `api_key_id` | `public.api_keys` | `id` | `CASCADE` | `a` |
| `api_key_request_logs_email_id_fkey` | `public.api_key_request_logs` | `email_id` | `public.emails` | `id` | `SET NULL` | `a` |
| `api_key_request_logs_user_id_fkey` | `public.api_key_request_logs` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `api_keys_organization_id_fkey` | `public.api_keys` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `api_keys_user_id_fkey` | `public.api_keys` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `automation_event_receipts_organization_id_fkey` | `public.automation_event_receipts` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `automation_events_organization_id_fkey` | `public.automation_events` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `automation_events_user_id_fkey` | `public.automation_events` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `automation_run_steps_run_id_fkey` | `public.automation_run_steps` | `run_id` | `public.automation_runs` | `id` | `CASCADE` | `a` |
| `automation_runs_automation_id_fkey` | `public.automation_runs` | `automation_id` | `public.automations` | `id` | `CASCADE` | `a` |
| `automation_runs_contact_id_fkey` | `public.automation_runs` | `contact_id` | `public.contacts` | `id` | `SET NULL` | `a` |
| `automation_runs_organization_id_fkey` | `public.automation_runs` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `automation_waiting_events_automation_id_fkey` | `public.automation_waiting_events` | `automation_id` | `public.automations` | `id` | `CASCADE` | `a` |
| `automation_waiting_events_contact_id_fkey` | `public.automation_waiting_events` | `contact_id` | `public.contacts` | `id` | `CASCADE` | `a` |
| `automation_waiting_events_organization_id_fkey` | `public.automation_waiting_events` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `automation_waiting_events_run_id_fkey` | `public.automation_waiting_events` | `run_id` | `public.automation_runs` | `id` | `CASCADE` | `a` |
| `automations_organization_id_fkey` | `public.automations` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `automations_user_id_fkey` | `public.automations` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `billing_addon_orders_addon_id_fkey` | `public.billing_addon_orders` | `addon_id` | `public.billing_addons` | `id` | `RESTRICT` | `a` |
| `billing_addon_orders_organization_id_fkey` | `public.billing_addon_orders` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `billing_addon_orders_user_id_fkey` | `public.billing_addon_orders` | `user_id` | `public.users` | `id` | `CASCADE` | `a` |
| `billing_dodo_snapshots_organization_id_fkey` | `public.billing_dodo_snapshots` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `billing_fulfilled_payments_organization_id_fkey` | `public.billing_fulfilled_payments` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `billing_payment_ledger_organization_id_fkey` | `public.billing_payment_ledger` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `billing_payment_ledger_plan_id_fkey` | `public.billing_payment_ledger` | `plan_id` | `public.plans` | `id` | `NO ACTION` | `a` |
| `blog_posts_author_id_fkey` | `public.blog_posts` | `author_id` | `public.blog_authors` | `id` | `RESTRICT` | `a` |
| `blog_posts_category_id_fkey` | `public.blog_posts` | `category_id` | `public.blog_categories` | `id` | `SET NULL` | `a` |
| `campaign_run_audience_campaign_run_id_fkey` | `public.campaign_run_audience` | `campaign_run_id` | `public.campaign_runs` | `id` | `CASCADE` | `a` |
| `campaign_run_audience_contact_id_fkey` | `public.campaign_run_audience` | `contact_id` | `public.contacts` | `id` | `CASCADE` | `a` |
| `campaign_run_audience_organization_id_fkey` | `public.campaign_run_audience` | `organization_id` | `public.organizations` | `id` | `NO ACTION` | `a` |
| `campaign_runs_campaign_id_fkey` | `public.campaign_runs` | `campaign_id` | `public.campaigns` | `id` | `CASCADE` | `a` |
| `campaign_runs_native_template_version_id_fkey` | `public.campaign_runs` | `native_template_version_id` | `public.native_template_versions` | `id` | `SET NULL` | `a` |
| `campaign_runs_organization_id_fkey` | `public.campaign_runs` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `campaign_runs_user_id_fkey` | `public.campaign_runs` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `campaign_sending_holds_campaign_id_fkey` | `public.campaign_sending_holds` | `campaign_id` | `public.campaigns` | `id` | `CASCADE` | `a` |
| `campaign_sending_holds_organization_id_fkey` | `public.campaign_sending_holds` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `campaigns_folder_id_fkey` | `public.campaigns` | `segment_id` | `public.contact_segments` | `id` | `SET NULL` | `a` |
| `campaigns_organization_id_fkey` | `public.campaigns` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `campaigns_template_id_fkey` | `public.campaigns` | `template_id` | `public.templates` | `id` | `SET NULL` | `a` |
| `campaigns_topic_id_fkey` | `public.campaigns` | `topic_id` | `public.topics` | `id` | `SET NULL` | `a` |
| `campaigns_user_id_fkey` | `public.campaigns` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `contact_properties_organization_id_fkey` | `public.contact_properties` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `contact_property_values_contact_id_fkey` | `public.contact_property_values` | `contact_id` | `public.contacts` | `id` | `CASCADE` | `a` |
| `contact_property_values_organization_id_fkey` | `public.contact_property_values` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `contact_property_values_property_id_fkey` | `public.contact_property_values` | `property_id` | `public.contact_properties` | `id` | `CASCADE` | `a` |
| `contact_segments_managed_topic_id_fkey` | `public.contact_segments` | `managed_topic_id` | `public.topics` | `id` | `RESTRICT` | `a` |
| `contact_segments_organization_id_fkey` | `public.contact_segments` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `recipient_folders_user_id_fkey` | `public.contact_segments` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `contact_subscription_challenges_email_id_fkey` | `public.contact_subscription_challenges` | `email_id` | `public.emails` | `id` | `SET NULL` | `a` |
| `contact_subscription_challenges_subscription_id_fkey` | `public.contact_subscription_challenges` | `subscription_id` | `public.contact_topics` | `id` | `CASCADE` | `a` |
| `contact_subscription_events_contact_id_fkey` | `public.contact_subscription_events` | `contact_id` | `public.contacts` | `id` | `CASCADE` | `a` |
| `contact_subscription_events_organization_id_fkey` | `public.contact_subscription_events` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `contact_subscription_events_topic_id_fkey` | `public.contact_subscription_events` | `topic_id` | `public.topics` | `id` | `CASCADE` | `a` |
| `contact_topics_contact_id_fkey` | `public.contact_topics` | `contact_id` | `public.contacts` | `id` | `CASCADE` | `a` |
| `contact_topics_organization_id_fkey` | `public.contact_topics` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `contact_topics_topic_id_fkey` | `public.contact_topics` | `topic_id` | `public.topics` | `id` | `CASCADE` | `a` |
| `contacts_organization_id_fkey` | `public.contacts` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `recipients_user_id_fkey` | `public.contacts` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `email_send_confirmations_organization_id_fkey` | `public.email_send_confirmations` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `email_send_confirmations_user_id_fkey` | `public.email_send_confirmations` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `email_usage_operations_organization_id_fkey` | `public.email_usage_operations` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `email_usage_operations_period_id_fkey` | `public.email_usage_operations` | `period_id` | `public.organization_email_periods` | `id` | `CASCADE` | `a` |
| `emails_account_id_fkey` | `public.emails` | `account_id` | `public.identities` | `id` | `SET NULL` | `a` |
| `emails_api_key_id_fkey` | `public.emails` | `api_key_id` | `public.api_keys` | `id` | `SET NULL` | `a` |
| `emails_campaign_id_fkey` | `public.emails` | `campaign_id` | `public.campaigns` | `id` | `CASCADE` | `a` |
| `emails_campaign_run_id_fkey` | `public.emails` | `campaign_run_id` | `public.campaign_runs` | `id` | `CASCADE` | `a` |
| `emails_contact_id_fkey` | `public.emails` | `contact_id` | `public.contacts` | `id` | `SET NULL` | `a` |
| `emails_organization_id_fkey` | `public.emails` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `emails_user_id_fkey` | `public.emails` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `help_ai_queries_organization_id_fkey` | `public.help_ai_queries` | `organization_id` | `public.organizations` | `id` | `SET NULL` | `a` |
| `help_ai_queries_user_id_fkey` | `public.help_ai_queries` | `user_id` | `auth.users` | `id` | `SET NULL` | `a` |
| `identities_organization_id_fkey` | `public.identities` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `identities_user_id_fkey` | `public.identities` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `mailbox_aliases_mailbox_id_fkey` | `public.mailbox_aliases` | `mailbox_id` | `public.mailboxes` | `id` | `CASCADE` | `a` |
| `mailbox_aliases_organization_id_fkey` | `public.mailbox_aliases` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `mailboxes_created_by_fkey` | `public.mailboxes` | `created_by` | `auth.users` | `id` | `CASCADE` | `a` |
| `mailboxes_domain_id_fkey` | `public.mailboxes` | `domain_id` | `public.sending_domains` | `id` | `RESTRICT` | `a` |
| `mailboxes_organization_id_fkey` | `public.mailboxes` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `mailofly_user_mail_queue_cron_user_id_fkey` | `public.mailofly_user_mail_queue_cron` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `managed_audience_programs_organization_id_fkey` | `public.managed_audience_programs` | `organization_id` | `public.organizations` | `id` | `NO ACTION` | `a` |
| `managed_audience_programs_segment_id_fkey` | `public.managed_audience_programs` | `segment_id` | `public.contact_segments` | `id` | `NO ACTION` | `a` |
| `managed_audience_programs_topic_id_fkey` | `public.managed_audience_programs` | `topic_id` | `public.topics` | `id` | `NO ACTION` | `a` |
| `managed_audience_programs_user_id_fkey` | `public.managed_audience_programs` | `user_id` | `auth.users` | `id` | `NO ACTION` | `a` |
| `native_template_versions_created_by_fkey` | `public.native_template_versions` | `created_by` | `auth.users` | `id` | `SET NULL` | `a` |
| `native_template_versions_organization_id_fkey` | `public.native_template_versions` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `native_template_versions_template_id_fkey` | `public.native_template_versions` | `template_id` | `public.templates` | `id` | `CASCADE` | `a` |
| `oauth_access_tokens_client_id_fkey` | `public.oauth_access_tokens` | `client_id` | `public.oauth_clients` | `client_id` | `CASCADE` | `a` |
| `oauth_access_tokens_organization_id_fkey` | `public.oauth_access_tokens` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `oauth_access_tokens_user_id_fkey` | `public.oauth_access_tokens` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `oauth_authorization_codes_client_id_fkey` | `public.oauth_authorization_codes` | `client_id` | `public.oauth_clients` | `client_id` | `CASCADE` | `a` |
| `oauth_authorization_codes_organization_id_fkey` | `public.oauth_authorization_codes` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `oauth_authorization_codes_user_id_fkey` | `public.oauth_authorization_codes` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `oauth_authorization_requests_client_id_fkey` | `public.oauth_authorization_requests` | `client_id` | `public.oauth_clients` | `client_id` | `CASCADE` | `a` |
| `oauth_authorization_requests_organization_id_fkey` | `public.oauth_authorization_requests` | `organization_id` | `public.organizations` | `id` | `SET NULL` | `a` |
| `oauth_authorization_requests_user_id_fkey` | `public.oauth_authorization_requests` | `user_id` | `auth.users` | `id` | `SET NULL` | `a` |
| `oauth_clients_organization_id_fkey` | `public.oauth_clients` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `oauth_clients_user_id_fkey` | `public.oauth_clients` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `oauth_refresh_tokens_access_token_id_fkey` | `public.oauth_refresh_tokens` | `access_token_id` | `public.oauth_access_tokens` | `id` | `CASCADE` | `a` |
| `oauth_refresh_tokens_client_id_fkey` | `public.oauth_refresh_tokens` | `client_id` | `public.oauth_clients` | `client_id` | `CASCADE` | `a` |
| `oauth_refresh_tokens_organization_id_fkey` | `public.oauth_refresh_tokens` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `oauth_refresh_tokens_user_id_fkey` | `public.oauth_refresh_tokens` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `organization_addon_subscriptions_organization_id_fkey` | `public.organization_addon_subscriptions` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `user_addons_addon_id_fkey` | `public.organization_addons` | `addon_id` | `public.billing_addons` | `id` | `RESTRICT` | `a` |
| `user_addons_organization_id_fkey` | `public.organization_addons` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_billing_notifications_organization_id_fkey` | `public.organization_billing_notifications` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_billing_notifications_user_id_fkey` | `public.organization_billing_notifications` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `organization_billing_plan_state_organization_id_fkey` | `public.organization_billing_plan_state` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_credit_transactions_organization_id_fkey` | `public.organization_credit_transactions` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_email_days_organization_id_fkey` | `public.organization_email_days` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_email_periods_organization_id_fkey` | `public.organization_email_periods` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_email_policy_organization_id_fkey` | `public.organization_email_policy` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_invitations_invited_by_fkey` | `public.organization_invitations` | `invited_by` | `auth.users` | `id` | `CASCADE` | `a` |
| `organization_invitations_organization_id_fkey` | `public.organization_invitations` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_members_organization_id_fkey` | `public.organization_members` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_members_user_id_fkey` | `public.organization_members` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `organization_payment_notice_state_organization_id_fkey` | `public.organization_payment_notice_state` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_sending_protection_organization_id_fkey` | `public.organization_sending_protection` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organization_subscriptions_marketing_plan_id_fkey` | `public.organization_subscriptions` | `marketing_plan_id` | `public.plans` | `id` | `NO ACTION` | `a` |
| `user_subscriptions_organization_id_fkey` | `public.organization_subscriptions` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `user_subscriptions_plan_id_fkey` | `public.organization_subscriptions` | `plan_id` | `public.plans` | `id` | `RESTRICT` | `a` |
| `user_usage_organization_id_fkey` | `public.organization_usage` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `organizations_created_by_fkey` | `public.organizations` | `created_by` | `auth.users` | `id` | `SET NULL` | `a` |
| `platform_email_deliveries_email_id_fkey` | `public.platform_email_deliveries` | `email_id` | `public.emails` | `id` | `SET NULL` | `a` |
| `platform_email_preferences_organization_id_fkey` | `public.platform_email_preferences` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `platform_email_preferences_user_id_fkey` | `public.platform_email_preferences` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `platform_notification_events_organization_id_fkey` | `public.platform_notification_events` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `platform_notification_events_user_id_fkey` | `public.platform_notification_events` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `received_emails_domain_id_fkey` | `public.received_emails` | `domain_id` | `public.sending_domains` | `id` | `SET NULL` | `a` |
| `received_emails_organization_id_fkey` | `public.received_emails` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `received_emails_user_id_fkey` | `public.received_emails` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `referral_earnings_organization_id_fkey` | `public.referral_earnings` | `organization_id` | `public.organizations` | `id` | `SET NULL` | `a` |
| `referral_earnings_plan_id_fkey` | `public.referral_earnings` | `plan_id` | `public.plans` | `id` | `SET NULL` | `a` |
| `referral_earnings_referred_user_id_fkey` | `public.referral_earnings` | `referred_user_id` | `public.users` | `id` | `CASCADE` | `a` |
| `referral_earnings_referrer_user_id_fkey` | `public.referral_earnings` | `referrer_user_id` | `public.users` | `id` | `CASCADE` | `a` |
| `referral_payout_methods_user_id_fkey` | `public.referral_payout_methods` | `user_id` | `public.users` | `id` | `CASCADE` | `a` |
| `referral_withdrawal_requests_payout_method_id_fkey` | `public.referral_withdrawal_requests` | `payout_method_id` | `public.referral_payout_methods` | `id` | `SET NULL` | `a` |
| `referral_withdrawal_requests_user_id_fkey` | `public.referral_withdrawal_requests` | `user_id` | `public.users` | `id` | `CASCADE` | `a` |
| `folder_recipients_folder_id_fkey` | `public.segment_contacts` | `segment_id` | `public.contact_segments` | `id` | `CASCADE` | `a` |
| `folder_recipients_recipient_id_fkey` | `public.segment_contacts` | `contact_id` | `public.contacts` | `id` | `CASCADE` | `a` |
| `segment_google_sheets_organization_id_fkey` | `public.segment_google_sheets` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `segment_google_sheets_segment_id_fkey` | `public.segment_google_sheets` | `segment_id` | `public.contact_segments` | `id` | `CASCADE` | `a` |
| `segment_google_sheets_user_id_fkey` | `public.segment_google_sheets` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `sending_domains_organization_id_fkey` | `public.sending_domains` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `sending_domains_user_id_fkey` | `public.sending_domains` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `ses_event_log_email_id_fkey` | `public.ses_event_log` | `email_id` | `public.emails` | `id` | `SET NULL` | `a` |
| `ses_event_log_organization_id_fkey` | `public.ses_event_log` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `ses_organization_tenants_organization_id_fkey` | `public.ses_organization_tenants` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `ses_recipient_outcomes_organization_id_fkey` | `public.ses_recipient_outcomes` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `ses_send_attempts_organization_id_fkey` | `public.ses_send_attempts` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `smtp_credentials_created_by_fkey` | `public.smtp_credentials` | `created_by` | `auth.users` | `id` | `CASCADE` | `a` |
| `smtp_credentials_organization_id_fkey` | `public.smtp_credentials` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `smtp_credentials_prefer_account_id_fkey` | `public.smtp_credentials` | `prefer_account_id` | `public.identities` | `id` | `SET NULL` | `a` |
| `supabase_integrations_created_by_fkey` | `public.supabase_integrations` | `created_by` | `auth.users` | `id` | `CASCADE` | `a` |
| `supabase_integrations_organization_id_fkey` | `public.supabase_integrations` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `supabase_integrations_template_id_fkey` | `public.supabase_integrations` | `template_id` | `public.templates` | `id` | `SET NULL` | `a` |
| `support_ticket_messages_sender_id_fkey` | `public.support_ticket_messages` | `sender_id` | `public.users` | `id` | `CASCADE` | `a` |
| `support_ticket_messages_ticket_id_fkey` | `public.support_ticket_messages` | `ticket_id` | `public.support_tickets` | `id` | `CASCADE` | `a` |
| `support_tickets_created_by_fkey` | `public.support_tickets` | `created_by` | `auth.users` | `id` | `CASCADE` | `a` |
| `template_editor_drafts_organization_id_fkey` | `public.template_editor_drafts` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `template_editor_drafts_template_id_fkey` | `public.template_editor_drafts` | `template_id` | `public.templates` | `id` | `CASCADE` | `a` |
| `template_editor_drafts_user_id_fkey` | `public.template_editor_drafts` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `templates_native_published_fk` | `public.templates` | `published_native_version_id` | `public.native_template_versions` | `id` | `SET NULL` | `a` |
| `templates_organization_id_fkey` | `public.templates` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `templates_user_id_fkey` | `public.templates` | `user_id` | `auth.users` | `id` | `CASCADE` | `a` |
| `tenant_suppression_list_organization_id_fkey` | `public.tenant_suppression_list` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `topics_organization_id_fkey` | `public.topics` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `user_notifications_user_id_fkey` | `public.user_notifications` | `user_id` | `public.users` | `id` | `CASCADE` | `a` |
| `user_onboarding_responses_user_id_fkey` | `public.user_onboarding_responses` | `user_id` | `public.users` | `id` | `CASCADE` | `a` |
| `users_admin_role_id_fkey` | `public.users` | `admin_role_id` | `public.admin_roles` | `id` | `SET NULL` | `a` |
| `users_default_organization_id_fkey` | `public.users` | `default_organization_id` | `public.organizations` | `id` | `SET NULL` | `a` |
| `users_id_fkey` | `public.users` | `id` | `auth.users` | `id` | `CASCADE` | `a` |
| `users_referredby_fkey` | `public.users` | `referredby` | `public.users` | `id` | `SET NULL` | `a` |
| `users_role_fkey` | `public.users` | `role` | `public.roles` | `name` | `NO ACTION` | `a` |
| `webhook_deliveries_organization_id_fkey` | `public.webhook_deliveries` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `webhook_deliveries_received_email_id_fkey` | `public.webhook_deliveries` | `received_email_id` | `public.received_emails` | `id` | `SET NULL` | `a` |
| `webhook_deliveries_webhook_id_fkey` | `public.webhook_deliveries` | `webhook_id` | `public.webhooks` | `id` | `CASCADE` | `a` |
| `webhooks_created_by_fkey` | `public.webhooks` | `created_by` | `auth.users` | `id` | `CASCADE` | `a` |
| `webhooks_organization_id_fkey` | `public.webhooks` | `organization_id` | `public.organizations` | `id` | `CASCADE` | `a` |
| `workspace_uploads_organization_id_fkey` | `public.workspace_uploads` | `organization_id` | `public.organizations` | `id` | `RESTRICT` | `a` |
| `workspace_uploads_user_id_fkey` | `public.workspace_uploads` | `user_id` | `auth.users` | `id` | `SET NULL` | `a` |
| `bucket_lifecycle_states_bucket_id_fkey` | `storage.bucket_lifecycle_states` | `bucket_id` | `storage.buckets` | `id` | `CASCADE` | `a` |
| `objects_bucketId_fkey` | `storage.objects` | `bucket_id` | `storage.buckets` | `id` | `NO ACTION` | `a` |
| `s3_multipart_uploads_bucket_id_fkey` | `storage.s3_multipart_uploads` | `bucket_id` | `storage.buckets` | `id` | `NO ACTION` | `a` |
| `s3_multipart_uploads_parts_bucket_id_fkey` | `storage.s3_multipart_uploads_parts` | `bucket_id` | `storage.buckets` | `id` | `NO ACTION` | `a` |
| `s3_multipart_uploads_parts_upload_id_fkey` | `storage.s3_multipart_uploads_parts` | `upload_id` | `storage.s3_multipart_uploads` | `id` | `CASCADE` | `a` |
| `vector_indexes_bucket_id_fkey` | `storage.vector_indexes` | `bucket_id` | `storage.buckets_vectors` | `id` | `NO ACTION` | `a` |
