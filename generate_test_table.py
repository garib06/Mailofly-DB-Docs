import subprocess
import json
import os

# Test script for Figcraft table creation
commands = [
    { "command": "page.rename", "params": { "name": "Pilot ERD Test" } },
    { "command": "page.setBackground", "params": { "color": "#0B0F19" } },
    
    # Canvas Header
    {
        "command": "node.create",
        "params": {
            "type": "text",
            "name": "Title",
            "text": "MAILOFLY DATABASE ARCHITECTURE — PILOT ERD",
            "x": 60, "y": 60,
            "props": { "fontSize": 24, "fill": "#F8FAFC", "fontWeight": 700 }
        }
    },
    {
        "command": "node.create",
        "params": {
            "type": "text",
            "name": "Subtitle",
            "text": "Tenancy & CRM Domain Relationship Verification | Deterministic Graph Layout",
            "x": 60, "y": 95,
            "props": { "fontSize": 14, "fill": "#94A3B8" }
        }
    },

    # Table 1: organizations
    {
        "command": "node.create",
        "params": {
            "type": "frame",
            "name": "public.organizations",
            "x": 100, "y": 160,
            "width": 420,
            "props": {
                "fill": "#111827",
                "stroke": "#38BDF8",
                "strokeWeight": 1.5,
                "cornerRadius": 8,
                "layout": "vertical",
                "gap": 0,
                "padding": 0,
                "sizingV": "hug"
            }
        }
    },
    # Table 1 Header
    {
        "command": "node.create",
        "params": {
            "type": "frame",
            "name": "Header",
            "props": {
                "fill": "#1E293B",
                "layout": "horizontal",
                "mainAlign": "spaceBetween",
                "crossAlign": "center",
                "padding": [10, 14, 10, 14],
                "sizingH": "fill"
            }
        }
    },
    {
        "command": "node.create",
        "params": {
            "type": "text",
            "name": "TableName",
            "text": "public.organizations",
            "props": { "fontSize": 13, "fill": "#F8FAFC", "fontWeight": 700 }
        }
    },
    {
        "command": "node.create",
        "params": {
            "type": "text",
            "name": "Badge",
            "text": "14 cols",
            "props": { "fontSize": 11, "fill": "#94A3B8" }
        }
    },
    # Select parent table again to add rows
    { "command": "select.parent", "params": {} },
    
    # Row 1: id
    {
        "command": "node.create",
        "params": {
            "type": "frame",
            "name": "Row_id",
            "props": {
                "layout": "horizontal",
                "crossAlign": "center",
                "padding": [6, 14, 6, 14],
                "gap": 10,
                "sizingH": "fill",
                "fill": "#111827"
            }
        }
    },
    { "command": "node.create", "params": { "type": "text", "name": "PK", "text": "PK", "props": { "fontSize": 10, "fill": "#F59E0B", "fontWeight": 700 } } },
    { "command": "node.create", "params": { "type": "text", "name": "ColName", "text": "id", "props": { "fontSize": 11, "fill": "#F8FAFC", "fontWeight": 600 } } },
    { "command": "node.create", "params": { "type": "text", "name": "Type", "text": "uuid", "props": { "fontSize": 11, "fill": "#38BDF8" } } },
    { "command": "node.create", "params": { "type": "text", "name": "Null", "text": "NOT NULL", "props": { "fontSize": 10, "fill": "#64748B" } } },
    
    # Back to table
    { "command": "select.parent", "params": {} },

    # Row 2: name
    {
        "command": "node.create",
        "params": {
            "type": "frame",
            "name": "Row_name",
            "props": {
                "layout": "horizontal",
                "crossAlign": "center",
                "padding": [6, 14, 6, 14],
                "gap": 10,
                "sizingH": "fill",
                "fill": "#0F172A"
            }
        }
    },
    { "command": "node.create", "params": { "type": "text", "name": "PK", "text": "  ", "props": { "fontSize": 10, "fill": "#64748B" } } },
    { "command": "node.create", "params": { "type": "text", "name": "ColName", "text": "name", "props": { "fontSize": 11, "fill": "#F8FAFC" } } },
    { "command": "node.create", "params": { "type": "text", "name": "Type", "text": "text", "props": { "fontSize": 11, "fill": "#38BDF8" } } },
    { "command": "node.create", "params": { "type": "text", "name": "Null", "text": "NOT NULL", "props": { "fontSize": 10, "fill": "#64748B" } } }
]

with open("test_table_script.json", "w", encoding="utf-8") as f:
    json.dump(commands, f, indent=2)

print("Saved test_table_script.json")
