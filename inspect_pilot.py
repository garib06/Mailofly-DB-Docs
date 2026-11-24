import json

with open("database-docs/source/tables.json", "r", encoding="utf-8") as f:
    tables = { (t["table_schema"], t["table_name"]): t for t in json.load(f)["data"] }

with open("database-docs/source/columns.json", "r", encoding="utf-8") as f:
    cols_list = json.load(f)["data"]

with open("database-docs/source/relationships.json", "r", encoding="utf-8") as f:
    fks_list = json.load(f)["data"]

with open("database-docs/source/constraints.json", "r", encoding="utf-8") as f:
    cons_list = json.load(f)["data"]

with open("database-docs/source/domains.json", "r", encoding="utf-8") as f:
    domains = json.load(f)["domains"]

pilot_tables = sorted(list(set(domains["tenancy_and_users"]["tables"] + domains["contacts_and_crm"]["tables"])))
print(f"Pilot tables count: {len(pilot_tables)}")
for t in pilot_tables:
    t_cols = [c for c in cols_list if c["table_schema"] == "public" and c["table_name"] == t]
    print(f"  - {t}: {len(t_cols)} columns")

pilot_fks = [fk for fk in fks_list if fk["source_schema"] == "public" and fk["source_table"] in pilot_tables]
print(f"\nPilot foreign keys count: {len(pilot_fks)}")
for fk in pilot_fks:
    print(f"  {fk['source_table']}.{fk['source_column']} -> {fk['target_schema']}.{fk['target_table']}.{fk['target_column']} [{fk['constraint_name']}] (ON DELETE: {fk['delete_action']}, ON UPDATE: {fk['update_action']})")
