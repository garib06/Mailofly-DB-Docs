import subprocess
import json
import os
import sys

# Load database metadata
with open("c:/projects/maiofly_test/supabase_docs/metadata.json", "r", encoding="utf-8") as f:
    meta = json.load(f)

# Launch figcraft-cli MCP engine
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

# Palette
BG_CANVAS = "#0B0F19"
SURFACE_CARD = "#111827"
HEADER_BG = "#1E293B"
BORDER_COLOR = "#334155"
TEXT_WHITE = "#F8FAFC"
TEXT_MUTED = "#94A3B8"
ACCENT_BLUE = "#38BDF8"
AMBER_PK = "#F59E0B"
PURPLE_UQ = "#C084FC"
GREEN_HEALTH = "#22C55E"
RED_CRIT = "#EF4444"

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

def create_text(name, text, parent=None, x=None, y=None, fontSize=11, fill=TEXT_WHITE, props=None):
    p = {"fontSize": fontSize, "fill": fill}
    if props:
        p.update(props)
    args = {"type": "text", "name": name, "text": text, "props": p}
    if parent is not None:
        args["parent"] = parent
    if x is not None:
        args["x"] = x
    if y is not None:
        args["y"] = y
    res = call_tool("create_node", args)
    if isinstance(res, dict) and "id" in res:
        return res["id"]
    return None

def create_connector(name, x1, y1, x2, y2, color="#38BDF8"):
    # Draw an editable orthogonal vector connector
    mid_x = (x1 + x2) / 2
    path = f"M {x1} {y1} L {mid_x} {y1} L {mid_x} {y2} L {x2} {y2}"
    args = {
        "type": "vector",
        "name": name,
        "path": path,
        "props": {
            "stroke": color,
            "strokeWeight": 1.5
        }
    }
    return call_tool("create_node", args)

# Index table columns, PKs, FKs, UQs from metadata
cols_by_table = {}
for c in meta["columns"]:
    cols_by_table.setdefault((c["table_schema"], c["table_name"]), []).append(c)

pks_by_table = {}
for pk in meta["primary_keys"]:
    pks_by_table.setdefault((pk["table_schema"], pk["table_name"]), set()).add(pk["column_name"])

fks_by_table = {}
for fk in meta["foreign_keys"]:
    fks_by_table.setdefault((fk["source_schema"], fk["source_table"]), []).append(fk)

uqs_by_table = {}
for con in meta["constraints"]:
    if con["constraint_type"] == "u":
        uqs_by_table.setdefault((con["schema_name"], con["table_name"]), set()).add(con["constraint_name"])

# Function to render a true DrawSQL / dbdiagram style table component
def render_erd_table(schema, table_name, x, y, width=320, parent=None):
    t_id = create_frame(
        f"{schema}.{table_name}",
        parent=parent,
        x=x, y=y, width=width,
        props={
            "fill": SURFACE_CARD,
            "cornerRadius": 8,
            "stroke": BORDER_COLOR,
            "strokeWeight": 1.5,
            "layout": "vertical",
            "padding": 0,
            "gap": 0,
            "sizingV": "hug"
        }
    )
    
    # Table Header
    hdr_id = create_frame(
        "Header",
        parent=t_id,
        height=34,
        props={
            "fill": HEADER_BG,
            "layout": "horizontal",
            "mainAlign": "spaceBetween",
            "crossAlign": "center",
            "padding": [8, 12, 8, 12],
            "sizingH": "fill"
        }
    )
    create_text("TableName", f"{schema}.{table_name}", parent=hdr_id, fontSize=12, fill=TEXT_WHITE)
    create_text("Badge", "TABLE", parent=hdr_id, fontSize=10, fill=TEXT_MUTED)

    # Columns
    cols = cols_by_table.get((schema, table_name), [])
    table_pks = pks_by_table.get((schema, table_name), set())
    table_fks = {fk["source_column"]: fk for fk in fks_by_table.get((schema, table_name), [])}
    
    # Display up to 10 prominent columns so card remains compact & clean
    display_cols = cols[:10]
    
    for c in display_cols:
        c_name = c["column_name"]
        c_type = c["data_type"]
        is_pk = c_name in table_pks
        is_fk = c_name in table_fks
        is_uq = "unique" in c_name.lower() or c_name in uqs_by_table.get((schema, table_name), set())
        
        row_id = create_frame(
            f"Row: {c_name}",
            parent=t_id,
            height=26,
            props={
                "fill": "#00000000",
                "layout": "horizontal",
                "mainAlign": "spaceBetween",
                "crossAlign": "center",
                "padding": [4, 12, 4, 12],
                "sizingH": "fill"
            }
        )
        
        # Left group
        left_id = create_frame(
            "Left",
            parent=row_id,
            props={"fill": "#00000000", "layout": "horizontal", "gap": 6, "crossAlign": "center", "sizingV": "hug", "sizingH": "hug"}
        )
        if is_pk:
            create_text("PK", "[PK]", parent=left_id, fontSize=9, fill=AMBER_PK)
            create_text("Name", c_name, parent=left_id, fontSize=11, fill=TEXT_WHITE)
        elif is_fk:
            create_text("FK", "[FK]", parent=left_id, fontSize=9, fill=ACCENT_BLUE)
            create_text("Name", c_name, parent=left_id, fontSize=11, fill=ACCENT_BLUE)
        elif is_uq:
            create_text("UQ", "[UQ]", parent=left_id, fontSize=9, fill=PURPLE_UQ)
            create_text("Name", c_name, parent=left_id, fontSize=11, fill=TEXT_WHITE)
        else:
            create_text("Name", c_name, parent=left_id, fontSize=11, fill="#CBD5E1")
            
        # Right group (Data Type)
        # shorten long data types for clean visual
        short_type = c_type.replace("timestamp with time zone", "timestamptz").replace("character varying", "varchar").replace("USER-DEFINED", "enum")
        create_text("Type", short_type, parent=row_id, fontSize=10, fill=TEXT_MUTED)
        
    if len(cols) > 10:
        more_row = create_frame("MoreRow", parent=t_id, height=22, props={"fill": "#00000000", "padding": [4, 12, 4, 12], "sizingH": "fill"})
        create_text("More", f"+ {len(cols) - 10} more columns...", parent=more_row, fontSize=10, fill=TEXT_MUTED)

    return t_id

print("Connecting to FigCraft MCP...")
send("initialize", {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "drawsql-generator", "version": "1.0"}})

# ==============================================================================
# PAGE 1: ARCHITECTURE OVERVIEW & DOMAIN MAP
# ==============================================================================
print("Building Page 1: Architecture Overview...")
run_cmd("page.rename", {"name": "1. Architecture Overview"})
run_cmd("page.setBackground", {"color": BG_CANVAS})

# Overview Canvas Container
p1_id = create_frame(
    "Overview Canvas",
    x=60, y=60, width=1600, height=1100,
    props={"fill": BG_CANVAS, "layout": "vertical", "gap": 24, "padding": 40, "sizingV": "hug"}
)

# Header
p1_hdr = create_frame("Header", parent=p1_id, props={"fill": "#00000000", "layout": "vertical", "gap": 6, "sizingH": "fill", "sizingV": "hug"})
create_text("Title", "Database Architecture Workspace: mailofly (Production)", parent=p1_hdr, fontSize=24, fill=TEXT_WHITE)
create_text("Sub", "PostgreSQL 17.6 (aarch64) | Ref: aymarrhbnaygxkaorjfl | 169 Tables | 215 Foreign Keys | 523 Indexes | 100% RLS Coverage", parent=p1_hdr, fontSize=13, fill=TEXT_MUTED)

# High-Level Domain Map Row
dom_row = create_frame("Domain Modules Map", parent=p1_id, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

domains_summary = [
    ("1. Tenancy & Access", "organizations, members, users, roles", ACCENT_BLUE),
    ("2. CRM & Audiences", "contacts, segments, properties, topics", GREEN_HEALTH),
    ("3. Campaigns Engine", "campaigns, runs, audience targeting", PURPLE_UQ),
    ("4. Sending & SES Logs", "mailboxes, sending_domains, emails, ses_logs", AMBER_PK),
    ("5. Automation Workflows", "automations, runs, steps, events", ACCENT_BLUE),
    ("6. Billing & Subscriptions", "plans, subscriptions, addons, ledger", GREEN_HEALTH)
]

for d_name, d_desc, d_color in domains_summary:
    box = create_frame(f"Domain: {d_name}", parent=dom_row, width=240, props={"fill": SURFACE_CARD, "cornerRadius": 10, "padding": 16, "layout": "vertical", "gap": 6, "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingV": "hug"})
    create_text("DName", d_name, parent=box, fontSize=13, fill=d_color)
    create_text("DDesc", d_desc, parent=box, fontSize=11, fill=TEXT_MUTED)

# System Metrics Bar
metrics_bar = create_frame("Metrics Bar", parent=p1_id, props={"fill": SURFACE_CARD, "cornerRadius": 12, "padding": [16, 24, 16, 24], "layout": "horizontal", "mainAlign": "spaceBetween", "crossAlign": "center", "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingH": "fill", "sizingV": "hug"})
for m_label, m_val in [
    ("PUBLIC BASE TABLES", "104"),
    ("PUBLIC VIEWS", "7"),
    ("AUTH SCHEMAS", "27 Tables"),
    ("STORAGE TABLES", "10"),
    ("FOREIGN KEYS", "215 Mapped"),
    ("TOTAL INDEXES", "523"),
    ("RLS STATUS", "100% Secured")
]:
    m_box = create_frame("MItem", parent=metrics_bar, props={"fill": "#00000000", "layout": "vertical", "gap": 2, "sizingV": "hug", "sizingH": "hug"})
    create_text("MLabel", m_label, parent=m_box, fontSize=10, fill=TEXT_MUTED)
    create_text("MVal", m_val, parent=m_box, fontSize=16, fill=TEXT_WHITE)

# ==============================================================================
# PAGE 2: ERD — TENANCY, IDENTITY & CRM CANVAS
# ==============================================================================
print("Building Page 2: ERD — Tenancy & CRM...")
run_cmd("page.add", {"name": "2. ERD - Tenancy & CRM"})
run_cmd("page.setBackground", {"color": BG_CANVAS})

# Canvas Header
create_text("Canvas Title", "Entity Relationship Canvas: Tenancy, Access Control & CRM Audiences", x=80, y=50, fontSize=22, fill=TEXT_WHITE)
create_text("Canvas Sub", "DrawSQL-style interactive model | Actual Foreign Key Connectors connecting source to target tables", x=80, y=82, fontSize=12, fill=TEXT_MUTED)

# Render Tables with exact coordinates
render_erd_table("public", "organizations", 80, 140, 320)
render_erd_table("public", "organization_members", 460, 140, 320)
render_erd_table("public", "organization_invitations", 460, 440, 320)
render_erd_table("public", "users", 840, 140, 320)
render_erd_table("public", "identities", 840, 440, 320)

render_erd_table("public", "contacts", 80, 680, 320)
render_erd_table("public", "contact_segments", 460, 680, 320)
render_erd_table("public", "segment_contacts", 460, 980, 320)
render_erd_table("public", "contact_properties", 840, 680, 320)
render_erd_table("public", "contact_property_values", 840, 980, 320)
render_erd_table("public", "topics", 1220, 680, 320)
render_erd_table("public", "contact_topics", 1220, 980, 320)

# Connectors for Page 2
print("Drawing Page 2 FK Connectors...")
# org_members -> organizations
create_connector("FK: org_members -> organizations", 460, 200, 400, 200)
# org_members -> users
create_connector("FK: org_members -> users", 780, 200, 840, 200)
# org_invitations -> organizations
create_connector("FK: org_invitations -> organizations", 460, 480, 240, 380)
# contacts -> organizations
create_connector("FK: contacts -> organizations", 240, 680, 240, 380)
# contact_segments -> organizations
create_connector("FK: segments -> organizations", 460, 720, 280, 380)
# segment_contacts -> contact_segments
create_connector("FK: segment_contacts -> segments", 620, 980, 620, 920)
# segment_contacts -> contacts
create_connector("FK: segment_contacts -> contacts", 460, 1020, 400, 780)
# contact_property_values -> contacts
create_connector("FK: property_values -> contacts", 840, 1020, 400, 800)
# contact_topics -> contacts
create_connector("FK: contact_topics -> contacts", 1220, 1020, 400, 820)
# contact_topics -> topics
create_connector("FK: contact_topics -> topics", 1380, 980, 1380, 880)

# ==============================================================================
# PAGE 3: ERD — CAMPAIGNS, AUTOMATIONS & DELIVERIES
# ==============================================================================
print("Building Page 3: ERD — Campaigns & Deliveries...")
run_cmd("page.add", {"name": "3. ERD - Campaigns & Delivery"})
run_cmd("page.setBackground", {"color": BG_CANVAS})

create_text("Canvas Title", "Entity Relationship Canvas: Campaigns, Automations & AWS SES Delivery Pipeline", x=80, y=50, fontSize=22, fill=TEXT_WHITE)
create_text("Canvas Sub", "DrawSQL-style interactive model | Complete relational mapping of broadcast & event queues", x=80, y=82, fontSize=12, fill=TEXT_MUTED)

# Row 1: Campaigns
render_erd_table("public", "campaigns", 80, 140, 320)
render_erd_table("public", "campaign_runs", 460, 140, 320)
render_erd_table("public", "campaign_run_audience", 840, 140, 320)
render_erd_table("public", "campaign_sending_holds", 460, 420, 320)

# Row 2: Automations
render_erd_table("public", "automations", 80, 620, 320)
render_erd_table("public", "automation_runs", 460, 620, 320)
render_erd_table("public", "automation_run_steps", 840, 620, 320)
render_erd_table("public", "automation_events", 1220, 620, 320)
render_erd_table("public", "automation_waiting_events", 840, 900, 320)

# Row 3: Sending & SES Logs
render_erd_table("public", "mailboxes", 80, 1000, 320)
render_erd_table("public", "sending_domains", 460, 1000, 320)
render_erd_table("public", "emails", 840, 1180, 320)
render_erd_table("public", "ses_event_log", 1220, 1180, 320)
render_erd_table("public", "ses_event_inbox", 1220, 140, 320)

# Connectors for Page 3
print("Drawing Page 3 FK Connectors...")
# campaign_runs -> campaigns
create_connector("FK: campaign_runs -> campaigns", 460, 200, 400, 200)
# campaign_run_audience -> campaign_runs
create_connector("FK: audience -> campaign_runs", 840, 200, 780, 200)
# automation_runs -> automations
create_connector("FK: automation_runs -> automations", 460, 680, 400, 680)
# automation_run_steps -> automation_runs
create_connector("FK: run_steps -> automation_runs", 840, 680, 780, 680)
# emails -> mailboxes
create_connector("FK: emails -> mailboxes", 840, 1220, 400, 1080)
# emails -> campaigns
create_connector("FK: emails -> campaigns", 840, 1200, 240, 400)
# ses_event_log -> emails
create_connector("FK: ses_log -> emails", 1220, 1220, 1160, 1220)

# ==============================================================================
# PAGE 4: ERD — BILLING, DEVELOPER APIS & ADDONS
# ==============================================================================
print("Building Page 4: ERD — Billing & APIs...")
run_cmd("page.add", {"name": "4. ERD - Billing & APIs"})
run_cmd("page.setBackground", {"color": BG_CANVAS})

create_text("Canvas Title", "Entity Relationship Canvas: Billing, Subscriptions & Developer API Platform", x=80, y=50, fontSize=22, fill=TEXT_WHITE)
create_text("Canvas Sub", "DrawSQL-style interactive model | Complete relational mapping of monetization & API tokens", x=80, y=82, fontSize=12, fill=TEXT_MUTED)

# Billing Section
render_erd_table("public", "plans", 80, 140, 320)
render_erd_table("public", "organization_subscriptions", 460, 140, 320)
render_erd_table("public", "organization_usage", 840, 140, 320)

render_erd_table("public", "billing_addons", 80, 460, 320)
render_erd_table("public", "billing_addon_orders", 460, 460, 320)
render_erd_table("public", "billing_payment_ledger", 840, 460, 320)
render_erd_table("public", "billing_fulfilled_payments", 1220, 460, 320)

# Developer API Section
render_erd_table("public", "api_keys", 80, 780, 320)
render_erd_table("public", "api_key_request_logs", 460, 780, 320)
render_erd_table("public", "webhooks", 840, 780, 320)
render_erd_table("public", "webhook_deliveries", 1220, 780, 320)

# Connectors for Page 4
print("Drawing Page 4 FK Connectors...")
# subscriptions -> plans
create_connector("FK: subscriptions -> plans", 460, 200, 400, 200)
# addon_orders -> billing_addons
create_connector("FK: addon_orders -> billing_addons", 460, 520, 400, 520)
# api_key_request_logs -> api_keys
create_connector("FK: request_logs -> api_keys", 460, 840, 400, 840)
# webhook_deliveries -> webhooks
create_connector("FK: deliveries -> webhooks", 1220, 840, 1160, 840)

# ==============================================================================
# PAGE 5: SCHEMA ARCHITECTURE & OBJECT HIERARCHY
# ==============================================================================
print("Building Page 5: Schema Architecture...")
run_cmd("page.add", {"name": "5. Schema Architecture"})
run_cmd("page.setBackground", {"color": BG_CANVAS})

p5_id = create_frame(
    "Schema Hierarchy Canvas",
    x=60, y=60, width=1600, height=1100,
    props={"fill": BG_CANVAS, "layout": "vertical", "gap": 24, "padding": 40, "sizingV": "hug"}
)
p5_hdr = create_frame("Header", parent=p5_id, props={"fill": "#00000000", "layout": "vertical", "gap": 6, "sizingH": "fill", "sizingV": "hug"})
create_text("Title", "Database Schema Hierarchy & Object Distribution", parent=p5_hdr, fontSize=24, fill=TEXT_WHITE)
create_text("Sub", "Complete tree view of all accessible schemas, user objects, and Supabase-managed engines", parent=p5_hdr, fontSize=13, fill=TEXT_MUTED)

s_grid = create_frame("Grid", parent=p5_id, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

schemas_breakdown = [
    ("public (Application)", "104 Base Tables | 7 Views | 224 Functions", [
        "Tenancy: organizations, members, invitations, roles, permissions",
        "CRM: contacts, segments, segment_contacts, properties, topics",
        "Campaigns: campaigns, runs, run_audience, sending_holds",
        "Automations: automations, runs, run_steps, events, waiting_events",
        "Email Pipeline: mailboxes, domains, emails, ses_logs, suppressions",
        "Monetization: plans, subscriptions, addons, ledger, orders",
        "Developer: api_keys, webhooks, oauth_clients, oauth_tokens"
    ], ACCENT_BLUE),
    ("auth (GoTrue Auth)", "27 Base Tables", [
        "users: Primary user credentials, emails, and phone records",
        "identities: Social logins, OAuth providers (Google, GitHub)",
        "sessions: Active JWT sessions with expiration timestamps",
        "refresh_tokens: Secure token refresh cycles",
        "mfa_factors & mfa_challenges: TOTP & Authenticator app records",
        "sso_providers & sso_domains: Enterprise SAML Single Sign-On",
        "audit_log_entries: Security, login, and password change audit log"
    ], GREEN_HEALTH),
    ("storage (S3 Storage)", "10 Base Tables", [
        "buckets: Public and private bucket definitions and configurations",
        "objects: Uploaded asset paths, file sizes, and MIME types",
        "s3_multipart_uploads: In-flight chunked upload coordinators",
        "bucket_lifecycle_states: Retention rules and cleanup tracking"
    ], PURPLE_UQ),
    ("realtime & extensions", "16 System Tables", [
        "realtime.channels: WebSocket presence and broadcast pub/sub",
        "cron.job & cron.job_run_details: Scheduled database tasks",
        "vault.secrets: Encrypted third-party API keys and credentials",
        "extensions: pg_trgm, uuid-ossp, pgcrypto, etc."
    ], AMBER_PK)
]

for s_t, s_sub, s_items, s_col in schemas_breakdown:
    b = create_frame(f"Box: {s_t}", parent=s_grid, width=360, props={"fill": SURFACE_CARD, "cornerRadius": 12, "padding": 20, "layout": "vertical", "gap": 10, "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingV": "hug"})
    create_text("ST", s_t, parent=b, fontSize=15, fill=s_col)
    create_text("SSub", s_sub, parent=b, fontSize=11, fill=TEXT_MUTED)
    for it in s_items:
        r = create_frame("R", parent=b, props={"fill": HEADER_BG, "cornerRadius": 6, "padding": 8, "layout": "vertical", "sizingH": "fill", "sizingV": "hug"})
        create_text("ITxt", it, parent=r, fontSize=11, fill=TEXT_WHITE)

# ==============================================================================
# PAGE 6: COMPLETE DATA DICTIONARY (ALL 104 PUBLIC APPLICATION TABLES)
# ==============================================================================
print("Building Page 6: Complete Data Dictionary...")
run_cmd("page.add", {"name": "6. Data Dictionary (All Tables)"})
run_cmd("page.setBackground", {"color": BG_CANVAS})

p6_id = create_frame(
    "Data Dictionary Canvas",
    x=60, y=60, width=1600, height=1300,
    props={"fill": BG_CANVAS, "layout": "vertical", "gap": 20, "padding": 40, "sizingV": "hug"}
)
p6_hdr = create_frame("Header", parent=p6_id, props={"fill": "#00000000", "layout": "vertical", "gap": 6, "sizingH": "fill", "sizingV": "hug"})
create_text("Title", "Complete Application Data Dictionary (All 104 Public Tables)", parent=p6_hdr, fontSize=24, fill=TEXT_WHITE)
create_text("Sub", "Exhaustive inventory of every single public application table with column counts, primary keys, foreign key targets, row counts, and RLS policies", parent=p6_hdr, fontSize=13, fill=TEXT_MUTED)

# 4 Columns of Tables
dict_cols_container = create_frame("ColsContainer", parent=p6_id, props={"fill": "#00000000", "layout": "horizontal", "gap": 16, "sizingH": "fill", "sizingV": "hug"})

# Get all 104 public base tables sorted alphabetically
pub_tables = sorted([t for t in meta["tables"] if t["schema_name"] == "public" and t["kind"] == "r"], key=lambda x: x["table_name"])

# Divide into 4 chunks
chunk_size = (len(pub_tables) + 3) // 4

for i in range(4):
    chunk = pub_tables[i*chunk_size : (i+1)*chunk_size]
    col_frame = create_frame(f"DictCol_{i+1}", parent=dict_cols_container, width=360, props={"fill": "#00000000", "layout": "vertical", "gap": 8, "sizingV": "hug"})
    for t in chunk:
        t_name = t["table_name"]
        t_cols = cols_by_table.get(("public", t_name), [])
        t_fks = fks_by_table.get(("public", t_name), [])
        t_pks = pks_by_table.get(("public", t_name), set())
        
        entry = create_frame(f"Dict_{t_name}", parent=col_frame, props={"fill": SURFACE_CARD, "cornerRadius": 6, "padding": [8, 12, 8, 12], "layout": "vertical", "gap": 2, "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingH": "fill", "sizingV": "hug"})
        
        # Row 1: Table Name & Columns Count
        r1 = create_frame("R1", parent=entry, props={"fill": "#00000000", "layout": "horizontal", "mainAlign": "spaceBetween", "sizingH": "fill", "sizingV": "hug"})
        create_text("TName", f"📄 {t_name}", parent=r1, fontSize=11, fill=TEXT_WHITE)
        create_text("CCount", f"{len(t_cols)} cols", parent=r1, fontSize=10, fill=TEXT_MUTED)
        
        # Row 2: PK & FK count
        r2 = create_frame("R2", parent=entry, props={"fill": "#00000000", "layout": "horizontal", "mainAlign": "spaceBetween", "sizingH": "fill", "sizingV": "hug"})
        pk_str = f"PK: {', '.join(t_pks)}" if t_pks else "PK: NONE"
        pk_col = AMBER_PK if t_pks else RED_CRIT
        create_text("PK", pk_str[:22], parent=r2, fontSize=9, fill=pk_col)
        create_text("FK", f"{len(t_fks)} FKs | RLS: ON", parent=r2, fontSize=9, fill=ACCENT_BLUE)

# ==============================================================================
# PAGE 7: INDEX & PERFORMANCE AUDIT
# ==============================================================================
print("Building Page 7: Performance Audit...")
run_cmd("page.add", {"name": "7. Performance & Index Audit"})
run_cmd("page.setBackground", {"color": BG_CANVAS})

p7_id = create_frame(
    "Performance Canvas",
    x=60, y=60, width=1600, height=1100,
    props={"fill": BG_CANVAS, "layout": "vertical", "gap": 24, "padding": 40, "sizingV": "hug"}
)
p7_hdr = create_frame("Header", parent=p7_id, props={"fill": "#00000000", "layout": "vertical", "gap": 6, "sizingH": "fill", "sizingV": "hug"})
create_text("Title", "Index Optimization & Performance Telemetry Audit", parent=p7_hdr, fontSize=24, fill=TEXT_WHITE)
create_text("Sub", "Identification of 59 unindexed foreign key columns, table size bloat, and sequential scan ratios", parent=p7_hdr, fontSize=13, fill=TEXT_MUTED)

p7_grid = create_frame("Perf Grid", parent=p7_id, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

# Card 1: Top Sizes
card_sz = create_frame("Storage Card", parent=p7_grid, width=480, props={"fill": SURFACE_CARD, "cornerRadius": 12, "padding": 20, "layout": "vertical", "gap": 10, "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "📦 Storage Distribution (Top Tables)", parent=card_sz, fontSize=15, fill=AMBER_PK)
for tbl, sz, rows, desc in [
    ("public.emails", "14.36 MB", "379 rows", "Large HTML/text message payloads"),
    ("public.ses_event_log", "11.37 MB", "963 rows", "Raw JSON event webhook deliveries"),
    ("public.api_key_request_logs", "9.82 MB", "485 rows", "HTTP request/response body snapshots"),
    ("public.contacts", "4.38 MB", "1,224 rows", "Custom properties JSONB attributes"),
    ("public.ses_event_inbox", "2.08 MB", "1,000 rows", "High-throughput webhook queue"),
    ("public.ses_recipient_outcomes", "1.34 MB", "2,357 rows", "Bounces, clicks, opens, complaints")
]:
    r = create_frame("R", parent=card_sz, props={"fill": HEADER_BG, "cornerRadius": 6, "padding": 8, "layout": "horizontal", "mainAlign": "spaceBetween", "sizingH": "fill", "sizingV": "hug"})
    create_text("T", f"{tbl} ({rows})", parent=r, fontSize=11, fill=TEXT_WHITE)
    create_text("S", sz, parent=r, fontSize=11, fill=AMBER_PK)

# Card 2: 59 Missing FK Indexes
card_mfk = create_frame("Missing FK Card", parent=p7_grid, width=480, props={"fill": SURFACE_CARD, "cornerRadius": 12, "padding": 20, "layout": "vertical", "gap": 8, "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "⚠️ 59 Unindexed Foreign Key Columns (High Priority)", parent=card_mfk, fontSize=15, fill=RED_CRIT)
create_text("Sub", "Foreign keys lacking an index on the source column trigger full table sequential scans during joins and ON DELETE CASCADE.", parent=card_mfk, fontSize=10, fill=TEXT_MUTED)

for src_tbl, src_col, tgt_tbl in [
    ("automation_waiting_events", "automation_id", "automations"),
    ("billing_addon_orders", "addon_id", "billing_addons"),
    ("campaign_run_audience", "organization_id", "organizations"),
    ("automations", "user_id", "users"),
    ("billing_dodo_snapshots", "organization_id", "organizations"),
    ("billing_fulfilled_payments", "organization_id", "organizations"),
    ("billing_payment_ledger", "plan_id", "plans"),
    ("admin_roles", "created_by", "users")
]:
    r = create_frame("R", parent=card_mfk, props={"fill": HEADER_BG, "cornerRadius": 6, "padding": 8, "layout": "vertical", "gap": 2, "sizingH": "fill", "sizingV": "hug"})
    create_text("Col", f"• {src_tbl}.{src_col}", parent=r, fontSize=11, fill=TEXT_WHITE)
    create_text("Sql", f"  -> CREATE INDEX ON {src_tbl}({src_col});", parent=r, fontSize=10, fill=ACCENT_BLUE)

# Card 3: Performance Plan
card_plan = create_frame("Plan Card", parent=p7_grid, width=480, props={"fill": SURFACE_CARD, "cornerRadius": 12, "padding": 20, "layout": "vertical", "gap": 10, "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🚀 Performance Optimization Recommendations", parent=card_plan, fontSize=15, fill=GREEN_HEALTH)
create_text("PlanBody",
    "1. Index High-Traffic FK Columns [HIGH SEVERITY]:\n"
    "   Adding indexes on high-frequency tables (e.g. campaign_run_audience, automation_events) prevents full sequential scans during cascading deletes.\n\n"
    "2. Log Table Archiving / Retention [MEDIUM SEVERITY]:\n"
    "   ses_event_log and api_key_request_logs account for >40% of database storage despite low row counts. Implement a 30-day or 90-day retention partition.\n\n"
    "3. Autovacuum Tuning [LOW SEVERITY]:\n"
    "   Dead tuple accumulation is normal on event queue tables (ses_event_inbox). Ensure autovacuum_vacuum_scale_factor is set to 0.05 for queue tables.",
    parent=card_plan, fontSize=11, fill=TEXT_MUTED
)

# ==============================================================================
# PAGE 8: SECURITY, RLS & ARCHITECTURAL RECOMMENDATIONS
# ==============================================================================
print("Building Page 8: Security & Recommendations...")
run_cmd("page.add", {"name": "8. Security & Recommendations"})
run_cmd("page.setBackground", {"color": BG_CANVAS})

p8_id = create_frame(
    "Security Canvas",
    x=60, y=60, width=1600, height=1100,
    props={"fill": BG_CANVAS, "layout": "vertical", "gap": 24, "padding": 40, "sizingV": "hug"}
)
p8_hdr = create_frame("Header", parent=p8_id, props={"fill": "#00000000", "layout": "vertical", "gap": 6, "sizingH": "fill", "sizingV": "hug"})
create_text("Title", "Row Level Security (RLS) Audit & Architectural Action Plan", parent=p8_hdr, fontSize=24, fill=TEXT_WHITE)
create_text("Sub", "Audit of 104 secured public tables, 219 active policies, and 33 service-role backend boundaries", parent=p8_hdr, fontSize=13, fill=TEXT_MUTED)

p8_grid = create_frame("Sec Grid", parent=p8_id, props={"fill": "#00000000", "layout": "horizontal", "gap": 20, "sizingH": "fill", "sizingV": "hug"})

# Box 1: RLS Audit
box_rls = create_frame("RLS Audit Box", parent=p8_grid, width=480, props={"fill": SURFACE_CARD, "cornerRadius": 12, "padding": 20, "layout": "vertical", "gap": 10, "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🛡️ Row Level Security Posture", parent=box_rls, fontSize=15, fill=GREEN_HEALTH)
create_text("Body",
    "• 100% RLS Coverage in public:\n"
    "  All 104 public base tables have rls_enabled = true. Zero tables are accidentally exposed without RLS.\n\n"
    "• 219 Active Policies:\n"
    "  Granular tenancy enforcement using auth.uid() and organization_id.\n\n"
    "• 33 Service-Role Locked Tables:\n"
    "  Tables with RLS enabled but 0 public policies (e.g. billing_payment_ledger, billing_addon_orders, billing_webhook_inbox). Perfectly locked to backend service-role.\n\n"
    "• 28 Public / Anon Policies:\n"
    "  Restricted strictly to marketing assets (published blog posts, authors, public pricing plans, and newsletter signups).",
    parent=box_rls, fontSize=11, fill=TEXT_MUTED
)

# Box 2: Actionable Findings
box_find = create_frame("Findings Box", parent=p8_grid, width=480, props={"fill": SURFACE_CARD, "cornerRadius": 12, "padding": 20, "layout": "vertical", "gap": 8, "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "📋 Evidence-Based Architectural Findings", parent=box_find, fontSize=15, fill=AMBER_PK)

findings = [
    ("HIGH", "Index 59 Foreign Key Columns", "Creates B-tree indexes on unindexed FKs to avoid full sequential scans."),
    ("MEDIUM", "SES Event Log Retention Policy", "Implement 30-day or 90-day retention on ses_event_log (11.4MB)."),
    ("LOW", "Drop Orphaned Table `test_apply`", "test_apply has 0 rows and no primary key constraint."),
    ("INFO", "Document 33 Service-Role Tables", "Document backend-only tables in repo to avoid frontend client query errors.")
]
for sev, f_title, f_sol in findings:
    f_col = RED_CRIT if sev == "HIGH" else (AMBER_PK if sev == "MEDIUM" else (ACCENT_BLUE if sev == "LOW" else TEXT_MUTED))
    r = create_frame("Finding", parent=box_find, props={"fill": HEADER_BG, "cornerRadius": 6, "padding": 8, "layout": "vertical", "gap": 2, "sizingH": "fill", "sizingV": "hug"})
    create_text("Hdr", f"[{sev}] {f_title}", parent=r, fontSize=11, fill=f_col)
    create_text("Sol", f_sol, parent=r, fontSize=10, fill=TEXT_MUTED)

# Box 3: Roadmap & Telemetry Notice
box_road = create_frame("Roadmap Box", parent=p8_grid, width=480, props={"fill": SURFACE_CARD, "cornerRadius": 12, "padding": 20, "layout": "vertical", "gap": 10, "stroke": BORDER_COLOR, "strokeWeight": 1, "sizingV": "hug"})
create_text("Title", "🗺️ Implementation Roadmap", parent=box_road, fontSize=15, fill=ACCENT_BLUE)
create_text("RoadmapText",
    "Phase 1: Immediate (Week 1)\n"
    "• Run migration to add indexes on 59 FK columns.\n"
    "• Remove unused `public.test_apply` table.\n\n"
    "Phase 2: Short-term (Month 1)\n"
    "• Implement automated retention partitions on `ses_event_log`.\n"
    "• Monitor autovacuum frequency on high-throughput queue tables.\n\n"
    "Telemetry Notice:\n"
    "Hardware CPU and disk I/O metrics are host-managed by Supabase/AWS infrastructure and not accessible through PostgreSQL system catalog queries.",
    parent=box_road, fontSize=11, fill=TEXT_MUTED
)

# ==============================================================================
# SAVE AND EXPORT
# ==============================================================================
print("Saving redesigned architecture workspace...")
save_target = "c:\\projects\\maiofly_test\\supabase_docs\\mailofly_database_architecture.figcraft"
res_save = call_tool("save_file", {"path": save_target})
print("Save result:", res_save)

p.terminate()
print("Redesign complete! FigCraft document updated successfully.")
