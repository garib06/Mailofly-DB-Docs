import subprocess
import json
import os
import sys

# Load database metadata
with open("c:/projects/maiofly_test/supabase_docs/metadata.json", "r", encoding="utf-8") as f:
    meta = json.load(f)

# Launch figcraft-cli MCP engine process
p = subprocess.Popen(
    ["C:\\Program Files\\FigCraft\\figcraft-cli.exe", "mcp"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)

msg_id = 0
def send(method, params):
    global msg_id
    msg_id += 1
    req = {"jsonrpc": "2.0", "id": msg_id, "method": method, "params": params}
    p.stdin.write(json.dumps(req) + "\n")
    p.stdin.flush()
    while True:
        line = p.stdout.readline()
        if not line:
            break
        line = line.strip()
        if line.startswith("{"):
            try:
                res = json.loads(line)
                if res.get("id") == msg_id:
                    return res
            except:
                pass
    return None

def call_tool(name, args):
    res = send("tools/call", {"name": name, "arguments": args})
    if not res or "result" not in res:
        print(f"Error calling {name}: {res}")
        return None
    content = res["result"].get("content", [])
    if content and "text" in content[0]:
        try:
            return json.loads(content[0]["text"])
        except:
            return content[0]["text"]
    return res["result"]

def run_cmd(command, params=None):
    return call_tool("run_command", {"command": command, "params": params or {}})

# Palette constants
BG_COLOR = "#0B1020"
SURFACE_COLOR = "#111827"
CARD_BG = "#172033"
CARD_BORDER = "#1E293B"
TEXT_PRIMARY = "#F8FAFC"
TEXT_SECONDARY = "#94A3B8"
ACCENT_BLUE = "#3B82F6"
SUCCESS_GREEN = "#22C55E"
WARNING_YELLOW = "#F59E0B"
CRITICAL_RED = "#EF4444"
PURPLE_ACCENT = "#8B5CF6"

def create_frame(name, parent=None, width=None, height=None, x=None, y=None, props=None):
    args = {"type": "frame", "name": name}
    if parent is not None:
        args["parent"] = parent
    if width is not None:
        args["width"] = width
    if height is not None:
        args["height"] = height
    if x is not None:
        args["x"] = x
    if y is not None:
        args["y"] = y
    if props is not None:
        args["props"] = props
    res = call_tool("create_node", args)
    if isinstance(res, dict) and "id" in res:
        return res["id"]
    return None

def create_text(name, text, parent=None, fontSize=12, fill=TEXT_PRIMARY, props=None):
    p = {"fontSize": fontSize, "fill": fill}
    if props:
        p.update(props)
    args = {"type": "text", "name": name, "text": text, "props": p}
    if parent is not None:
        args["parent"] = parent
    res = call_tool("create_node", args)
    if isinstance(res, dict) and "id" in res:
        return res["id"]
    return None

print("Initializing FigCraft MCP session...")
init_res = send("initialize", {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {"name": "architecture-generator", "version": "1.0"}
})
print("Connected to FigCraft MCP:", init_res.get("result", {}).get("serverInfo", {}).get("name"))

# ==============================================================================
# Helper to set up a standard page header
# ==============================================================================
def setup_page_header(page_title, page_subtitle, page_num):
    root_id = create_frame(
        f"Page {page_num}: {page_title}",
        width=1440,
        x=60, y=60,
        props={"fill": BG_COLOR, "layout": "vertical", "gap": 22, "padding": 40, "sizingV": "hug"}
    )
    hdr_id = create_frame("Header Block", parent=root_id, props={"fill": "#00000000", "layout": "vertical", "gap": 6, "sizingH": "fill", "sizingV": "hug"})
    create_text("Page Title", f"{page_num}. {page_title}", parent=hdr_id, fontSize=24, fill=TEXT_PRIMARY)
    create_text("Page Subtitle", page_subtitle, parent=hdr_id, fontSize=13, fill=TEXT_SECONDARY)
    return root_id

# ==============================================================================
# PAGE 1: DATABASE OVERVIEW
# ==============================================================================
print("Generating Page 1: Database Overview...")
run_cmd("page.rename", {"name": "1. Database Overview"})
run_cmd("page.setBackground", {"color": BG_COLOR})

p1_root = setup_page_header(
    "Database Overview & Metadata Dashboard",
    "Supabase Production Database Audit: mailofly | PostgreSQL 17.6 (aarch64) | Ref: aymarrhbnaygxkaorjfl | Status: ACTIVE_HEALTHY",
    1
)

# Metric Row 1
m_row1 = create_frame("Metric Row 1", parent=p1_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 18, "sizingH": "fill", "sizingV": "hug"})
for label, val, sub, col in [
    ("Total Tables", "169", "104 Public Base | 7 Views | 58 System", ACCENT_BLUE),
    ("Foreign Key Constraints", "215", "Active Referential Constraints", SUCCESS_GREEN),
    ("Total Indexes", "523", "B-tree, Unique & Compound", ACCENT_BLUE),
    ("RLS Security Coverage", "100%", "104 of 104 Public Tables Secured", SUCCESS_GREEN)
]:
    c_id = create_frame(f"Card: {label}", parent=m_row1, width=326, props={"fill": CARD_BG, "cornerRadius": 12, "padding": 16, "layout": "vertical", "gap": 4, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
    create_text("L", label, parent=c_id, fontSize=12, fill=TEXT_SECONDARY)
    create_text("V", val, parent=c_id, fontSize=28, fill=col)
    create_text("S", sub, parent=c_id, fontSize=11, fill=TEXT_SECONDARY)

# Metric Row 2
m_row2 = create_frame("Metric Row 2", parent=p1_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 18, "sizingH": "fill", "sizingV": "hug"})
for label, val, sub, col in [
    ("Total Columns", "1,771", "Across all schemas and tables", TEXT_PRIMARY),
    ("Stored Functions", "224", "Triggers, RLS helpers & RPCs", TEXT_PRIMARY),
    ("Total Database Size", "~50.5 MB", "Top: emails (14.4MB), ses_logs (11.4MB)", WARNING_YELLOW),
    ("FKs Missing Indexes", "59", "Optimization opportunities identified", WARNING_YELLOW)
]:
    c_id = create_frame(f"Card: {label}", parent=m_row2, width=326, props={"fill": CARD_BG, "cornerRadius": 12, "padding": 16, "layout": "vertical", "gap": 4, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
    create_text("L", label, parent=c_id, fontSize=12, fill=TEXT_SECONDARY)
    create_text("V", val, parent=c_id, fontSize=28, fill=col)
    create_text("S", sub, parent=c_id, fontSize=11, fill=TEXT_SECONDARY)

# Content Panels Row
content_row1 = create_frame("Content Panels Row", parent=p1_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

# Left Panel: Domain Model
left_p1 = create_frame("Domain Model Panel", parent=content_row1, width=670, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 24, "layout": "vertical", "gap": 10, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🏢 Core SaaS Domain Model", parent=left_p1, fontSize=16, fill=ACCENT_BLUE)
create_text("Body", 
    "• Multi-Tenancy Boundary:\n"
    "  The `organizations` table acts as the master multi-tenant anchor. All customer data (contacts, campaigns, emails, mailboxes, domains) is strictly partitioned by organization_id.\n\n"
    "• Email Dispatch & AWS SES Ingestion:\n"
    "  High-volume transactional and marketing email pipeline. Webhook events stream into `ses_event_inbox`, recorded in `ses_event_log`, and update `ses_recipient_outcomes`.\n\n"
    "• Drip & Event Automation:\n"
    "  Automations workflow system (automations, automation_runs, automation_run_steps, automation_events) drives behavioral email sequences.\n\n"
    "• Audience & CRM:\n"
    "  Rich contact model with dynamic segmentation (segment_contacts), custom properties (contact_property_values), and subscription state.",
    parent=left_p1, fontSize=12, fill=TEXT_SECONDARY
)

# Right Panel: Schemas
right_p1 = create_frame("Schema Inventory Panel", parent=content_row1, width=670, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 24, "layout": "vertical", "gap": 10, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "📊 Schema & Object Inventory", parent=right_p1, fontSize=16, fill=SUCCESS_GREEN)
create_text("Body",
    "• public Schema: 104 Base Tables, 7 Views, 224 Functions, 119 Enums\n"
    "  Contains the complete application domain (tenancy, campaigns, contacts, billing).\n\n"
    "• auth Schema: 27 Tables\n"
    "  Managed by Supabase GoTrue (users, identities, sessions, mfa_factors, refresh_tokens).\n\n"
    "• storage Schema: 10 Tables\n"
    "  Supabase Storage engine (buckets, objects, s3_multipart_uploads).\n\n"
    "• realtime Schema: 10 Tables\n"
    "  Realtime broadcast, presence, and change data capture subscriptions.\n\n"
    "• extensions & cron Schemas: 6 Tables\n"
    "  pg_cron scheduled jobs (mail queue crons) and vault secret keys.",
    parent=right_p1, fontSize=12, fill=TEXT_SECONDARY
)

# ==============================================================================
# PAGE 2: COMPLETE ENTITY RELATIONSHIP DIAGRAM
# ==============================================================================
print("Generating Page 2: Entity Relationship Diagram...")
run_cmd("page.add", {"name": "2. Entity Relationship Diagram"})
run_cmd("page.setBackground", {"color": BG_COLOR})

p2_root = setup_page_header(
    "Entity Relationship Diagram (Core Application Modules)",
    "Mapped foreign key constraints across Tenancy, CRM, Campaigns, Deliveries, Automations & Billing",
    2
)

p2_grid = create_frame("ERD Modules Container", parent=p2_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

erd_modules = [
    ("Tenancy & Identity", [
        ("organizations", "🔑 id: uuid", ["name: text", "slug: text", "owner_id: uuid", "created_at: tstz"]),
        ("organization_members", "🔑 id: uuid", ["🔗 org_id: uuid (FK)", "🔗 user_id: uuid (FK)", "role: text"]),
        ("users", "🔑 id: uuid (auth)", ["email: text", "full_name: text", "avatar_url: text"])
    ], ACCENT_BLUE),
    ("Audience & CRM", [
        ("contacts", "🔑 id: uuid", ["🔗 org_id: uuid (FK)", "email: text", "status: text", "created_at: tstz"]),
        ("contact_segments", "🔑 id: uuid", ["🔗 org_id: uuid (FK)", "name: text", "filter_rules: jsonb"]),
        ("segment_contacts", "🔑 id: uuid (Junction)", ["🔗 segment_id: uuid (FK)", "🔗 contact_id: uuid (FK)"])
    ], SUCCESS_GREEN),
    ("Campaigns & Broadcasts", [
        ("campaigns", "🔑 id: uuid", ["🔗 org_id: uuid (FK)", "name: text", "status: text", "subject: text"]),
        ("campaign_runs", "🔑 id: uuid", ["🔗 campaign_id: uuid (FK)", "started_at: tstz", "status: text"]),
        ("campaign_run_audience", "🔑 id: uuid (Junction)", ["🔗 run_id: uuid (FK)", "🔗 contact_id: uuid (FK)"])
    ], PURPLE_ACCENT),
    ("Sending & Delivery", [
        ("mailboxes", "🔑 id: uuid", ["🔗 org_id: uuid (FK)", "email: text", "status: text", "daily_limit: int"]),
        ("emails", "🔑 id: uuid", ["🔗 mailbox_id: uuid (FK)", "recipient: text", "subject: text", "status: text"]),
        ("ses_event_log", "🔑 id: uuid", ["🔗 email_id: uuid (FK)", "event_type: text", "timestamp: tstz"])
    ], WARNING_YELLOW)
]

for mod_title, tables_list, mod_color in erd_modules:
    mod_box = create_frame(f"Module: {mod_title}", parent=p2_grid, width=325, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 16, "layout": "vertical", "gap": 12, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
    create_text("ModTitle", f"📦 {mod_title}", parent=mod_box, fontSize=14, fill=mod_color)
    for tbl_name, pk_col, cols in tables_list:
        t_box = create_frame(f"Tbl: {tbl_name}", parent=mod_box, props={"fill": SURFACE_COLOR, "cornerRadius": 8, "padding": 10, "layout": "vertical", "gap": 4, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingH": "fill", "sizingV": "hug"})
        create_text("TblName", f"📄 {tbl_name}", parent=t_box, fontSize=12, fill=TEXT_PRIMARY)
        create_text("PK", pk_col, parent=t_box, fontSize=10, fill=WARNING_YELLOW)
        for c in cols:
            c_col = ACCENT_BLUE if "🔗" in c else TEXT_SECONDARY
            create_text("C", f"  {c}", parent=t_box, fontSize=10, fill=c_col)

# ==============================================================================
# PAGE 3: SCHEMA-WISE DATABASE STRUCTURE
# ==============================================================================
print("Generating Page 3: Schema Structure...")
run_cmd("page.add", {"name": "3. Schema-wise Database Structure"})
run_cmd("page.setBackground", {"color": BG_COLOR})

p3_root = setup_page_header(
    "Schema-wise Database Structure & Breakdown",
    "Categorized inspection of public, auth, storage, realtime, and extension namespaces",
    3
)

p3_grid = create_frame("Schemas Grid", parent=p3_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

schemas_data = [
    ("public (Application)", "104 Base Tables | 7 Views", [
        "Core Multi-tenancy: organizations, members, invitations",
        "CRM & Audience: contacts, segments, topics, properties",
        "Email Infrastructure: mailboxes, domains, smtp, ses_logs",
        "Automation Pipeline: automations, runs, steps, events",
        "Billing System: plans, subscriptions, addons, ledger",
        "Developer Ecosystem: api_keys, webhooks, oauth_clients"
    ], ACCENT_BLUE),
    ("auth (Supabase GoTrue)", "27 Tables", [
        "users: Core user identity records",
        "identities: OAuth & email identity mappings",
        "sessions & refresh_tokens: Active user JWT sessions",
        "mfa_factors & mfa_challenges: Multi-factor auth",
        "sso_providers & sso_domains: Enterprise SAML/SSO",
        "audit_log_entries: Security and login event tracking"
    ], SUCCESS_GREEN),
    ("storage (Asset Engine)", "10 Tables", [
        "buckets: S3 bucket namespaces & configuration",
        "objects: File object metadata, paths, and mime types",
        "s3_multipart_uploads: Multipart upload state tracker",
        "bucket_lifecycle_states: Expiration and lifecycle rules"
    ], PURPLE_ACCENT),
    ("realtime & extensions", "16 Tables", [
        "realtime.channels: WebSocket broadcast subscriptions",
        "cron.job & job_run_details: Background cron runners",
        "vault.secrets: Encrypted secrets storage",
        "extensions: pg_trgm, uuid-ossp, pgcrypto, etc."
    ], WARNING_YELLOW)
]

for s_name, s_meta, s_items, s_color in schemas_data:
    s_box = create_frame(f"Schema: {s_name}", parent=p3_grid, width=325, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 18, "layout": "vertical", "gap": 10, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
    create_text("SName", s_name, parent=s_box, fontSize=15, fill=s_color)
    create_text("SMeta", s_meta, parent=s_box, fontSize=11, fill=TEXT_SECONDARY)
    for it in s_items:
        it_box = create_frame("Item", parent=s_box, props={"fill": SURFACE_COLOR, "cornerRadius": 6, "padding": 8, "layout": "vertical", "sizingH": "fill", "sizingV": "hug"})
        create_text("ItTxt", it, parent=it_box, fontSize=11, fill=TEXT_PRIMARY)

# ==============================================================================
# PAGE 4: TABLE DETAILS & DATA DICTIONARY
# ==============================================================================
print("Generating Page 4: Table Details...")
run_cmd("page.add", {"name": "4. Table Details"})
run_cmd("page.setBackground", {"color": BG_COLOR})

p4_root = setup_page_header(
    "Table Details & Data Dictionary (Core Anchor Tables)",
    "Exhaustive column types, constraints, default expressions, indexes, and security policies",
    4
)

p4_grid = create_frame("Tables Detail Grid", parent=p4_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

core_tables = [
    ("organizations", [
        ("id", "uuid", "gen_random_uuid()", "PK"),
        ("name", "text", "NOT NULL", "Attribute"),
        ("slug", "text", "NOT NULL [UNIQUE]", "Attribute"),
        ("owner_id", "uuid", "REFERENCES users(id)", "FK"),
        ("created_at", "timestamptz", "now()", "Timestamp")
    ], "4 Policies (CRUD) | 6 Indexes"),
    ("contacts", [
        ("id", "uuid", "gen_random_uuid()", "PK"),
        ("organization_id", "uuid", "REFERENCES organizations(id)", "FK"),
        ("email", "text", "NOT NULL", "Attribute"),
        ("status", "text", "'subscribed'", "Attribute"),
        ("attributes", "jsonb", "'{}'::jsonb", "Data")
    ], "4 Policies (Org-scoped) | 7 Indexes (4.38 MB)"),
    ("emails", [
        ("id", "uuid", "gen_random_uuid()", "PK"),
        ("mailbox_id", "uuid", "REFERENCES mailboxes(id)", "FK"),
        ("recipient", "text", "NOT NULL", "Attribute"),
        ("subject", "text", "NOT NULL", "Attribute"),
        ("status", "text", "'queued'", "Attribute")
    ], "3 Policies | 8 Indexes (14.36 MB)"),
    ("automations", [
        ("id", "uuid", "gen_random_uuid()", "PK"),
        ("organization_id", "uuid", "REFERENCES organizations(id)", "FK"),
        ("name", "text", "NOT NULL", "Attribute"),
        ("trigger_type", "text", "NOT NULL", "Attribute"),
        ("is_active", "boolean", "false", "Attribute")
    ], "4 Policies (Org-scoped) | 4 Indexes")
]

for t_name, cols_info, t_meta in core_tables:
    dt_box = create_frame(f"Detail: {t_name}", parent=p4_grid, width=325, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 18, "layout": "vertical", "gap": 10, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
    create_text("Title", f"📋 public.{t_name}", parent=dt_box, fontSize=15, fill=ACCENT_BLUE)
    create_text("Meta", t_meta, parent=dt_box, fontSize=11, fill=SUCCESS_GREEN)
    for c_name, c_type, c_def, c_kind in cols_info:
        r_box = create_frame("Col Line", parent=dt_box, props={"fill": SURFACE_COLOR, "cornerRadius": 6, "padding": 6, "layout": "horizontal", "mainAlign": "spaceBetween", "sizingH": "fill", "sizingV": "hug"})
        k_color = WARNING_YELLOW if c_kind == "PK" else (ACCENT_BLUE if c_kind == "FK" else TEXT_PRIMARY)
        create_text("Col", f"{c_name} ({c_type})", parent=r_box, fontSize=11, fill=k_color)
        create_text("Def", c_def[:16], parent=r_box, fontSize=10, fill=TEXT_SECONDARY)

# ==============================================================================
# PAGE 5: RELATIONSHIP MAP
# ==============================================================================
print("Generating Page 5: Relationship Map...")
run_cmd("page.add", {"name": "5. Relationship Map"})
run_cmd("page.setBackground", {"color": BG_COLOR})

p5_root = setup_page_header(
    "Database Relationship Map & Cardinality Matrix",
    "Structural mapping of 1:1, 1:N, N:M Junction Tables, and Standalone Entities",
    5
)

p5_grid = create_frame("Rel Matrix Container", parent=p5_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

rel_sections = [
    ("One-to-Many (1 : N)", [
        "organizations ──< campaigns",
        "organizations ──< contacts",
        "organizations ──< mailboxes",
        "organizations ──< automations",
        "campaigns ──< campaign_runs",
        "mailboxes ──< emails",
        "emails ──< ses_event_log",
        "plans ──< organization_subscriptions"
    ], SUCCESS_GREEN),
    ("Many-to-Many Junctions (N : M)", [
        "segment_contacts (segments ↔ contacts)",
        "organization_members (orgs ↔ users)",
        "campaign_run_audience (runs ↔ contacts)",
        "contact_topics (contacts ↔ topics)",
        "admin_role_permissions (roles ↔ perms)",
        "billing_addon_orders (orgs ↔ addons)"
    ], PURPLE_ACCENT),
    ("One-to-One (1 : 1)", [
        "users ↔ account_lifecycle_state",
        "organizations ↔ organization_usage",
        "organizations ↔ org_sending_protection",
        "organizations ↔ org_billing_plan_state"
    ], ACCENT_BLUE),
    ("Standalone / Unrelated", [
        "global_suppression_list (System-wide)",
        "app_settings (Platform-wide config)",
        "test_apply (Orphaned test table)"
    ], WARNING_YELLOW)
]

for r_title, r_list, r_color in rel_sections:
    rel_box = create_frame(f"Rel: {r_title}", parent=p5_grid, width=325, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 18, "layout": "vertical", "gap": 10, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
    create_text("RTitle", r_title, parent=rel_box, fontSize=14, fill=r_color)
    for itm in r_list:
        row_b = create_frame("RelRow", parent=rel_box, props={"fill": SURFACE_COLOR, "cornerRadius": 6, "padding": 8, "layout": "vertical", "sizingH": "fill", "sizingV": "hug"})
        create_text("RItm", itm, parent=row_b, fontSize=11, fill=TEXT_PRIMARY)

# ==============================================================================
# PAGE 6: INDEX AND PERFORMANCE ANALYSIS
# ==============================================================================
print("Generating Page 6: Performance Analysis...")
run_cmd("page.add", {"name": "6. Index & Performance Analysis"})
run_cmd("page.setBackground", {"color": BG_COLOR})

p6_root = setup_page_header(
    "Index & Database Performance Analysis",
    "Table sizing analysis, index coverage audit, and 59 foreign key indexing opportunities",
    6
)

p6_grid = create_frame("Perf Grid", parent=p6_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

# Card 1: Largest Tables
c1_perf = create_frame("Top Tables", parent=p6_grid, width=440, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 20, "layout": "vertical", "gap": 10, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "📦 Top Tables by Storage Size", parent=c1_perf, fontSize=16, fill=WARNING_YELLOW)
for tbl, sz, rows in [
    ("public.emails", "14.36 MB", "379 rows (heavy body/payloads)"),
    ("public.ses_event_log", "11.37 MB", "963 rows (SES JSON webhooks)"),
    ("public.api_key_request_logs", "9.82 MB", "485 rows (API request dumps)"),
    ("public.contacts", "4.38 MB", "1,224 rows (attributes jsonb)"),
    ("public.ses_event_inbox", "2.08 MB", "1,000 rows (event queue)"),
    ("public.ses_recipient_outcomes", "1.34 MB", "2,357 rows (delivery logs)")
]:
    t_row = create_frame("Row", parent=c1_perf, props={"fill": SURFACE_COLOR, "cornerRadius": 6, "padding": 8, "layout": "horizontal", "mainAlign": "spaceBetween", "sizingH": "fill", "sizingV": "hug"})
    create_text("N", tbl, parent=t_row, fontSize=11, fill=TEXT_PRIMARY)
    create_text("S", f"{sz} ({rows})", parent=t_row, fontSize=11, fill=WARNING_YELLOW)

# Card 2: Missing FK Indexes
c2_perf = create_frame("Missing FK Indexes", parent=p6_grid, width=440, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 20, "layout": "vertical", "gap": 8, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "⚠️ Missing Indexes on Foreign Keys (59 Found)", parent=c2_perf, fontSize=15, fill=CRITICAL_RED)
create_text("Sub", "Foreign keys lacking dedicated B-tree indexes cause sequential scans on deletes and joins.", parent=c2_perf, fontSize=11, fill=TEXT_SECONDARY)
for fk_col, tgt in [
    ("automation_waiting_events.automation_id", "automations.id"),
    ("billing_addon_orders.addon_id", "billing_addons.id"),
    ("campaign_run_audience.organization_id", "organizations.id"),
    ("automations.user_id", "users.id"),
    ("billing_dodo_snapshots.organization_id", "organizations.id"),
    ("billing_fulfilled_payments.organization_id", "organizations.id"),
    ("billing_payment_ledger.plan_id", "plans.id")
]:
    mfk_row = create_frame("MFK Row", parent=c2_perf, props={"fill": SURFACE_COLOR, "cornerRadius": 6, "padding": 7, "layout": "vertical", "sizingH": "fill", "sizingV": "hug"})
    create_text("Col", f"• {fk_col}", parent=mfk_row, fontSize=11, fill=TEXT_PRIMARY)
    create_text("Tgt", f"   -> references {tgt}", parent=mfk_row, fontSize=10, fill=ACCENT_BLUE)

# Card 3: Optimization Plan
c3_perf = create_frame("Perf Plan", parent=p6_grid, width=440, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 20, "layout": "vertical", "gap": 10, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🚀 Performance Optimization Plan", parent=c3_perf, fontSize=16, fill=SUCCESS_GREEN)
create_text("Notes",
    "1. Index Unindexed Foreign Keys [HIGH]:\n"
    "   Adding indexes on high-frequency tables (e.g. campaign_run_audience, automation_events) prevents full sequential scans during cascading deletes.\n\n"
    "2. Log Table Archiving / Retention [MEDIUM]:\n"
    "   ses_event_log and api_key_request_logs account for >40% of database storage despite low row counts. Implement a 30-day or 90-day retention partition.\n\n"
    "3. Autovacuum Tuning [LOW]:\n"
    "   Dead tuple accumulation is normal on event queue tables (ses_event_inbox). Ensure autovacuum_vacuum_scale_factor is set to 0.05 for queue tables.",
    parent=c3_perf, fontSize=12, fill=TEXT_SECONDARY
)

# ==============================================================================
# PAGE 7: SECURITY AND RLS VISUALIZATION
# ==============================================================================
print("Generating Page 7: Security & RLS...")
run_cmd("page.add", {"name": "7. Security & RLS Visualization"})
run_cmd("page.setBackground", {"color": BG_COLOR})

p7_root = setup_page_header(
    "Security & Row Level Security (RLS) Audit",
    "Audit of 104 RLS-enabled public tables, 219 active policies, and 33 service-role boundaries",
    7
)

p7_grid = create_frame("Security Grid", parent=p7_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

# Card 1: Posture
c1_sec = create_frame("Posture", parent=p7_grid, width=440, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 20, "layout": "vertical", "gap": 12, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🛡️ Row Level Security Posture", parent=c1_sec, fontSize=16, fill=SUCCESS_GREEN)
create_text("Desc",
    "• 100% RLS Adoption:\n"
    "  All 104 base tables in the public schema have Row Level Security enabled (rls_enabled: true). Zero tables have open, unmanaged public access.\n\n"
    "• 219 Defined RLS Policies:\n"
    "  Fine-grained access control using auth.uid() and organization_id tenancy checks.\n\n"
    "• 33 Service-Role Locked Tables:\n"
    "  Tables with RLS enabled but 0 client-facing policies. These are entirely shielded from the Supabase Data API and accessible only via trusted backend workers.\n\n"
    "• 28 Public / Anon Policies:\n"
    "  Permits unauthenticated read access to public marketing assets (blog posts, authors, public pricing plans, newsletter signups).",
    parent=c1_sec, fontSize=12, fill=TEXT_SECONDARY
)

# Card 2: Service Role
c2_sec = create_frame("Service Role Tables", parent=p7_grid, width=440, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 20, "layout": "vertical", "gap": 8, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🔒 Service-Role Isolated Tables (33)", parent=c2_sec, fontSize=16, fill=ACCENT_BLUE)
create_text("Sub", "Strict backend isolation: zero policies exist, blocking direct PostgREST client queries.", parent=c2_sec, fontSize=11, fill=TEXT_SECONDARY)
for s_tbl in [
    "billing_payment_ledger", "billing_addon_orders", "billing_fulfilled_payments",
    "billing_webhook_inbox", "billing_dodo_snapshots", "account_lifecycle_state",
    "account_lifecycle_policy", "account_lifecycle_deletions", "campaign_run_audience"
]:
    s_row = create_frame("SRow", parent=c2_sec, props={"fill": SURFACE_COLOR, "cornerRadius": 6, "padding": 7, "layout": "horizontal", "sizingH": "fill", "sizingV": "hug"})
    create_text("T", f"• {s_tbl}", parent=s_row, fontSize=11, fill=TEXT_PRIMARY)

# Card 3: Security Recs
c3_sec = create_frame("Security Recs", parent=p7_grid, width=440, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 20, "layout": "vertical", "gap": 10, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🔍 Security Recommendations", parent=c3_sec, fontSize=16, fill=PURPLE_ACCENT)
create_text("Recs",
    "1. Regular Policy Audit on Blog & Public Endpoints:\n"
    "   Ensure blog_posts and newsletter_subscribers policies do not accidentally expose draft or subscriber PII to 'anon'.\n\n"
    "2. Explicit Documentation of Service-Role Tables:\n"
    "   Document the 33 service-role tables in code repository documentation to prevent frontend developers from attempting direct client reads.\n\n"
    "3. Storage Object RLS Alignment:\n"
    "   Confirm that storage.objects policies reflect the organization-scoped access model used in public tables.",
    parent=c3_sec, fontSize=12, fill=TEXT_SECONDARY
)

# ==============================================================================
# PAGE 8: DATABASE HEALTH AND RECOMMENDATIONS
# ==============================================================================
print("Generating Page 8: Health & Recommendations...")
run_cmd("page.add", {"name": "8. Health & Recommendations"})
run_cmd("page.setBackground", {"color": BG_COLOR})

p8_root = setup_page_header(
    "Database Health Score & Prioritized Action Plan",
    "Comprehensive architectural evaluation and implementation roadmap for mailofly",
    8
)

p8_grid = create_frame("Health Grid", parent=p8_root, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

# Card 1: Score
c1_hlth = create_frame("Score Card", parent=p8_grid, width=440, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 24, "layout": "vertical", "gap": 12, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🏆 Database Health Rating", parent=c1_hlth, fontSize=18, fill=SUCCESS_GREEN)
create_text("Score", "88 / 100", parent=c1_hlth, fontSize=48, fill=SUCCESS_GREEN)
create_text("Grade", "GRADE: A- (Production Ready, Solid Security)", parent=c1_hlth, fontSize=13, fill=TEXT_PRIMARY)
create_text("Summary",
    "Strengths:\n"
    "• 100% RLS compliance on all public tables.\n"
    "• Clear multi-tenant relational hierarchy with organization_id.\n"
    "• 215 properly declared foreign keys.\n\n"
    "Areas for Improvement:\n"
    "• 59 foreign keys missing indexes.\n"
    "• Heavy log table bloat on email and SES webhook tables.\n"
    "• 1 orphaned table missing primary key (test_apply).",
    parent=c1_hlth, fontSize=12, fill=TEXT_SECONDARY
)

# Card 2: Action Items
c2_hlth = create_frame("Findings", parent=p8_grid, width=440, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 20, "layout": "vertical", "gap": 8, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "📋 Actionable Findings", parent=c2_hlth, fontSize=16, fill=WARNING_YELLOW)
for sev, title, action in [
    ("HIGH", "Index 59 Foreign Key Columns", "Run migration adding indexes on unindexed FKs to avoid join scans."),
    ("MEDIUM", "SES Event Log Retention", "Implement archival/partitioning on ses_event_log (11.4MB)."),
    ("LOW", "Remove test_apply Table", "Clean up the orphaned test_apply table which has no PK."),
    ("INFO", "Service-Role Table Inventory", "Document the 33 backend-only tables for frontend teams.")
]:
    col = CRITICAL_RED if sev == "HIGH" else (WARNING_YELLOW if sev == "MEDIUM" else (ACCENT_BLUE if sev == "LOW" else TEXT_SECONDARY))
    f_row = create_frame("FRow", parent=c2_hlth, props={"fill": SURFACE_COLOR, "cornerRadius": 6, "padding": 8, "layout": "vertical", "gap": 2, "sizingH": "fill", "sizingV": "hug"})
    create_text("T", f"[{sev}] {title}", parent=f_row, fontSize=12, fill=col)
    create_text("A", action, parent=f_row, fontSize=10, fill=TEXT_SECONDARY)

# Card 3: Roadmap
c3_hlth = create_frame("Roadmap", parent=p8_grid, width=440, props={"fill": CARD_BG, "cornerRadius": 14, "padding": 20, "layout": "vertical", "gap": 10, "stroke": CARD_BORDER, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🗺️ Suggested Optimization Roadmap", parent=c3_hlth, fontSize=16, fill=ACCENT_BLUE)
create_text("Roadmap",
    "Phase 1: Immediate Wins (Week 1)\n"
    "• Create B-tree indexes on high-traffic FKs: automation_waiting_events, campaign_run_audience, billing_addon_orders.\n"
    "• Drop or migrate `public.test_apply`.\n\n"
    "Phase 2: Data Lifecycle (Month 1)\n"
    "• Establish automated 90-day retention policies on `ses_event_log` and `api_key_request_logs`.\n"
    "• Evaluate table partitioning for `public.emails` as row volume grows.\n\n"
    "Phase 3: Continuous Monitoring (Ongoing)\n"
    "• Enable and monitor `pg_stat_statements` for slow query tracking.\n"
    "• Perform monthly RLS policy audits on new tables.",
    parent=c3_hlth, fontSize=12, fill=TEXT_SECONDARY
)

# ==============================================================================
# SAVE DOCUMENT
# ==============================================================================
print("Saving complete FigCraft architecture document...")
save_path = "c:\\projects\\maiofly_test\\supabase_docs\\mailofly_database_architecture.figcraft"
save_res = call_tool("save_file", {"path": save_path})
print("Saved document:", save_res)

# Select Page 1 and render a screenshot preview
print("Rendering preview screenshot...")
run_cmd("page.select", {"index": 0})
shot_res = call_tool("screenshot", {"scale": 1.5, "maxSize": 1600})
print("Screenshot result:", shot_res)

p.terminate()
print("Execution complete! Finished successfully.")
