# Complete Database Data Dictionary

Comprehensive catalog of all 111 application tables/views and 1,771 columns in the `public` schema.

## Table: `public.account_lifecycle_deletions`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 24,576 bytes (Table: 0 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `account_fingerprint` | `text` | `NO` | - | - |
| 3 | `cycle_id` | `uuid` | `NO` | - | - |
| 4 | `policy_version` | `integer` | `NO` | - | - |
| 5 | `last_activity_at` | `timestamp with time zone` | `NO` | - | - |
| 6 | `first_warning_at` | `timestamp with time zone` | `NO` | - | - |
| 7 | `second_warning_at` | `timestamp with time zone` | `NO` | - | - |
| 8 | `final_notice_at` | `timestamp with time zone` | `NO` | - | - |
| 9 | `deleted_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.account_lifecycle_notices`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 24,576 bytes (Table: 0 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `user_id` | `uuid` | `NO` | - | - |
| 2 | `cycle_id` | `uuid` | `NO` | - | - |
| 3 | `stage` | `integer` | `NO` | - | - |
| 4 | `occurrence_key` | `text` | `NO` | - | - |
| 5 | `delivered_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.account_lifecycle_policy`
- **Type**: `TABLE` | **Estimated Rows**: 1 | **RLS**: `ENABLED`
- **Total Bytes**: 57,344 bytes (Table: 8,192 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `boolean` | `NO` | `true` | - |
| 2 | `enabled` | `boolean` | `NO` | `false` | - |
| 3 | `deletion_enabled` | `boolean` | `NO` | `false` | - |
| 4 | `scan_after` | `uuid` | `YES` | - | - |
| 5 | `version` | `integer` | `NO` | `1` | - |

---

## Table: `public.account_lifecycle_state`
- **Type**: `TABLE` | **Estimated Rows**: 281 | **RLS**: `ENABLED`
- **Total Bytes**: 114,688 bytes (Table: 24,576 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `user_id` | `uuid` | `NO` | - | - |
| 2 | `cycle_id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 3 | `last_activity_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 4 | `has_activated` | `boolean` | `NO` | `false` | - |
| 5 | `last_deletion_hold` | `text` | `YES` | - | - |
| 6 | `suppressed` | `boolean` | `NO` | `false` | - |

---

## Table: `public.accounts`
- **Type**: `VIEW` | **Estimated Rows**: -1 | **RLS**: `DISABLED`
- **Total Bytes**: 0 bytes (Table: 0 bytes, Indexes: 0 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `YES` | - | - |
| 2 | `user_id` | `uuid` | `YES` | - | - |
| 3 | `provider_type` | `USER-DEFINED` | `YES` | - | - |
| 4 | `name` | `text` | `YES` | - | - |
| 5 | `smtp_host` | `text` | `YES` | - | - |
| 6 | `smtp_port` | `smallint` | `YES` | - | - |
| 7 | `smtp_username` | `text` | `YES` | - | - |
| 8 | `smtp_password` | `text` | `YES` | - | - |
| 9 | `google_access_token` | `text` | `YES` | - | - |
| 10 | `google_refresh_token` | `text` | `YES` | - | - |
| 11 | `google_email` | `text` | `YES` | - | - |
| 12 | `created_at` | `timestamp with time zone` | `YES` | - | - |
| 13 | `updated_at` | `timestamp with time zone` | `YES` | - | - |
| 14 | `daily_mail_limit` | `integer` | `YES` | - | - |
| 15 | `daily_mail_used` | `integer` | `YES` | - | - |
| 16 | `daily_mail_used_date` | `date` | `YES` | - | - |
| 17 | `google_expires_at` | `timestamp with time zone` | `YES` | - | - |
| 18 | `google_scope` | `text` | `YES` | - | - |
| 19 | `google_token_type` | `text` | `YES` | - | - |
| 20 | `account_key` | `text` | `YES` | - | - |
| 21 | `provisioned_by` | `USER-DEFINED` | `YES` | - | - |
| 22 | `custom_from_email` | `text` | `YES` | - | - |
| 23 | `custom_from_display_name` | `text` | `YES` | - | - |
| 24 | `billing_locked` | `boolean` | `YES` | - | - |
| 25 | `organization_id` | `uuid` | `YES` | - | - |
| 26 | `is_active` | `boolean` | `YES` | - | - |

---

## Table: `public.admin_permissions`
- **Type**: `TABLE` | **Estimated Rows**: 15 | **RLS**: `ENABLED`
- **Total Bytes**: 65,536 bytes (Table: 8,192 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `text` | `NO` | - | - |
| 2 | `name` | `text` | `NO` | - | - |
| 3 | `description` | `text` | `YES` | - | - |
| 4 | `category` | `text` | `NO` | - | - |
| 5 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.admin_role_permissions`
- **Type**: `TABLE` | **Estimated Rows**: 64 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 8,192 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `role_id` | `uuid` | `NO` | - | - |
| 2 | `permission_id` | `text` | `NO` | - | - |
| 3 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.admin_roles`
- **Type**: `TABLE` | **Estimated Rows**: 10 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 8,192 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `name` | `text` | `NO` | - | - |
| 3 | `label` | `text` | `NO` | - | - |
| 4 | `description` | `text` | `YES` | - | - |
| 5 | `is_system` | `boolean` | `NO` | `false` | - |
| 6 | `created_by` | `uuid` | `YES` | - | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.api_key_request_logs`
- **Type**: `TABLE` | **Estimated Rows**: 485 | **RLS**: `ENABLED`
- **Total Bytes**: 10,297,344 bytes (Table: 1,695,744 bytes, Indexes: 1,064,960 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `api_key_id` | `uuid` | `NO` | - | - |
| 3 | `user_id` | `uuid` | `NO` | - | - |
| 4 | `method` | `text` | `NO` | - | - |
| 5 | `path` | `text` | `NO` | - | - |
| 6 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `request_body` | `text` | `YES` | - | - |
| 8 | `response_body` | `text` | `YES` | - | - |
| 9 | `user_agent` | `text` | `YES` | - | - |
| 10 | `status_code` | `integer` | `NO` | `200` | - |
| 11 | `email_id` | `uuid` | `YES` | - | - |
| 12 | `ip_address` | `text` | `YES` | - | - |
| 13 | `duration_ms` | `integer` | `YES` | - | - |

---

## Table: `public.api_keys`
- **Type**: `TABLE` | **Estimated Rows**: 76 | **RLS**: `ENABLED`
- **Total Bytes**: 229,376 bytes (Table: 65,536 bytes, Indexes: 122,880 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `name` | `text` | `NO` | `'API key'::text` | - |
| 4 | `key_hash` | `text` | `NO` | - | - |
| 5 | `secret_suffix` | `text` | `NO` | - | - |
| 6 | `expires_at` | `timestamp with time zone` | `YES` | - | - |
| 7 | `last_used_at` | `timestamp with time zone` | `YES` | - | - |
| 8 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 10 | `organization_id` | `uuid` | `NO` | - | - |

---

## Table: `public.app_settings`
- **Type**: `TABLE` | **Estimated Rows**: 18 | **RLS**: `ENABLED`
- **Total Bytes**: 65,536 bytes (Table: 8,192 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `key` | `text` | `NO` | - | - |
| 2 | `value` | `text` | `NO` | - | - |
| 3 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 4 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.automation_event_receipts`
- **Type**: `TABLE` | **Estimated Rows**: 310 | **RLS**: `ENABLED`
- **Total Bytes**: 188,416 bytes (Table: 49,152 bytes, Indexes: 98,304 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `event_name` | `text` | `NO` | - | - |
| 4 | `status` | `text` | `NO` | `'processing'::text` | - |
| 5 | `runs_started` | `integer` | `NO` | `0` | - |
| 6 | `waits_resumed` | `integer` | `NO` | `0` | - |
| 7 | `error_code` | `text` | `YES` | - | - |
| 8 | `support_reference` | `text` | `YES` | - | - |
| 9 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 10 | `completed_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.automation_events`
- **Type**: `TABLE` | **Estimated Rows**: 10 | **RLS**: `ENABLED`
- **Total Bytes**: 106,496 bytes (Table: 16,384 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `user_id` | `uuid` | `NO` | - | - |
| 4 | `name` | `text` | `NO` | - | - |
| 5 | `description` | `text` | `YES` | - | - |
| 6 | `schema` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 9 | `properties` | `jsonb` | `YES` | `'[]'::jsonb` | - |

---

## Table: `public.automation_run_steps`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 73,728 bytes (Table: 0 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `run_id` | `uuid` | `NO` | - | - |
| 3 | `step_key` | `text` | `NO` | - | - |
| 4 | `step_type` | `text` | `NO` | - | - |
| 5 | `status` | `text` | `NO` | `'pending'::text` | - |
| 6 | `output` | `jsonb` | `YES` | - | - |
| 7 | `error` | `text` | `YES` | - | - |
| 8 | `started_at` | `timestamp with time zone` | `YES` | - | - |
| 9 | `completed_at` | `timestamp with time zone` | `YES` | - | - |
| 10 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.automation_runs`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 90,112 bytes (Table: 0 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `automation_id` | `uuid` | `NO` | - | - |
| 3 | `organization_id` | `uuid` | `NO` | - | - |
| 4 | `contact_id` | `uuid` | `YES` | - | - |
| 5 | `trigger_event_name` | `text` | `NO` | - | - |
| 6 | `trigger_event_payload` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 7 | `status` | `text` | `NO` | `'running'::text` | - |
| 8 | `current_step_key` | `text` | `YES` | - | - |
| 9 | `context` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 10 | `error` | `text` | `YES` | - | - |
| 11 | `started_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 12 | `completed_at` | `timestamp with time zone` | `YES` | - | - |
| 13 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.automation_waiting_events`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 32,768 bytes (Table: 0 bytes, Indexes: 24,576 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `run_id` | `uuid` | `NO` | - | - |
| 3 | `automation_id` | `uuid` | `NO` | - | - |
| 4 | `organization_id` | `uuid` | `NO` | - | - |
| 5 | `contact_id` | `uuid` | `NO` | - | - |
| 6 | `step_key` | `text` | `NO` | - | - |
| 7 | `event_name` | `text` | `NO` | - | - |
| 8 | `filter_rule` | `jsonb` | `YES` | - | - |
| 9 | `timeout_at` | `timestamp with time zone` | `NO` | - | - |
| 10 | `timeout_job_id` | `text` | `YES` | - | - |
| 11 | `status` | `text` | `NO` | `'waiting'::text` | - |
| 12 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.automations`
- **Type**: `TABLE` | **Estimated Rows**: 15 | **RLS**: `ENABLED`
- **Total Bytes**: 163,840 bytes (Table: 73,728 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `user_id` | `uuid` | `NO` | - | - |
| 4 | `name` | `text` | `NO` | - | - |
| 5 | `status` | `text` | `NO` | `'disabled'::text` | - |
| 6 | `steps` | `jsonb` | `NO` | `'[]'::jsonb` | - |
| 7 | `connections` | `jsonb` | `NO` | `'[]'::jsonb` | - |
| 8 | `total_runs` | `integer` | `NO` | `0` | - |
| 9 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 10 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 11 | `trigger` | `jsonb` | `YES` | `'{}'::jsonb` | - |

---

## Table: `public.billing_addon_orders`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 0 bytes, Indexes: 73,728 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `addon_id` | `uuid` | `YES` | - | - |
| 4 | `quantity` | `integer` | `YES` | - | - |
| 5 | `amount_minor` | `bigint` | `NO` | - | - |
| 6 | `currency` | `text` | `NO` | `'INR'::text` | - |
| 8 | `status` | `text` | `NO` | `'created'::text` | - |
| 10 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 11 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 12 | `line_items` | `jsonb` | `YES` | - | Array of {addon_id, quantity} when multi-line; legacy rows use addon_id + quantity only. |
| 13 | `organization_id` | `uuid` | `NO` | - | - |
| 14 | `payment_provider` | `text` | `YES` | `'dodopayments'::text` | Gateway used for this add-on checkout. |
| 15 | `dodo_checkout_session_id` | `text` | `YES` | - | - |
| 16 | `dodo_payment_id` | `text` | `YES` | - | - |

---

## Table: `public.billing_addons`
- **Type**: `TABLE` | **Estimated Rows**: 5 | **RLS**: `ENABLED`
- **Total Bytes**: 131,072 bytes (Table: 8,192 bytes, Indexes: 81,920 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `slug` | `text` | `NO` | - | - |
| 3 | `name` | `text` | `NO` | - | - |
| 4 | `unit_kind` | `text` | `NO` | - | - |
| 5 | `price_per_unit_usd` | `numeric` | `NO` | - | - |
| 7 | `sort_order` | `integer` | `NO` | `0` | - |
| 8 | `is_active` | `boolean` | `NO` | `true` | - |
| 9 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 10 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 11 | `dodo_product_id` | `text` | `YES` | - | Dodo Payments one-time product id for add-on checkout. |
| 12 | `dodo_product_id_test` | `text` | `YES` | - | Dodo Payments Test Mode (sandbox) one-time add-on product id. |
| 13 | `dodo_product_id_live` | `text` | `YES` | - | Dodo Payments Live Mode (production) one-time add-on product id. |

---

## Table: `public.billing_dodo_snapshots`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 32,768 bytes (Table: 8,192 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `environment` | `text` | `NO` | - | - |
| 2 | `subscription_id` | `text` | `NO` | - | - |
| 3 | `organization_id` | `uuid` | `NO` | - | - |
| 4 | `product_type` | `text` | `NO` | - | - |
| 5 | `provider_status` | `text` | `NO` | - | - |
| 6 | `observed_at` | `timestamp with time zone` | `NO` | - | - |

---

## Table: `public.billing_fulfilled_payments`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 16,384 bytes (Table: 0 bytes, Indexes: 8,192 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `environment` | `text` | `NO` | - | - |
| 2 | `payment_id` | `text` | `NO` | - | - |
| 3 | `organization_id` | `uuid` | `NO` | - | - |
| 4 | `fulfilled_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.billing_payment_ledger`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 49,152 bytes (Table: 8,192 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `environment` | `text` | `NO` | - | - |
| 2 | `payment_id` | `text` | `NO` | - | - |
| 3 | `organization_id` | `uuid` | `NO` | - | - |
| 4 | `subscription_id` | `text` | `NO` | - | - |
| 5 | `plan_id` | `uuid` | `NO` | - | - |
| 6 | `product_type` | `text` | `NO` | - | - |
| 7 | `amount_minor` | `bigint` | `NO` | - | - |
| 8 | `currency` | `text` | `NO` | - | - |
| 9 | `period_start` | `timestamp with time zone` | `NO` | - | - |
| 10 | `period_end` | `timestamp with time zone` | `NO` | - | - |
| 11 | `refunded` | `boolean` | `NO` | `false` | - |
| 12 | `verified_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.billing_webhook_inbox`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 24,576 bytes (Table: 0 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `environment` | `text` | `NO` | - | - |
| 2 | `event_id` | `text` | `NO` | - | - |
| 3 | `payload` | `jsonb` | `NO` | - | - |
| 4 | `received_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 5 | `processed_at` | `timestamp with time zone` | `YES` | - | - |
| 6 | `last_error` | `text` | `YES` | - | - |
| 7 | `attempts` | `integer` | `NO` | `0` | - |
| 8 | `next_attempt_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 9 | `leased_until` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.blog_authors`
- **Type**: `TABLE` | **Estimated Rows**: 1 | **RLS**: `ENABLED`
- **Total Bytes**: 81,920 bytes (Table: 8,192 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `name` | `text` | `NO` | - | - |
| 3 | `image_url` | `text` | `YES` | - | - |
| 4 | `bio` | `text` | `YES` | - | - |
| 5 | `sort_order` | `integer` | `NO` | `0` | - |
| 6 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.blog_categories`
- **Type**: `TABLE` | **Estimated Rows**: 4 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 8,192 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `name` | `text` | `NO` | - | - |
| 3 | `slug` | `text` | `NO` | - | - |
| 4 | `description` | `text` | `YES` | - | - |
| 5 | `sort_order` | `integer` | `NO` | `0` | - |
| 6 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.blog_posts`
- **Type**: `TABLE` | **Estimated Rows**: 15 | **RLS**: `ENABLED`
- **Total Bytes**: 319,488 bytes (Table: 16,384 bytes, Indexes: 81,920 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `category_id` | `uuid` | `YES` | - | - |
| 3 | `title` | `text` | `NO` | - | - |
| 4 | `slug` | `text` | `NO` | - | - |
| 5 | `excerpt` | `text` | `YES` | - | - |
| 6 | `body` | `text` | `NO` | `''::text` | - |
| 7 | `cover_image_url` | `text` | `YES` | - | - |
| 11 | `is_featured` | `boolean` | `NO` | `false` | - |
| 12 | `published` | `boolean` | `NO` | `false` | - |
| 13 | `published_at` | `timestamp with time zone` | `YES` | - | - |
| 14 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 15 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 16 | `author_id` | `uuid` | `NO` | - | - |
| 17 | `cover_image_square_url` | `text` | `YES` | - | - |

---

## Table: `public.campaign_run_audience`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 32,768 bytes (Table: 0 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `campaign_run_id` | `uuid` | `NO` | - | - |
| 2 | `contact_id` | `uuid` | `NO` | - | - |
| 3 | `organization_id` | `uuid` | `NO` | - | - |

---

## Table: `public.campaign_runs`
- **Type**: `TABLE` | **Estimated Rows**: 33 | **RLS**: `ENABLED`
- **Total Bytes**: 106,496 bytes (Table: 8,192 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `campaign_id` | `uuid` | `NO` | - | - |
| 3 | `user_id` | `uuid` | `NO` | - | - |
| 4 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 5 | `organization_id` | `uuid` | `NO` | - | - |
| 6 | `native_template_version_id` | `uuid` | `YES` | - | - |

---

## Table: `public.campaign_sending_holds`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 16,384 bytes (Table: 0 bytes, Indexes: 8,192 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `campaign_id` | `uuid` | `NO` | - | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `reason` | `text` | `NO` | - | - |
| 4 | `reviewed_at` | `timestamp with time zone` | `YES` | - | - |
| 5 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.campaigns`
- **Type**: `TABLE` | **Estimated Rows**: 43 | **RLS**: `ENABLED`
- **Total Bytes**: 385,024 bytes (Table: 122,880 bytes, Indexes: 114,688 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `title` | `text` | `NO` | - | - |
| 4 | `description` | `text` | `YES` | - | - |
| 5 | `segment_id` | `uuid` | `YES` | - | - |
| 6 | `template_id` | `uuid` | `YES` | - | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 9 | `schedule_type` | `text` | `NO` | `'manual'::text` | manual | scheduled_once | recurring | recurring_new_contacts |
| 10 | `scheduled_at` | `timestamp with time zone` | `YES` | - | One-time automated send at this time (UTC stored) |
| 11 | `recurrence_interval` | `integer` | `YES` | - | Every N units for recurring types |
| 12 | `recurrence_unit` | `text` | `YES` | - | day | week | month for recurring types |
| 13 | `next_automated_run_at` | `timestamp with time zone` | `YES` | - | Next time recurring campaigns run; also mirrors scheduled_once target until dispatched. |
| 14 | `automation_pg_cron_job_name` | `text` | `YES` | - | pg_cron job name for scheduled_once; cleared after dispatch. |
| 15 | `from_email` | `text` | `YES` | - | Default From for campaign sends when platform relay is enabled; must match a verified sending domain. |
| 16 | `billing_locked` | `boolean` | `NO` | `false` | - |
| 17 | `organization_id` | `uuid` | `NO` | - | - |
| 18 | `topic_id` | `uuid` | `YES` | - | - |
| 19 | `subject` | `text` | `YES` | - | - |
| 20 | `body_html` | `text` | `YES` | - | - |
| 21 | `body_json` | `jsonb` | `YES` | - | - |
| 22 | `preview_text` | `text` | `YES` | - | - |
| 23 | `status` | `text` | `NO` | `'draft'::text` | - |
| 24 | `native_issue_key` | `text` | `YES` | - | - |

---

## Table: `public.contact_properties`
- **Type**: `TABLE` | **Estimated Rows**: 102 | **RLS**: `ENABLED`
- **Total Bytes**: 352,256 bytes (Table: 172,032 bytes, Indexes: 139,264 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `name` | `text` | `NO` | - | - |
| 4 | `type` | `text` | `NO` | - | - |
| 5 | `fallback_value` | `text` | `YES` | - | - |
| 6 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `key` | `text` | `NO` | - | - |

---

## Table: `public.contact_property_values`
- **Type**: `TABLE` | **Estimated Rows**: 123 | **RLS**: `ENABLED`
- **Total Bytes**: 131,072 bytes (Table: 24,576 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `contact_id` | `uuid` | `NO` | - | - |
| 4 | `property_id` | `uuid` | `NO` | - | - |
| 5 | `value` | `text` | `YES` | - | - |
| 6 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.contact_segments`
- **Type**: `TABLE` | **Estimated Rows**: 32 | **RLS**: `ENABLED`
- **Total Bytes**: 114,688 bytes (Table: 8,192 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `name` | `text` | `NO` | - | - |
| 4 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 5 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 6 | `organization_id` | `uuid` | `NO` | - | - |
| 7 | `managed_topic_id` | `uuid` | `YES` | - | - |

---

## Table: `public.contact_subscription_challenges`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 73,728 bytes (Table: 0 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `subscription_id` | `uuid` | `NO` | - | - |
| 3 | `token_hash` | `text` | `NO` | - | - |
| 4 | `token_ciphertext` | `text` | `YES` | - | - |
| 5 | `expires_at` | `timestamp with time zone` | `NO` | - | - |
| 6 | `consumed_at` | `timestamp with time zone` | `YES` | - | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `notification_status` | `text` | `NO` | `'pending'::text` | - |
| 9 | `email_id` | `uuid` | `YES` | - | - |
| 10 | `attempts` | `integer` | `NO` | `0` | - |
| 11 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 12 | `error` | `text` | `YES` | - | - |

---

## Table: `public.contact_subscription_events`
- **Type**: `TABLE` | **Estimated Rows**: 8 | **RLS**: `ENABLED`
- **Total Bytes**: 81,920 bytes (Table: 8,192 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `contact_id` | `uuid` | `NO` | - | - |
| 4 | `topic_id` | `uuid` | `NO` | - | - |
| 5 | `event` | `text` | `NO` | - | - |
| 6 | `source` | `text` | `NO` | - | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.contact_topics`
- **Type**: `TABLE` | **Estimated Rows**: 9 | **RLS**: `ENABLED`
- **Total Bytes**: 147,456 bytes (Table: 8,192 bytes, Indexes: 98,304 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `contact_id` | `uuid` | `NO` | - | - |
| 4 | `topic_id` | `uuid` | `NO` | - | - |
| 5 | `status` | `text` | `NO` | `'subscribed'::text` | - |
| 6 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `subscription` | `text` | `NO` | `'opt_in'::text` | - |
| 8 | `consent_state` | `text` | `YES` | - | - |
| 9 | `consent_version` | `text` | `YES` | - | - |
| 10 | `consent_source` | `text` | `YES` | - | - |
| 11 | `requested_at` | `timestamp with time zone` | `YES` | - | - |
| 12 | `confirmed_at` | `timestamp with time zone` | `YES` | - | - |
| 13 | `unsubscribed_at` | `timestamp with time zone` | `YES` | - | - |
| 14 | `request_window` | `timestamp with time zone` | `YES` | - | - |
| 15 | `request_count` | `integer` | `NO` | `0` | - |
| 16 | `legacy_subscriber_id` | `uuid` | `YES` | - | - |

---

## Table: `public.contacts`
- **Type**: `TABLE` | **Estimated Rows**: 1,224 | **RLS**: `ENABLED`
- **Total Bytes**: 4,587,520 bytes (Table: 1,769,472 bytes, Indexes: 2,752,512 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `email` | `text` | `NO` | - | - |
| 4 | `name` | `text` | `YES` | - | - |
| 5 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 10 | `status` | `text` | `NO` | `'subscribed'::text` | - |
| 11 | `organization_id` | `uuid` | `NO` | - | - |
| 12 | `email_validation_status` | `text` | `YES` | - | MailProbe deliverability verdict: deliverable | risky | undeliverable | unknown |
| 13 | `email_validation_score` | `smallint` | `YES` | - | Deliverability score 0-100 (MailProbe) |
| 14 | `email_validation_checked_at` | `timestamp with time zone` | `YES` | - | Timestamp of most recent MailProbe validation run |
| 15 | `email_validation_details` | `jsonb` | `YES` | - | Raw MailProbe payload: confidence, reason, is_catchall, is_disposable, is_role_account, provider |
| 16 | `properties` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 17 | `unsubscribed` | `boolean` | `NO` | `false` | - |

---

## Table: `public.email_send_confirmations`
- **Type**: `TABLE` | **Estimated Rows**: 1 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 8,192 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `token_hash` | `text` | `NO` | - | - |
| 3 | `organization_id` | `uuid` | `NO` | - | - |
| 4 | `user_id` | `uuid` | `NO` | - | - |
| 5 | `payload_hash` | `text` | `NO` | - | - |
| 6 | `payload` | `jsonb` | `NO` | - | - |
| 7 | `expires_at` | `timestamp with time zone` | `NO` | - | - |
| 8 | `used_at` | `timestamp with time zone` | `YES` | - | - |
| 9 | `created_at` | `timestamp with time zone` | `NO` | `timezone('utc'::text, now())` | - |

---

## Table: `public.email_usage_operations`
- **Type**: `TABLE` | **Estimated Rows**: -1 | **RLS**: `ENABLED`
- **Total Bytes**: 49,152 bytes (Table: 0 bytes, Indexes: 40,960 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `period_id` | `uuid` | `NO` | - | - |
| 4 | `source` | `text` | `NO` | - | - |
| 5 | `operation_key` | `text` | `NO` | - | - |
| 6 | `recipients` | `jsonb` | `NO` | - | - |
| 7 | `units` | `integer` | `NO` | - | - |
| 8 | `credit_units` | `integer` | `NO` | `0` | - |
| 9 | `state` | `text` | `NO` | `'reserved'::text` | - |
| 10 | `provider_message_id` | `text` | `YES` | - | - |
| 11 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 12 | `reserved_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 13 | `attempt_count` | `integer` | `NO` | `1` | - |
| 14 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.emails`
- **Type**: `TABLE` | **Estimated Rows**: 379 | **RLS**: `ENABLED`
- **Total Bytes**: 15,056,896 bytes (Table: 5,136,384 bytes, Indexes: 4,653,056 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `campaign_id` | `uuid` | `YES` | - | - |
| 4 | `account_id` | `uuid` | `YES` | - | Sending account used for this message; NULL if the account was removed. |
| 5 | `contact_id` | `uuid` | `YES` | - | - |
| 6 | `to_email` | `text` | `NO` | - | - |
| 7 | `subject` | `text` | `NO` | - | - |
| 8 | `body_html` | `text` | `NO` | - | - |
| 9 | `status` | `USER-DEFINED` | `NO` | `'pending'::email_status` | - |
| 10 | `scheduled_for` | `date` | `NO` | `CURRENT_DATE` | - |
| 11 | `sent_at` | `timestamp with time zone` | `YES` | - | - |
| 12 | `error` | `text` | `YES` | - | - |
| 13 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 14 | `campaign_run_id` | `uuid` | `YES` | - | - |
| 15 | `from_email` | `text` | `YES` | - | RFC5322 From address used for this message (header); envelope may use platform relay. |
| 16 | `smtp_message_id` | `text` | `YES` | - | Message-ID from the outbound SMTP server (if returned), for correlating with provider logs. |
| 17 | `organization_id` | `uuid` | `NO` | - | - |
| 18 | `kind` | `USER-DEFINED` | `NO` | `'transactional'::email_kind` | transactional = one-off (API/SDK/compose/SMTP); campaign = campaign sends |
| 19 | `source` | `USER-DEFINED` | `YES` | - | Origin of the send: api, sdk, compose, smtp, campaign, campaign_api, campaign_automation, onboarding |
| 20 | `smtp_credential_id` | `uuid` | `YES` | - | SMTP credential that authenticated the inbound submission (source = smtp); null for other origins. |
| 21 | `scheduled_at` | `timestamp with time zone` | `YES` | - | When status is pending: null means due immediately; timestamptz is the earliest send time. |
| 22 | `send_payload` | `jsonb` | `NO` | `'{}'::jsonb` | Queued send extras (cc, bcc, reply_to, headers, text, tags, attachments) for the per-user worker. |
| 23 | `tags` | `jsonb` | `NO` | `'[]'::jsonb` | Resend-style tags array: [{ "name": "...", "value": "..." }] |
| 24 | `bounced_at` | `timestamp with time zone` | `YES` | - | - |
| 25 | `complained_at` | `timestamp with time zone` | `YES` | - | - |
| 26 | `delivered_at` | `timestamp with time zone` | `YES` | - | - |
| 27 | `delayed_at` | `timestamp with time zone` | `YES` | - | - |
| 28 | `failed_at` | `timestamp with time zone` | `YES` | - | - |
| 29 | `opened_at` | `timestamp with time zone` | `YES` | - | - |
| 30 | `clicked_at` | `timestamp with time zone` | `YES` | - | - |
| 31 | `claimed_at` | `timestamp with time zone` | `YES` | - | - |
| 32 | `delivery_attempts` | `integer` | `NO` | `0` | - |
| 33 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 34 | `suppressed_at` | `timestamp with time zone` | `YES` | - | - |
| 35 | `api_key_id` | `uuid` | `YES` | - | - |
| 36 | `native_delivery_claimed_at` | `timestamp with time zone` | `YES` | - | - |
| 37 | `delivery_uncertain` | `boolean` | `NO` | `false` | - |
| 38 | `bounce_category` | `text` | `YES` | - | - |
| 39 | `idempotency_key` | `text` | `YES` | - | Stable caller-provided key for idempotent email enqueue operations. |

---

## Table: `public.global_suppression_list`
- **Type**: `TABLE` | **Estimated Rows**: 14 | **RLS**: `ENABLED`
- **Total Bytes**: 114,688 bytes (Table: 8,192 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `email` | `text` | `NO` | - | - |
| 3 | `reason` | `text` | `NO` | - | - |
| 4 | `source` | `text` | `NO` | `'ses_webhook'::text` | - |
| 5 | `metadata` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 6 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.help_ai_queries`
- **Type**: `TABLE` | **Estimated Rows**: 11 | **RLS**: `ENABLED`
- **Total Bytes**: 122,880 bytes (Table: 16,384 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `YES` | - | - |
| 3 | `organization_id` | `uuid` | `YES` | - | - |
| 4 | `query` | `text` | `NO` | - | - |
| 5 | `model_used` | `text` | `YES` | - | - |
| 6 | `metadata` | `jsonb` | `YES` | `'{}'::jsonb` | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.identities`
- **Type**: `TABLE` | **Estimated Rows**: 39 | **RLS**: `ENABLED`
- **Total Bytes**: 172,032 bytes (Table: 32,768 bytes, Indexes: 98,304 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `YES` | - | - |
| 3 | `provider_type` | `USER-DEFINED` | `NO` | - | - |
| 4 | `name` | `text` | `NO` | - | - |
| 5 | `smtp_host` | `text` | `YES` | - | - |
| 6 | `smtp_port` | `smallint` | `YES` | - | - |
| 7 | `smtp_username` | `text` | `YES` | - | - |
| 8 | `smtp_password` | `text` | `YES` | - | - |
| 9 | `google_access_token` | `text` | `YES` | - | - |
| 10 | `google_refresh_token` | `text` | `YES` | - | - |
| 11 | `google_email` | `text` | `YES` | - | - |
| 12 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 13 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 14 | `daily_mail_limit` | `integer` | `NO` | `500` | - |
| 15 | `daily_mail_used` | `integer` | `NO` | `0` | - |
| 16 | `daily_mail_used_date` | `date` | `YES` | - | - |
| 17 | `google_expires_at` | `timestamp with time zone` | `YES` | - | - |
| 18 | `google_scope` | `text` | `YES` | - | - |
| 19 | `google_token_type` | `text` | `YES` | - | - |
| 20 | `account_key` | `text` | `NO` | `('acc_'::text || replace((gen_` | Stable public identifier: acc_ prefix plus32 hex characters; unique per row. |
| 21 | `provisioned_by` | `USER-DEFINED` | `NO` | `'user'::account_provisioned_by` | user = normal connected account; admin = platform inventory (relay rows have user_id null). |
| 23 | `custom_from_email` | `text` | `YES` | - | For provider_type domain_relay: verified header From address at user sending domain (delivered via Amazon SES). |
| 26 | `custom_from_display_name` | `text` | `YES` | - | Optional display name for MIME From on domain_relay accounts (e.g. "Acme Newsletter"). |
| 27 | `billing_locked` | `boolean` | `NO` | `false` | - |
| 28 | `organization_id` | `uuid` | `NO` | - | - |
| 29 | `is_active` | `boolean` | `NO` | `true` | - |
| 30 | `identity_email` | `text` | `YES` | - | - |

---

## Table: `public.mailbox_aliases`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 40,960 bytes (Table: 0 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `mailbox_id` | `uuid` | `NO` | - | - |
| 4 | `alias_email` | `text` | `NO` | - | - |
| 5 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.mailbox_queue_events`
- **Type**: `TABLE` | **Estimated Rows**: -1 | **RLS**: `ENABLED`
- **Total Bytes**: 16,384 bytes (Table: 0 bytes, Indexes: 8,192 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `queue_key` | `text` | `NO` | - | - |
| 2 | `event_id` | `text` | `NO` | - | - |
| 3 | `event_type` | `text` | `NO` | - | - |
| 4 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.mailboxes`
- **Type**: `TABLE` | **Estimated Rows**: 8 | **RLS**: `ENABLED`
- **Total Bytes**: 131,072 bytes (Table: 8,192 bytes, Indexes: 81,920 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `created_by` | `uuid` | `NO` | - | - |
| 4 | `domain_id` | `uuid` | `NO` | - | - |
| 5 | `email` | `text` | `NO` | - | - |
| 6 | `local_part` | `text` | `NO` | - | - |
| 7 | `domain` | `text` | `NO` | - | - |
| 8 | `display_name` | `text` | `NO` | - | - |
| 9 | `password_hash` | `text` | `NO` | - | - |
| 10 | `storage_quota_bytes` | `bigint` | `NO` | `'5368709120'::bigint` | - |
| 11 | `storage_used_bytes` | `bigint` | `NO` | `0` | - |
| 12 | `is_active` | `boolean` | `NO` | `true` | - |
| 13 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 14 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 15 | `provisioning_state` | `text` | `NO` | `'active'::text` | - |
| 16 | `stalwart_account_id` | `text` | `YES` | - | - |
| 17 | `storage_synced_at` | `timestamp with time zone` | `YES` | - | - |
| 18 | `storage_sync_attempted_at` | `timestamp with time zone` | `YES` | - | - |
| 19 | `storage_sync_error` | `text` | `YES` | - | - |

---

## Table: `public.mailofly_user_mail_queue_cron`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 57,344 bytes (Table: 0 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `user_id` | `uuid` | `NO` | - | - |
| 2 | `cron_job_name` | `text` | `NO` | - | - |

---

## Table: `public.managed_audience_programs`
- **Type**: `TABLE` | **Estimated Rows**: 1 | **RLS**: `ENABLED`
- **Total Bytes**: 65,536 bytes (Table: 8,192 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `name` | `text` | `NO` | - | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `user_id` | `uuid` | `NO` | - | - |
| 4 | `topic_id` | `uuid` | `NO` | - | - |
| 5 | `segment_id` | `uuid` | `NO` | - | - |
| 6 | `legacy_bridge_enabled` | `boolean` | `NO` | `true` | - |

---

## Table: `public.native_template_versions`
- **Type**: `TABLE` | **Estimated Rows**: 67 | **RLS**: `ENABLED`
- **Total Bytes**: 360,448 bytes (Table: 131,072 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `template_id` | `uuid` | `NO` | - | - |
| 3 | `organization_id` | `uuid` | `NO` | - | - |
| 4 | `revision` | `bigint` | `NO` | - | - |
| 5 | `source_format` | `text` | `NO` | - | - |
| 6 | `snapshot` | `jsonb` | `NO` | - | - |
| 7 | `html` | `text` | `NO` | - | - |
| 8 | `plain_text` | `text` | `NO` | - | - |
| 9 | `compiler_version` | `text` | `NO` | - | - |
| 10 | `content_hash` | `text` | `NO` | - | - |
| 11 | `created_by` | `uuid` | `YES` | - | - |
| 12 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.newsletter_signup_windows`
- **Type**: `TABLE` | **Estimated Rows**: 1 | **RLS**: `ENABLED`
- **Total Bytes**: 65,536 bytes (Table: 8,192 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `ip_hash` | `text` | `NO` | - | - |
| 2 | `window_start` | `timestamp with time zone` | `NO` | `now()` | - |
| 3 | `attempts` | `integer` | `NO` | `1` | - |

---

## Table: `public.newsletter_subscribers`
- **Type**: `TABLE` | **Estimated Rows**: 8 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 8,192 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `email` | `text` | `NO` | - | - |
| 3 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 4 | `status` | `text` | `NO` | `'pending'::text` | - |
| 5 | `confirmation_hash` | `text` | `YES` | - | - |
| 6 | `confirmation_expires_at` | `timestamp with time zone` | `YES` | - | - |
| 7 | `confirmation_requested_at` | `timestamp with time zone` | `YES` | - | - |
| 8 | `confirmed_at` | `timestamp with time zone` | `YES` | - | - |
| 9 | `unsubscribed_at` | `timestamp with time zone` | `YES` | - | - |
| 10 | `consent_version` | `text` | `YES` | - | - |
| 11 | `request_window` | `timestamp with time zone` | `YES` | - | - |
| 12 | `request_count` | `integer` | `NO` | `0` | - |

---

## Table: `public.oauth_access_tokens`
- **Type**: `TABLE` | **Estimated Rows**: 29 | **RLS**: `ENABLED`
- **Total Bytes**: 122,880 bytes (Table: 16,384 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `token_hash` | `text` | `NO` | - | - |
| 3 | `client_id` | `text` | `NO` | - | - |
| 4 | `user_id` | `uuid` | `NO` | - | - |
| 5 | `organization_id` | `uuid` | `NO` | - | - |
| 6 | `scopes` | `ARRAY` | `NO` | `'{}'::text[]` | - |
| 7 | `expires_at` | `timestamp with time zone` | `NO` | - | - |
| 8 | `revoked_at` | `timestamp with time zone` | `YES` | - | - |
| 9 | `last_used_at` | `timestamp with time zone` | `YES` | - | - |
| 10 | `created_at` | `timestamp with time zone` | `NO` | `timezone('utc'::text, now())` | - |

---

## Table: `public.oauth_authorization_codes`
- **Type**: `TABLE` | **Estimated Rows**: 13 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 8,192 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `code_hash` | `text` | `NO` | - | - |
| 3 | `client_id` | `text` | `NO` | - | - |
| 4 | `user_id` | `uuid` | `NO` | - | - |
| 5 | `organization_id` | `uuid` | `NO` | - | - |
| 6 | `scopes` | `ARRAY` | `NO` | `'{}'::text[]` | - |
| 7 | `redirect_uri` | `text` | `NO` | - | - |
| 8 | `code_challenge` | `text` | `NO` | - | - |
| 9 | `code_challenge_method` | `text` | `NO` | `'S256'::text` | - |
| 10 | `expires_at` | `timestamp with time zone` | `NO` | - | - |
| 11 | `used_at` | `timestamp with time zone` | `YES` | - | - |
| 12 | `created_at` | `timestamp with time zone` | `NO` | `timezone('utc'::text, now())` | - |

---

## Table: `public.oauth_authorization_requests`
- **Type**: `TABLE` | **Estimated Rows**: 13 | **RLS**: `ENABLED`
- **Total Bytes**: 81,920 bytes (Table: 8,192 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `client_id` | `text` | `NO` | - | - |
| 3 | `redirect_uri` | `text` | `NO` | - | - |
| 4 | `response_type` | `text` | `NO` | `'code'::text` | - |
| 5 | `scope` | `text` | `NO` | - | - |
| 6 | `state` | `text` | `YES` | - | - |
| 7 | `code_challenge` | `text` | `NO` | - | - |
| 8 | `code_challenge_method` | `text` | `NO` | `'S256'::text` | - |
| 9 | `user_id` | `uuid` | `YES` | - | - |
| 10 | `organization_id` | `uuid` | `YES` | - | - |
| 11 | `status` | `text` | `NO` | `'pending'::text` | - |
| 12 | `code` | `text` | `YES` | - | - |
| 13 | `expires_at` | `timestamp with time zone` | `NO` | - | - |
| 14 | `created_at` | `timestamp with time zone` | `NO` | `timezone('utc'::text, now())` | - |

---

## Table: `public.oauth_clients`
- **Type**: `TABLE` | **Estimated Rows**: 12 | **RLS**: `ENABLED`
- **Total Bytes**: 81,920 bytes (Table: 8,192 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `client_id` | `text` | `NO` | - | - |
| 3 | `client_secret_hash` | `text` | `YES` | - | - |
| 4 | `client_name` | `text` | `NO` | - | - |
| 5 | `redirect_uris` | `ARRAY` | `NO` | `'{}'::text[]` | - |
| 6 | `allowed_scopes` | `ARRAY` | `NO` | `'{domains:read,emails:read,tem` | - |
| 7 | `is_trusted` | `boolean` | `NO` | `false` | - |
| 8 | `created_at` | `timestamp with time zone` | `NO` | `timezone('utc'::text, now())` | - |
| 9 | `updated_at` | `timestamp with time zone` | `NO` | `timezone('utc'::text, now())` | - |
| 10 | `token_endpoint_auth_method` | `text` | `NO` | `'none'::text` | - |
| 11 | `grant_types` | `ARRAY` | `NO` | `ARRAY['authorization_code'::te` | - |
| 12 | `response_types` | `ARRAY` | `NO` | `ARRAY['code'::text]` | - |
| 13 | `client_uri` | `text` | `YES` | - | - |
| 14 | `logo_uri` | `text` | `YES` | - | - |
| 15 | `organization_id` | `uuid` | `YES` | - | - |
| 16 | `user_id` | `uuid` | `YES` | - | - |

---

## Table: `public.oauth_refresh_tokens`
- **Type**: `TABLE` | **Estimated Rows**: 26 | **RLS**: `ENABLED`
- **Total Bytes**: 106,496 bytes (Table: 16,384 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `token_hash` | `text` | `NO` | - | - |
| 3 | `access_token_id` | `uuid` | `YES` | - | - |
| 4 | `client_id` | `text` | `NO` | - | - |
| 5 | `user_id` | `uuid` | `NO` | - | - |
| 6 | `organization_id` | `uuid` | `NO` | - | - |
| 7 | `scopes` | `ARRAY` | `NO` | `'{}'::text[]` | - |
| 8 | `expires_at` | `timestamp with time zone` | `NO` | - | - |
| 9 | `revoked_at` | `timestamp with time zone` | `YES` | - | - |
| 10 | `created_at` | `timestamp with time zone` | `NO` | `timezone('utc'::text, now())` | - |
| 11 | `grant_id` | `uuid` | `YES` | `gen_random_uuid()` | - |

---

## Table: `public.organization_addon_subscriptions`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 24,576 bytes (Table: 0 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `addon_slug` | `text` | `NO` | - | - |
| 4 | `dodo_addon_id` | `text` | `NO` | - | - |
| 5 | `quantity` | `integer` | `NO` | `1` | - |
| 6 | `status` | `text` | `NO` | `'active'::text` | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.organization_addons`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 57,344 bytes (Table: 0 bytes, Indexes: 40,960 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 3 | `addon_id` | `uuid` | `NO` | - | - |
| 4 | `units_remaining` | `integer` | `NO` | `0` | - |
| 5 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 6 | `organization_id` | `uuid` | `NO` | - | - |

---

## Table: `public.organization_billing_notification_policy`
- **Type**: `TABLE` | **Estimated Rows**: 1 | **RLS**: `ENABLED`
- **Total Bytes**: 57,344 bytes (Table: 8,192 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `boolean` | `NO` | `true` | - |
| 2 | `enabled` | `boolean` | `NO` | `false` | - |
| 3 | `scan_after` | `uuid` | `YES` | - | - |

---

## Table: `public.organization_billing_notifications`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 32,768 bytes (Table: 0 bytes, Indexes: 24,576 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `event_key` | `text` | `NO` | - | - |
| 3 | `organization_id` | `uuid` | `NO` | - | - |
| 4 | `user_id` | `uuid` | `NO` | - | - |
| 5 | `kind` | `text` | `NO` | - | - |
| 6 | `headline` | `text` | `NO` | - | - |
| 7 | `details` | `text` | `NO` | - | - |
| 8 | `next_steps` | `text` | `NO` | - | - |
| 9 | `usage_metric` | `text` | `YES` | - | - |
| 10 | `usage_cap` | `bigint` | `YES` | - | - |
| 11 | `usage_threshold` | `integer` | `YES` | - | - |
| 12 | `usage_period` | `text` | `YES` | - | - |
| 13 | `payment_environment` | `text` | `YES` | - | - |
| 14 | `payment_id` | `text` | `YES` | - | - |
| 15 | `payment_status` | `text` | `YES` | - | - |
| 16 | `expires_at` | `timestamp with time zone` | `NO` | `(now() + '7 days'::interval)` | - |
| 17 | `available_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 18 | `attempts` | `integer` | `NO` | `0` | - |
| 19 | `completed_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.organization_billing_plan_state`
- **Type**: `TABLE` | **Estimated Rows**: 560 | **RLS**: `ENABLED`
- **Total Bytes**: 147,456 bytes (Table: 49,152 bytes, Indexes: 57,344 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `organization_id` | `uuid` | `NO` | - | - |
| 2 | `product_type` | `text` | `NO` | - | - |
| 3 | `plan_id` | `uuid` | `NO` | - | - |

---

## Table: `public.organization_credit_transactions`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 57,344 bytes (Table: 0 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `amount_cents` | `integer` | `NO` | - | - |
| 4 | `balance_after_cents` | `integer` | `NO` | - | - |
| 5 | `type` | `text` | `NO` | - | - |
| 6 | `description` | `text` | `YES` | - | - |
| 7 | `payment_id` | `text` | `YES` | - | - |
| 8 | `metadata` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 9 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.organization_email_days`
- **Type**: `TABLE` | **Estimated Rows**: -1 | **RLS**: `ENABLED`
- **Total Bytes**: 8,192 bytes (Table: 0 bytes, Indexes: 8,192 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `organization_id` | `uuid` | `NO` | - | - |
| 2 | `day` | `date` | `NO` | - | - |
| 3 | `used_units` | `bigint` | `NO` | `0` | - |

---

## Table: `public.organization_email_periods`
- **Type**: `TABLE` | **Estimated Rows**: -1 | **RLS**: `ENABLED`
- **Total Bytes**: 16,384 bytes (Table: 0 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `period_start` | `timestamp with time zone` | `NO` | - | - |
| 4 | `period_end` | `timestamp with time zone` | `NO` | - | - |
| 5 | `allowance_units` | `integer` | `NO` | - | - |
| 6 | `opening_credit_units` | `bigint` | `NO` | `0` | - |
| 7 | `opening_units` | `bigint` | `NO` | `0` | - |
| 8 | `committed_units` | `bigint` | `NO` | `0` | - |
| 9 | `committed_credit_units` | `bigint` | `NO` | `0` | - |
| 10 | `reserved_units` | `bigint` | `NO` | `0` | - |

---

## Table: `public.organization_email_policy`
- **Type**: `TABLE` | **Estimated Rows**: -1 | **RLS**: `ENABLED`
- **Total Bytes**: 16,384 bytes (Table: 0 bytes, Indexes: 8,192 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `organization_id` | `uuid` | `NO` | - | - |
| 2 | `mode` | `text` | `NO` | `'legacy'::text` | - |
| 3 | `outbound_ready` | `boolean` | `NO` | `false` | - |
| 4 | `mailbox_ready` | `boolean` | `NO` | `false` | - |
| 5 | `receiving_ready` | `boolean` | `NO` | `false` | - |
| 6 | `enabled_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.organization_invitations`
- **Type**: `TABLE` | **Estimated Rows**: 6 | **RLS**: `ENABLED`
- **Total Bytes**: 114,688 bytes (Table: 8,192 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `email` | `text` | `NO` | - | - |
| 4 | `role` | `USER-DEFINED` | `NO` | `'viewer'::organization_role` | Role granted on acceptance. Owners can invite co-owners; admins can invite admin/viewer only (enforced at app layer). |
| 5 | `token` | `text` | `NO` | `encode(extensions.gen_random_b` | - |
| 6 | `invited_by` | `uuid` | `NO` | - | - |
| 7 | `expires_at` | `timestamp with time zone` | `NO` | `(now() + '7 days'::interval)` | - |
| 8 | `accepted_at` | `timestamp with time zone` | `YES` | - | - |
| 9 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.organization_members`
- **Type**: `TABLE` | **Estimated Rows**: 283 | **RLS**: `ENABLED`
- **Total Bytes**: 196,608 bytes (Table: 32,768 bytes, Indexes: 131,072 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `user_id` | `uuid` | `NO` | - | - |
| 4 | `role` | `USER-DEFINED` | `NO` | `'viewer'::organization_role` | - |
| 5 | `joined_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.organization_payment_notice_state`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 40,960 bytes (Table: 8,192 bytes, Indexes: 24,576 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `environment` | `text` | `NO` | - | - |
| 2 | `payment_id` | `text` | `NO` | - | - |
| 3 | `organization_id` | `uuid` | `NO` | - | - |
| 4 | `status` | `text` | `NO` | - | - |
| 5 | `invoice_id` | `text` | `NO` | - | - |
| 6 | `amount_display` | `text` | `NO` | - | - |
| 7 | `observed_at` | `timestamp with time zone` | `NO` | - | - |
| 8 | `status_since` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.organization_sending_protection`
- **Type**: `TABLE` | **Estimated Rows**: 23 | **RLS**: `ENABLED`
- **Total Bytes**: 90,112 bytes (Table: 32,768 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `organization_id` | `uuid` | `NO` | - | - |
| 2 | `state` | `text` | `NO` | `'normal'::text` | - |
| 3 | `reason` | `text` | `YES` | - | - |
| 4 | `metrics` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 5 | `reviewed_at` | `timestamp with time zone` | `YES` | - | - |
| 6 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `reason_code` | `text` | `YES` | - | - |
| 8 | `notification_revision` | `uuid` | `NO` | `gen_random_uuid()` | - |

---

## Table: `public.organization_subscriptions`
- **Type**: `TABLE` | **Estimated Rows**: 284 | **RLS**: `ENABLED`
- **Total Bytes**: 147,456 bytes (Table: 40,960 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2 | `plan_id` | `uuid` | `NO` | - | - |
| 3 | `status` | `USER-DEFINED` | `NO` | `'active'::subscription_status` | - |
| 6 | `current_period_start` | `timestamp with time zone` | `YES` | - | - |
| 7 | `current_period_end` | `timestamp with time zone` | `YES` | - | - |
| 8 | `cancel_at_period_end` | `boolean` | `NO` | `false` | - |
| 9 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 10 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 11 | `organization_id` | `uuid` | `NO` | - | - |
| 12 | `payment_provider` | `text` | `YES` | `'dodopayments'::text` | Active gateway for this subscription row: dodopayments or razorpay. |
| 13 | `dodo_subscription_id` | `text` | `YES` | - | - |
| 14 | `dodo_customer_id` | `text` | `YES` | - | - |
| 15 | `credit_balance_cents` | `integer` | `NO` | `0` | - |
| 16 | `marketing_plan_id` | `uuid` | `YES` | - | - |
| 17 | `dodo_marketing_subscription_id` | `text` | `YES` | - | - |
| 18 | `marketing_status` | `USER-DEFINED` | `YES` | `'active'::subscription_status` | - |
| 19 | `ai_credits_used_in_period` | `integer` | `YES` | `0` | - |
| 20 | `automation_runs_in_period` | `integer` | `YES` | `0` | - |

---

## Table: `public.organization_usage`
- **Type**: `TABLE` | **Estimated Rows**: 282 | **RLS**: `ENABLED`
- **Total Bytes**: 73,728 bytes (Table: 24,576 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2 | `period_start` | `timestamp with time zone` | `NO` | - | - |
| 3 | `emails_sent_in_period` | `integer` | `NO` | `0` | - |
| 4 | `api_requests_in_period` | `integer` | `NO` | `0` | - |
| 5 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 6 | `organization_id` | `uuid` | `NO` | - | - |

---

## Table: `public.organizations`
- **Type**: `TABLE` | **Estimated Rows**: 258 | **RLS**: `ENABLED`
- **Total Bytes**: 147,456 bytes (Table: 40,960 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `name` | `text` | `NO` | - | - |
| 3 | `slug` | `text` | `NO` | - | - |
| 4 | `created_by` | `uuid` | `YES` | - | User who created the workspace. Nullable after that auth user is deleted. |
| 5 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 6 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `type` | `USER-DEFINED` | `NO` | `'business'::organization_type` | - |
| 8 | `credit_balance_cents` | `integer` | `NO` | `0` | - |
| 9 | `ses_configuration_set` | `text` | `YES` | - | Custom AWS SES Configuration Set name override for this organization (e.g. dedicated IP pool or enterprise config set). |
| 10 | `unsubscribe_page_config` | `jsonb` | `NO` | `'{}'::jsonb` | Custom branding, copy, styling, and controls configuration for the public unsubscribe and preference center page. |
| 11 | `is_locked` | `boolean` | `NO` | `false` | - |
| 12 | `locked_at` | `timestamp with time zone` | `YES` | - | - |
| 13 | `locked_reason` | `text` | `YES` | - | - |
| 14 | `auto_verify_contacts` | `boolean` | `NO` | `false` | When true, newly added or imported contacts are automatically queued for background deliverability verification |

---

## Table: `public.plans`
- **Type**: `TABLE` | **Estimated Rows**: 25 | **RLS**: `ENABLED`
- **Total Bytes**: 163,840 bytes (Table: 24,576 bytes, Indexes: 98,304 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `slug` | `text` | `NO` | - | - |
| 3 | `name` | `text` | `NO` | - | - |
| 4 | `tier` | `USER-DEFINED` | `NO` | `'free'::plan_tier` | - |
| 5 | `billing_interval` | `text` | `NO` | `'none'::text` | - |
| 7 | `description` | `text` | `YES` | - | - |
| 8 | `sort_order` | `integer` | `NO` | `0` | - |
| 9 | `is_active` | `boolean` | `NO` | `true` | - |
| 10 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 11 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 12 | `max_accounts` | `integer` | `NO` | `1` | Max connected sending accounts per user; -1 = unlimited. |
| 13 | `max_templates` | `integer` | `NO` | `1000` | Max email templates; -1 = unlimited. |
| 14 | `max_campaigns_per_month` | `integer` | `NO` | `'-1'::integer` | Max campaigns created per calendar month (UTC); -1 = unlimited. |
| 15 | `max_contacts` | `integer` | `NO` | `500` | Max contacts; -1 = unlimited. |
| 16 | `max_contact_segments` | `integer` | `NO` | `5` | Max segments (lists); -1 = unlimited. |
| 17 | `allow_automation` | `boolean` | `NO` | `false` | Scheduled and recurring campaign automation. |
| 18 | `allow_google_sheet_sync` | `boolean` | `NO` | `false` | Google Sheets segment sync. |
| 19 | `mail_log_retention_days` | `integer` | `YES` | - | Delete mail_logs older than this many days; NULL = no automatic pruning. |
| 20 | `max_stored_mail_logs` | `integer` | `NO` | `2000` | Max mail_logs rows per user; -1 = unlimited. |
| 21 | `price_monthly_cents` | `integer` | `YES` | - | - |
| 22 | `price_display_label` | `text` | `YES` | - | - |
| 23 | `currency` | `text` | `NO` | `'USD'::text` | - |
| 24 | `monthly_email_quota` | `integer` | `NO` | `1000` | - |
| 25 | `max_sending_domains` | `integer` | `NO` | `1` | - |
| 26 | `max_api_requests_per_month` | `integer` | `NO` | `'-1'::integer` | - |
| 27 | `allow_mail_warmups` | `boolean` | `NO` | `false` | - |
| 28 | `allow_mailofly_ai` | `boolean` | `NO` | `false` | - |
| 29 | `addons_enabled` | `boolean` | `NO` | `true` | - |
| 30 | `dodo_product_id` | `text` | `YES` | - | Dodo Payments subscription product id (pdt_...) for checkout sessions. |
| 31 | `dodo_product_id_test` | `text` | `YES` | - | Dodo Payments Test Mode (sandbox) subscription product id. |
| 32 | `dodo_product_id_live` | `text` | `YES` | - | Dodo Payments Live Mode (production) subscription product id. |
| 35 | `product_type` | `USER-DEFINED` | `NO` | `'transactional'::plan_product_` | - |
| 36 | `overage_price_per_thousand_cents` | `integer` | `YES` | `0` | - |
| 37 | `daily_email_limit` | `integer` | `YES` | `'-1'::integer` | - |
| 38 | `ai_credits_monthly` | `integer` | `YES` | `5` | - |
| 39 | `webhook_endpoints_limit` | `integer` | `YES` | `1` | - |
| 40 | `dodo_overage_meter_id_test` | `text` | `YES` | - | - |
| 41 | `dodo_overage_meter_id_live` | `text` | `YES` | - | - |
| 42 | `max_mailboxes` | `integer` | `NO` | `1` | - |

---

## Table: `public.platform_email_deliveries`
- **Type**: `TABLE` | **Estimated Rows**: 302 | **RLS**: `ENABLED`
- **Total Bytes**: 237,568 bytes (Table: 114,688 bytes, Indexes: 81,920 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `occurrence_key` | `text` | `NO` | - | - |
| 2 | `status` | `text` | `NO` | `'processing'::text` | - |
| 3 | `email_id` | `uuid` | `YES` | - | - |
| 4 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 5 | `error` | `text` | `YES` | - | - |
| 6 | `notification_name` | `text` | `YES` | - | - |
| 7 | `payload_ciphertext` | `text` | `YES` | - | - |
| 8 | `dispatch_id` | `text` | `YES` | - | - |
| 9 | `expires_at` | `timestamp with time zone` | `YES` | - | - |
| 10 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.platform_email_preferences`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 8,192 bytes (Table: 0 bytes, Indexes: 8,192 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `organization_id` | `uuid` | `NO` | - | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `weekly_report` | `boolean` | `NO` | `true` | - |
| 4 | `monthly_report` | `boolean` | `NO` | `true` | - |

---

## Table: `public.platform_notification_events`
- **Type**: `TABLE` | **Estimated Rows**: 13 | **RLS**: `ENABLED`
- **Total Bytes**: 106,496 bytes (Table: 16,384 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `occurrence_key` | `text` | `NO` | - | - |
| 3 | `kind` | `text` | `NO` | - | - |
| 4 | `user_id` | `uuid` | `NO` | - | - |
| 5 | `organization_id` | `uuid` | `NO` | - | - |
| 6 | `resource_id` | `uuid` | `NO` | - | - |
| 7 | `payload` | `jsonb` | `NO` | - | - |
| 8 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 9 | `available_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 10 | `attempts` | `integer` | `NO` | `0` | - |
| 11 | `completed_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.properties`
- **Type**: `VIEW` | **Estimated Rows**: -1 | **RLS**: `DISABLED`
- **Total Bytes**: 0 bytes (Table: 0 bytes, Indexes: 0 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `YES` | - | - |
| 2 | `organization_id` | `uuid` | `YES` | - | - |
| 3 | `name` | `text` | `YES` | - | - |
| 4 | `type` | `text` | `YES` | - | - |
| 5 | `fallback_value` | `text` | `YES` | - | - |
| 6 | `created_at` | `timestamp with time zone` | `YES` | - | - |
| 7 | `updated_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.queue_fallback_jobs`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 0 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `queue_name` | `text` | `NO` | - | - |
| 3 | `job_name` | `text` | `NO` | - | - |
| 4 | `payload` | `jsonb` | `NO` | - | - |
| 5 | `job_options` | `jsonb` | `YES` | `'{}'::jsonb` | - |
| 6 | `status` | `text` | `NO` | `'pending'::text` | - |
| 7 | `attempts` | `integer` | `NO` | `0` | - |
| 8 | `max_attempts` | `integer` | `NO` | `3` | - |
| 9 | `error` | `text` | `YES` | - | - |
| 10 | `scheduled_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 11 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 12 | `processed_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.received_emails`
- **Type**: `TABLE` | **Estimated Rows**: 4 | **RLS**: `ENABLED`
- **Total Bytes**: 163,840 bytes (Table: 8,192 bytes, Indexes: 114,688 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `user_id` | `uuid` | `NO` | - | - |
| 4 | `domain_id` | `uuid` | `YES` | - | - |
| 5 | `from_address` | `text` | `NO` | - | - |
| 6 | `from_name` | `text` | `YES` | - | - |
| 7 | `to_address` | `text` | `NO` | - | - |
| 8 | `to_recipients` | `jsonb` | `NO` | `'[]'::jsonb` | - |
| 9 | `cc_recipients` | `jsonb` | `NO` | `'[]'::jsonb` | - |
| 10 | `bcc_recipients` | `jsonb` | `NO` | `'[]'::jsonb` | - |
| 11 | `reply_to` | `jsonb` | `NO` | `'[]'::jsonb` | - |
| 12 | `subject` | `text` | `YES` | - | - |
| 13 | `text_body` | `text` | `YES` | - | - |
| 14 | `html_body` | `text` | `YES` | - | - |
| 15 | `headers` | `jsonb` | `YES` | - | - |
| 16 | `attachments` | `jsonb` | `NO` | `'[]'::jsonb` | - |
| 17 | `raw_eml_url` | `text` | `YES` | - | - |
| 18 | `message_id` | `text` | `YES` | - | - |
| 19 | `spam_verdict` | `text` | `YES` | - | - |
| 20 | `virus_verdict` | `text` | `YES` | - | - |
| 21 | `spf_verdict` | `text` | `YES` | - | - |
| 22 | `dkim_verdict` | `text` | `YES` | - | - |
| 23 | `dmarc_verdict` | `text` | `YES` | - | - |
| 24 | `status` | `text` | `NO` | `'received'::text` | - |
| 25 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 26 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 27 | `provider_receipt_id` | `text` | `YES` | - | - |
| 28 | `quota_pending` | `boolean` | `NO` | `false` | - |
| 29 | `quota_retry_at` | `timestamp with time zone` | `YES` | - | - |
| 30 | `attachment_count` | `integer` | `YES` | - | - |

---

## Table: `public.referral_earnings`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 0 bytes, Indexes: 73,728 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `referrer_user_id` | `uuid` | `NO` | - | - |
| 3 | `referred_user_id` | `uuid` | `NO` | - | - |
| 4 | `organization_id` | `uuid` | `YES` | - | - |
| 5 | `plan_id` | `uuid` | `YES` | - | - |
| 6 | `plan_name` | `text` | `NO` | - | - |
| 7 | `plan_base_price_cents` | `integer` | `NO` | `0` | - |
| 8 | `commission_percent` | `numeric` | `NO` | `10.00` | - |
| 9 | `earned_amount_cents` | `integer` | `NO` | `0` | - |
| 10 | `currency` | `text` | `NO` | `'usd'::text` | - |
| 11 | `dodo_subscription_id` | `text` | `YES` | - | - |
| 12 | `dodo_payment_id` | `text` | `YES` | - | - |
| 13 | `status` | `text` | `NO` | `'credited'::text` | - |
| 14 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.referral_payout_methods`
- **Type**: `TABLE` | **Estimated Rows**: 2 | **RLS**: `ENABLED`
- **Total Bytes**: 81,920 bytes (Table: 8,192 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `payout_type` | `text` | `NO` | `'bank_transfer'::text` | - |
| 4 | `account_holder_name` | `text` | `NO` | - | - |
| 5 | `bank_name` | `text` | `YES` | - | - |
| 6 | `account_number` | `text` | `NO` | - | - |
| 7 | `routing_number` | `text` | `YES` | - | - |
| 8 | `upi_id` | `text` | `YES` | - | - |
| 9 | `paypal_email` | `text` | `YES` | - | - |
| 10 | `currency` | `text` | `NO` | `'usd'::text` | - |
| 11 | `is_default` | `boolean` | `NO` | `true` | - |
| 12 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 13 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.referral_withdrawal_requests`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 32,768 bytes (Table: 0 bytes, Indexes: 24,576 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `amount_cents` | `integer` | `NO` | - | - |
| 4 | `currency` | `text` | `NO` | `'usd'::text` | - |
| 5 | `payout_method_id` | `uuid` | `YES` | - | - |
| 6 | `payout_details` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 7 | `status` | `text` | `NO` | `'pending'::text` | - |
| 8 | `admin_notes` | `text` | `YES` | - | - |
| 9 | `transaction_reference` | `text` | `YES` | - | - |
| 10 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 11 | `processed_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.roles`
- **Type**: `TABLE` | **Estimated Rows**: 2 | **RLS**: `ENABLED`
- **Total Bytes**: 57,344 bytes (Table: 8,192 bytes, Indexes: 16,384 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `name` | `USER-DEFINED` | `NO` | - | - |

---

## Table: `public.segment_contacts`
- **Type**: `TABLE` | **Estimated Rows**: 924 | **RLS**: `ENABLED`
- **Total Bytes**: 311,296 bytes (Table: 131,072 bytes, Indexes: 147,456 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `segment_id` | `uuid` | `NO` | - | - |
| 2 | `contact_id` | `uuid` | `NO` | - | - |
| 3 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.segment_google_sheets`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 65,536 bytes (Table: 0 bytes, Indexes: 40,960 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `segment_id` | `uuid` | `NO` | - | - |
| 5 | `spreadsheet_id` | `text` | `NO` | - | - |
| 6 | `sheet_name` | `text` | `NO` | - | - |
| 7 | `header_row` | `integer` | `NO` | `1` | - |
| 8 | `last_processed_row` | `integer` | `NO` | `1` | - |
| 9 | `channel_id` | `text` | `YES` | - | - |
| 10 | `resource_id` | `text` | `YES` | - | - |
| 11 | `channel_expiration` | `timestamp with time zone` | `YES` | - | - |
| 12 | `last_synced_at` | `timestamp with time zone` | `YES` | - | - |
| 13 | `last_sync_error` | `text` | `YES` | - | - |
| 14 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 15 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 16 | `organization_id` | `uuid` | `NO` | - | - |

---

## Table: `public.sending_domains`
- **Type**: `TABLE` | **Estimated Rows**: 60 | **RLS**: `ENABLED`
- **Total Bytes**: 475,136 bytes (Table: 131,072 bytes, Indexes: 98,304 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `domain` | `text` | `NO` | - | - |
| 4 | `dkim_selector` | `text` | `NO` | - | - |
| 5 | `dkim_private_key_pem` | `text` | `NO` | - | - |
| 6 | `dns_verification` | `jsonb` | `YES` | - | - |
| 7 | `dns_last_checked_at` | `timestamp with time zone` | `YES` | - | - |
| 8 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 9 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 10 | `ses_identity_status` | `text` | `YES` | - | SES GetEmailIdentity VerificationStatus snapshot (e.g. PENDING, SUCCESS). |
| 11 | `ses_dkim_cname_records` | `jsonb` | `YES` | - | Easy DKIM CNAME records [{name,value}] from SES. |
| 12 | `ses_mail_from_domain` | `text` | `YES` | - | Custom MAIL FROM subdomain, e.g. send.example.com. |
| 13 | `ses_mail_from_mx_target` | `text` | `YES` | - | - |
| 14 | `ses_mail_from_spf_txt` | `text` | `YES` | - | - |
| 15 | `ses_last_error` | `text` | `YES` | - | - |
| 16 | `billing_locked` | `boolean` | `NO` | `false` | - |
| 17 | `organization_id` | `uuid` | `NO` | - | - |
| 18 | `tracking_subdomain` | `text` | `YES` | `'links'::text` | - |
| 19 | `click_tracking` | `boolean` | `NO` | `false` | - |
| 20 | `open_tracking` | `boolean` | `NO` | `false` | - |
| 21 | `tls_mode` | `text` | `NO` | `'opportunistic'::text` | - |
| 22 | `enable_receiving` | `boolean` | `NO` | `false` | - |
| 23 | `receive_mode` | `text` | `NO` | `'catch_all'::text` | - |
| 24 | `enable_mailbox` | `boolean` | `NO` | `false` | - |
| 25 | `stalwart_dkim_selector` | `text` | `YES` | - | DKIM selector used for the Stalwart mailbox DKIM signature (e.g. "mailbox2a3b4c5d"). DNS record: <selector>._domainkey.<domain>. |
| 26 | `stalwart_dkim_private_key_pem` | `text` | `YES` | - | RSA-2048 private key PEM registered in Stalwart for DKIM signing. Server-side only; never exposed to clients. |
| 27 | `use_avatar` | `boolean` | `NO` | `false` | - |
| 28 | `avatar_url` | `text` | `YES` | - | - |
| 29 | `status` | `USER-DEFINED` | `NO` | `'not_started'::domain_status` | - |
| 30 | `region` | `text` | `NO` | `'ap-south-1'::text` | AWS SES region where the domain identity is registered and from which emails are sent (e.g., ap-south-1, ap-southeast-1, ap-northeast-1). |

---

## Table: `public.sending_identities`
- **Type**: `VIEW` | **Estimated Rows**: -1 | **RLS**: `DISABLED`
- **Total Bytes**: 0 bytes (Table: 0 bytes, Indexes: 0 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `YES` | - | - |
| 2 | `user_id` | `uuid` | `YES` | - | - |
| 3 | `provider_type` | `USER-DEFINED` | `YES` | - | - |
| 4 | `name` | `text` | `YES` | - | - |
| 5 | `smtp_host` | `text` | `YES` | - | - |
| 6 | `smtp_port` | `smallint` | `YES` | - | - |
| 7 | `smtp_username` | `text` | `YES` | - | - |
| 8 | `smtp_password` | `text` | `YES` | - | - |
| 9 | `google_access_token` | `text` | `YES` | - | - |
| 10 | `google_refresh_token` | `text` | `YES` | - | - |
| 11 | `google_email` | `text` | `YES` | - | - |
| 12 | `created_at` | `timestamp with time zone` | `YES` | - | - |
| 13 | `updated_at` | `timestamp with time zone` | `YES` | - | - |
| 14 | `daily_mail_limit` | `integer` | `YES` | - | - |
| 15 | `daily_mail_used` | `integer` | `YES` | - | - |
| 16 | `daily_mail_used_date` | `date` | `YES` | - | - |
| 17 | `google_expires_at` | `timestamp with time zone` | `YES` | - | - |
| 18 | `google_scope` | `text` | `YES` | - | - |
| 19 | `google_token_type` | `text` | `YES` | - | - |
| 20 | `account_key` | `text` | `YES` | - | - |
| 21 | `provisioned_by` | `USER-DEFINED` | `YES` | - | - |
| 22 | `custom_from_email` | `text` | `YES` | - | - |
| 23 | `custom_from_display_name` | `text` | `YES` | - | - |
| 24 | `billing_locked` | `boolean` | `YES` | - | - |
| 25 | `organization_id` | `uuid` | `YES` | - | - |
| 26 | `is_active` | `boolean` | `YES` | - | - |

---

## Table: `public.ses_event_inbox`
- **Type**: `TABLE` | **Estimated Rows**: 1,000 | **RLS**: `ENABLED`
- **Total Bytes**: 2,179,072 bytes (Table: 1,859,584 bytes, Indexes: 278,528 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `event_key` | `text` | `NO` | - | - |
| 2 | `region` | `text` | `NO` | - | - |
| 3 | `payload` | `jsonb` | `NO` | - | - |
| 4 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 5 | `processed_at` | `timestamp with time zone` | `YES` | - | - |
| 6 | `attempts` | `integer` | `NO` | `0` | - |
| 7 | `last_error` | `text` | `YES` | - | - |

---

## Table: `public.ses_event_log`
- **Type**: `TABLE` | **Estimated Rows**: 963 | **RLS**: `ENABLED`
- **Total Bytes**: 11,919,360 bytes (Table: 10,616,832 bytes, Indexes: 1,236,992 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `email_id` | `uuid` | `YES` | - | - |
| 3 | `organization_id` | `uuid` | `YES` | - | - |
| 4 | `event_type` | `text` | `NO` | - | - |
| 5 | `ses_message_id` | `text` | `YES` | - | - |
| 6 | `raw_payload` | `jsonb` | `NO` | - | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.ses_organization_tenants`
- **Type**: `TABLE` | **Estimated Rows**: 23 | **RLS**: `ENABLED`
- **Total Bytes**: 90,112 bytes (Table: 16,384 bytes, Indexes: 32,768 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `organization_id` | `uuid` | `NO` | - | - |
| 2 | `region` | `text` | `NO` | - | - |
| 3 | `tenant_name` | `text` | `NO` | - | - |
| 4 | `tenant_arn` | `text` | `NO` | - | - |
| 5 | `configuration_set` | `text` | `NO` | - | - |
| 6 | `ready` | `boolean` | `NO` | `false` | - |
| 7 | `aws_status` | `text` | `NO` | `'UNKNOWN'::text` | - |
| 8 | `customer_paused` | `boolean` | `NO` | `false` | - |
| 9 | `checked_at` | `timestamp with time zone` | `YES` | - | - |
| 10 | `sync_error` | `text` | `YES` | - | - |

---

## Table: `public.ses_recipient_outcomes`
- **Type**: `TABLE` | **Estimated Rows**: 2,357 | **RLS**: `ENABLED`
- **Total Bytes**: 1,409,024 bytes (Table: 589,824 bytes, Indexes: 778,240 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `organization_id` | `uuid` | `NO` | - | - |
| 2 | `message_id` | `text` | `NO` | - | - |
| 3 | `recipient` | `text` | `NO` | - | - |
| 4 | `region` | `text` | `NO` | - | - |
| 5 | `accepted_at` | `timestamp with time zone` | `NO` | - | - |
| 6 | `hard_bounced_at` | `timestamp with time zone` | `YES` | - | - |
| 7 | `complained_at` | `timestamp with time zone` | `YES` | - | - |
| 8 | `completed_at` | `timestamp with time zone` | `YES` | - | - |
| 9 | `bounced_at` | `timestamp with time zone` | `YES` | - | - |
| 10 | `invalid_recipient_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.ses_send_attempts`
- **Type**: `TABLE` | **Estimated Rows**: 273 | **RLS**: `ENABLED`
- **Total Bytes**: 204,800 bytes (Table: 73,728 bytes, Indexes: 90,112 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `email_id` | `uuid` | `YES` | - | - |
| 4 | `region` | `text` | `NO` | - | - |
| 5 | `recipients` | `ARRAY` | `NO` | - | - |
| 6 | `state` | `text` | `NO` | `'reserved'::text` | - |
| 7 | `message_id` | `text` | `YES` | - | - |
| 8 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 9 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.smtp_credentials`
- **Type**: `TABLE` | **Estimated Rows**: 10 | **RLS**: `ENABLED`
- **Total Bytes**: 114,688 bytes (Table: 8,192 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `created_by` | `uuid` | `NO` | - | - |
| 4 | `name` | `text` | `NO` | - | - |
| 5 | `username` | `text` | `NO` | - | - |
| 6 | `password_hash` | `text` | `NO` | - | - |
| 7 | `password_encrypted` | `text` | `NO` | - | - |
| 8 | `password_suffix` | `text` | `NO` | - | - |
| 9 | `enabled` | `boolean` | `NO` | `true` | - |
| 10 | `account_mode` | `USER-DEFINED` | `NO` | `'rotate'::smtp_credential_acco` | - |
| 11 | `prefer_account_id` | `uuid` | `YES` | - | - |
| 12 | `last_used_at` | `timestamp with time zone` | `YES` | - | - |
| 13 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 14 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.stalwart_accounts`
- **Type**: `VIEW` | **Estimated Rows**: -1 | **RLS**: `DISABLED`
- **Total Bytes**: 0 bytes (Table: 0 bytes, Indexes: 0 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `name` | `text` | `YES` | - | - |
| 2 | `type` | `text` | `YES` | - | - |
| 3 | `secret` | `text` | `YES` | - | - |
| 4 | `description` | `text` | `YES` | - | - |
| 5 | `quota` | `bigint` | `YES` | - | - |
| 6 | `active` | `boolean` | `YES` | - | - |
| 7 | `organization_id` | `uuid` | `YES` | - | - |
| 8 | `created_at` | `timestamp with time zone` | `YES` | - | - |
| 9 | `updated_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.stalwart_domains`
- **Type**: `VIEW` | **Estimated Rows**: -1 | **RLS**: `DISABLED`
- **Total Bytes**: 0 bytes (Table: 0 bytes, Indexes: 0 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `name` | `text` | `YES` | - | - |
| 2 | `type` | `text` | `YES` | - | - |
| 3 | `organization_id` | `uuid` | `YES` | - | - |
| 4 | `created_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.stalwart_emails`
- **Type**: `VIEW` | **Estimated Rows**: -1 | **RLS**: `DISABLED`
- **Total Bytes**: 0 bytes (Table: 0 bytes, Indexes: 0 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `address` | `text` | `YES` | - | - |
| 2 | `name` | `text` | `YES` | - | - |
| 3 | `type` | `text` | `YES` | - | - |

---

## Table: `public.supabase_integrations`
- **Type**: `TABLE` | **Estimated Rows**: 1 | **RLS**: `ENABLED`
- **Total Bytes**: 114,688 bytes (Table: 8,192 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `created_by` | `uuid` | `NO` | - | - |
| 4 | `supabase_access_token_encrypted` | `text` | `NO` | - | - |
| 5 | `supabase_refresh_token_encrypted` | `text` | `NO` | - | - |
| 6 | `supabase_token_expires_at` | `timestamp with time zone` | `YES` | - | - |
| 7 | `supabase_project_ref` | `text` | `YES` | - | - |
| 8 | `supabase_project_name` | `text` | `YES` | - | - |
| 9 | `supabase_org_id` | `text` | `YES` | - | - |
| 10 | `table_schema` | `text` | `NO` | `'public'::text` | - |
| 11 | `table_name` | `text` | `YES` | - | - |
| 12 | `event_type` | `text` | `YES` | - | - |
| 13 | `filter_column` | `text` | `YES` | - | - |
| 14 | `filter_value` | `text` | `YES` | - | - |
| 15 | `recipient_column` | `text` | `YES` | - | - |
| 16 | `template_id` | `uuid` | `YES` | - | - |
| 17 | `supabase_webhook_id` | `text` | `YES` | - | - |
| 18 | `supabase_webhook_secret_encrypted` | `text` | `YES` | - | - |
| 19 | `is_active` | `boolean` | `NO` | `false` | - |
| 20 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 21 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 22 | `emails_sent` | `integer` | `NO` | `0` | - |
| 23 | `last_sent_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.support_ticket_messages`
- **Type**: `TABLE` | **Estimated Rows**: 1 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 8,192 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `ticket_id` | `uuid` | `NO` | - | - |
| 3 | `sender_id` | `uuid` | `NO` | - | - |
| 4 | `sender_role` | `text` | `NO` | - | - |
| 5 | `message` | `text` | `NO` | - | - |
| 6 | `attachment_url` | `text` | `YES` | - | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `read_at` | `timestamp with time zone` | `YES` | - | - |

---

## Table: `public.support_tickets`
- **Type**: `TABLE` | **Estimated Rows**: 2 | **RLS**: `ENABLED`
- **Total Bytes**: 131,072 bytes (Table: 8,192 bytes, Indexes: 81,920 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `created_by` | `uuid` | `NO` | - | - |
| 3 | `subject` | `text` | `NO` | - | - |
| 4 | `body` | `text` | `NO` | - | - |
| 5 | `status` | `USER-DEFINED` | `NO` | `'open'::support_ticket_status` | - |
| 6 | `priority` | `USER-DEFINED` | `NO` | `'normal'::support_ticket_prior` | - |
| 7 | `admin_notes` | `text` | `YES` | - | - |
| 8 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 9 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 10 | `category` | `USER-DEFINED` | `NO` | `'support'::support_ticket_cate` | User-facing ticket category (support, feature request, or complaint). |
| 11 | `attachment_url` | `text` | `YES` | - | Public URL of an optional screenshot attached to feature feedback. |

---

## Table: `public.template_editor_drafts`
- **Type**: `TABLE` | **Estimated Rows**: 26 | **RLS**: `ENABLED`
- **Total Bytes**: 393,216 bytes (Table: 212,992 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `template_id` | `uuid` | `NO` | - | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `user_id` | `uuid` | `NO` | - | - |
| 4 | `revision` | `bigint` | `NO` | `1` | - |
| 5 | `base_revision` | `bigint` | `NO` | - | - |
| 6 | `payload` | `jsonb` | `NO` | - | - |
| 7 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.templates`
- **Type**: `TABLE` | **Estimated Rows**: 70 | **RLS**: `ENABLED`
- **Total Bytes**: 516,096 bytes (Table: 278,528 bytes, Indexes: 73,728 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `name` | `text` | `NO` | - | - |
| 4 | `subject` | `text` | `NO` | `''::text` | - |
| 5 | `body` | `text` | `NO` | `''::text` | - |
| 6 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 7 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `body_json` | `jsonb` | `YES` | - | TipTap editor document JSON; HTML is stored in body. |
| 9 | `billing_locked` | `boolean` | `NO` | `false` | - |
| 10 | `organization_id` | `uuid` | `NO` | - | - |
| 11 | `is_public` | `boolean` | `YES` | `false` | - |
| 12 | `category` | `text` | `YES` | - | - |
| 13 | `thumbnail_url` | `text` | `YES` | - | - |
| 14 | `from_email` | `text` | `YES` | - | Default From header (e.g. Acme <acme@example.com> or acme@example.com) for this template. |
| 15 | `reply_to` | `text` | `YES` | - | Default Reply-To email address for this template. |
| 16 | `preview_text` | `text` | `YES` | - | Inbox preview snippet / preheader text for this template. |
| 17 | `variable_names` | `ARRAY` | `NO` | - | Read-only, sorted unique placeholder names from subject, body, preview_text and body_json. Computed on every write; values are supplied separately when sending. |
| 18 | `editor_revision` | `bigint` | `NO` | `0` | - |
| 19 | `editor_format` | `text` | `YES` | - | - |
| 20 | `editor_version` | `integer` | `YES` | - | - |
| 21 | `template_key` | `text` | `YES` | - | - |
| 22 | `published_native_version_id` | `uuid` | `YES` | - | - |

---

## Table: `public.tenant_suppression_list`
- **Type**: `TABLE` | **Estimated Rows**: 20 | **RLS**: `ENABLED`
- **Total Bytes**: 147,456 bytes (Table: 8,192 bytes, Indexes: 98,304 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `email` | `text` | `NO` | - | - |
| 4 | `reason` | `text` | `NO` | - | - |
| 5 | `source` | `text` | `NO` | `'ses_webhook'::text` | - |
| 6 | `metadata` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.test_apply`
- **Type**: `TABLE` | **Estimated Rows**: 0 | **RLS**: `ENABLED`
- **Total Bytes**: 0 bytes (Table: 0 bytes, Indexes: 0 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `integer` | `YES` | - | - |

---

## Table: `public.topics`
- **Type**: `TABLE` | **Estimated Rows**: 6 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 8,192 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `name` | `text` | `NO` | - | - |
| 4 | `slug` | `text` | `NO` | - | - |
| 5 | `description` | `text` | `YES` | - | - |
| 6 | `default_subscription` | `text` | `NO` | `'opt_in'::text` | - |
| 7 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 8 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 9 | `visibility` | `text` | `NO` | `'private'::text` | - |
| 10 | `requires_confirmation` | `boolean` | `NO` | `false` | - |

---

## Table: `public.user_notifications`
- **Type**: `TABLE` | **Estimated Rows**: 3 | **RLS**: `ENABLED`
- **Total Bytes**: 114,688 bytes (Table: 8,192 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `kind` | `USER-DEFINED` | `NO` | - | - |
| 4 | `title` | `text` | `NO` | - | - |
| 5 | `body` | `text` | `NO` | - | - |
| 6 | `action_href` | `text` | `YES` | - | - |
| 7 | `action_label` | `text` | `YES` | - | - |
| 8 | `metadata` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 9 | `read_at` | `timestamp with time zone` | `YES` | - | - |
| 10 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 11 | `dedupe_key` | `text` | `NO` | - | - |

---

## Table: `public.user_onboarding_responses`
- **Type**: `TABLE` | **Estimated Rows**: 290 | **RLS**: `ENABLED`
- **Total Bytes**: 188,416 bytes (Table: 40,960 bytes, Indexes: 106,496 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `user_id` | `uuid` | `NO` | - | - |
| 3 | `question_key` | `text` | `NO` | - | - |
| 4 | `answer_value` | `text` | `NO` | - | - |
| 5 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 6 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.users`
- **Type**: `TABLE` | **Estimated Rows**: 270 | **RLS**: `ENABLED`
- **Total Bytes**: 172,032 bytes (Table: 49,152 bytes, Indexes: 81,920 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | - | - |
| 2 | `role` | `USER-DEFINED` | `NO` | `'user'::user_role` | - |
| 3 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 4 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 5 | `email` | `text` | `YES` | - | - |
| 6 | `display_name` | `text` | `YES` | - | Preferred name from onboarding / profile. |
| 7 | `company_name` | `text` | `YES` | - | Company or organization from onboarding. |
| 8 | `onboarding_completed` | `boolean` | `NO` | `false` | When true, skip the first-login onboarding flow. |
| 9 | `has_email_password` | `boolean` | `NO` | `false` | Set when the user saves an auth password via the app; complements auth.identities for Mailofly account UI. |
| 13 | `user_type` | `USER-DEFINED` | `NO` | `'free'::user_billing_type` | free: no prepaid balance; payg: wallet_balance_inr > 0 (maintained by trigger). |
| 25 | `account_type` | `USER-DEFINED` | `NO` | `'transactional_email_users'::u` | Used to segment users into transactional vs campaign email workflows. |
| 26 | `onboarding_first_email_sent_at` | `timestamp with time zone` | `YES` | - | Set when the user successfully sends the onboarding test email via /user/onboarding. |
| 27 | `default_organization_id` | `uuid` | `YES` | - | - |
| 28 | `mobile_phone` | `text` | `YES` | - | E.164 mobile number, optional, from welcome onboarding. |
| 29 | `mobile_country_code` | `text` | `YES` | - | ISO 3166-1 alpha-2 country used for mobile_phone dial code. |
| 30 | `marketing_contact_consent` | `boolean` | `NO` | `false` | User opted in to support and promotional contact |
| 31 | `marketing_contact_consent_at` | `timestamp with time zone` | `YES` | - | When marketing_contact_consent was last set to true. |
| 32 | `phone` | `text` | `YES` | - | E.164 phone number when provided during onboarding or settings. |
| 33 | `phone_country_code` | `text` | `YES` | - | ISO 3166-1 alpha-2 country used for phone entry. |
| 34 | `referredby` | `uuid` | `YES` | - | ID of the user who referred this user (nullable). |
| 35 | `referral_code` | `text` | `YES` | - | Unique referral code for sharing referral links. |
| 36 | `admin_role_id` | `uuid` | `YES` | - | - |

---

## Table: `public.webhook_deliveries`
- **Type**: `TABLE` | **Estimated Rows**: 25 | **RLS**: `ENABLED`
- **Total Bytes**: 172,032 bytes (Table: 40,960 bytes, Indexes: 90,112 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `webhook_id` | `uuid` | `NO` | - | - |
| 4 | `event` | `text` | `NO` | - | - |
| 5 | `payload` | `jsonb` | `NO` | `'{}'::jsonb` | - |
| 6 | `status` | `USER-DEFINED` | `NO` | `'pending'::webhook_delivery_st` | - |
| 7 | `attempts` | `integer` | `NO` | `0` | - |
| 8 | `next_attempt_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 9 | `last_status_code` | `integer` | `YES` | - | - |
| 10 | `last_error` | `text` | `YES` | - | - |
| 11 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 12 | `delivered_at` | `timestamp with time zone` | `YES` | - | - |
| 13 | `received_email_id` | `uuid` | `YES` | - | - |

---

## Table: `public.webhooks`
- **Type**: `TABLE` | **Estimated Rows**: 2 | **RLS**: `ENABLED`
- **Total Bytes**: 98,304 bytes (Table: 8,192 bytes, Indexes: 49,152 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `created_by` | `uuid` | `NO` | - | - |
| 4 | `name` | `text` | `NO` | - | - |
| 5 | `url` | `text` | `NO` | - | - |
| 6 | `secret_encrypted` | `text` | `NO` | - | - |
| 7 | `secret_suffix` | `text` | `NO` | - | - |
| 8 | `events` | `ARRAY` | `NO` | `'{}'::text[]` | - |
| 9 | `source` | `USER-DEFINED` | `NO` | `'all'::webhook_source` | - |
| 10 | `enabled` | `boolean` | `NO` | `true` | - |
| 11 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |
| 12 | `updated_at` | `timestamp with time zone` | `NO` | `now()` | - |

---

## Table: `public.workspace_logs_unified`
- **Type**: `VIEW` | **Estimated Rows**: -1 | **RLS**: `DISABLED`
- **Total Bytes**: 0 bytes (Table: 0 bytes, Indexes: 0 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `YES` | - | - |
| 2 | `kind` | `text` | `YES` | - | - |
| 3 | `protocol` | `text` | `YES` | - | - |
| 4 | `method` | `text` | `YES` | - | - |
| 5 | `endpoint` | `text` | `YES` | - | - |
| 6 | `status_code` | `integer` | `YES` | - | - |
| 7 | `api_key_id` | `uuid` | `YES` | - | - |
| 8 | `user_agent` | `text` | `YES` | - | - |
| 9 | `ip_address` | `text` | `YES` | - | - |
| 10 | `email_id` | `uuid` | `YES` | - | - |
| 11 | `duration_ms` | `integer` | `YES` | - | - |
| 12 | `request_body` | `text` | `YES` | - | - |
| 13 | `response_body` | `text` | `YES` | - | - |
| 14 | `from_email` | `text` | `YES` | - | - |
| 15 | `to_email` | `text` | `YES` | - | - |
| 16 | `subject` | `text` | `YES` | - | - |
| 17 | `error` | `text` | `YES` | - | - |
| 18 | `created_at` | `timestamp with time zone` | `YES` | - | - |
| 19 | `organization_id` | `uuid` | `YES` | - | - |

---

## Table: `public.workspace_uploads`
- **Type**: `TABLE` | **Estimated Rows**: 3 | **RLS**: `ENABLED`
- **Total Bytes**: 114,688 bytes (Table: 8,192 bytes, Indexes: 65,536 bytes)

| # | Column Name | Data Type | Nullable | Default | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `id` | `uuid` | `NO` | `gen_random_uuid()` | - |
| 2 | `organization_id` | `uuid` | `NO` | - | - |
| 3 | `user_id` | `uuid` | `YES` | - | - |
| 4 | `bucket_id` | `text` | `NO` | - | - |
| 5 | `object_path` | `text` | `NO` | - | - |
| 6 | `created_at` | `timestamp with time zone` | `NO` | `now()` | - |

---
