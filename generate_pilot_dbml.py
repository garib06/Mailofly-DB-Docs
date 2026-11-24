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

# Generate DBML
dbml_lines = ["// Mailofly Pilot ERD: Tenancy & CRM Domains\n"]

pks_by_table = {}
for con in cons_list:
    key = (con["schema_name"], con["table_name"])
    if con["constraint_type"] == "p":
        pks_by_table.setdefault(key, set())
        m = con["constraint_definition"]
        if "(" in m and ")" in m:
            cols = m[m.index("(")+1:m.rindex(")")].split(",")
            for c in cols:
                pks_by_table[key].add(c.strip().replace('"', ''))

for tbl in pilot_tables:
    dbml_lines.append(f"Table public.{tbl} {{")
    t_cols = [c for c in cols_list if c["table_schema"] == "public" and c["table_name"] == tbl]
    t_pks = pks_by_table.get(("public", tbl), set())
    for col in t_cols:
        c_name = col["column_name"]
        c_type = col.get("data_type") or col.get("udt_name") or "text"
        flags = []
        if c_name in t_pks:
            flags.append("pk")
        if col.get("is_nullable") == "NO":
            flags.append("not null")
        if col.get("column_default"):
            clean_def = str(col["column_default"]).replace("'", "\\'")
            flags.append(f"default: `{clean_def}`")
        flag_str = f" [{', '.join(flags)}]" if flags else ""
        dbml_lines.append(f"  {c_name} {c_type}{flag_str}")
    dbml_lines.append("}\n")

# Add auth.users stub
dbml_lines.append("""Table auth.users {
  id uuid [pk, not null]
  email text
  created_at timestamp
}
""")

# Foreign keys
dbml_lines.append("// Relationship Constraints")
pilot_all_set = set(pilot_tables) | {"users"} # includes auth.users
for fk in fks_list:
    src_t = fk["source_table"]
    tgt_t = fk["target_table"]
    src_sch = fk["source_schema"]
    tgt_sch = fk["target_schema"]
    if src_t in pilot_tables and (tgt_t in pilot_tables or (tgt_sch == "auth" and tgt_t == "users")):
        del_rule = "cascade" if fk["delete_action"] == "c" else ("set null" if fk["delete_action"] == "n" else "restrict")
        dbml_lines.append(f"Ref {fk['constraint_name']}: {src_sch}.{src_t}.{fk['source_column']} > {tgt_sch}.{tgt_t}.{fk['target_column']} [delete: {del_rule}]")

with open("database-docs/diagrams/pilot_tenancy_crm.dbml", "w", encoding="utf-8") as f:
    f.write("\n".join(dbml_lines))

print("Saved pilot DBML companion to database-docs/diagrams/pilot_tenancy_crm.dbml")
