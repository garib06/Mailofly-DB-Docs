from PIL import Image
import json

with open("database-docs/diagrams/pilot_layout.json", "r", encoding="utf-8") as f:
    layout = json.load(f)

nodes_by_id = { n["id"]: n for n in layout["nodes"] }

im = Image.open('mailofly_pilot_tenancy_crm.png')

# Find center of organizations table
org_node = nodes_by_id["public.organizations"]
ox, oy = org_node["x"], org_node["y"]
print(f"Organizations at x={ox}, y={oy}")

# Crop 1: Around organizations & users
crop1_box = (max(0, ox - 400), max(0, oy - 200), min(im.width, ox + 1400), min(im.height, oy + 1200))
crop1 = im.crop(crop1_box)
crop1.save(r'C:\Users\atharva\.gemini\antigravity\brain\ce7557b2-0727-450a-a8f2-9d13258101df\pilot_crop_tenancy_hub.png')

# Find center of contacts table
cont_node = nodes_by_id["public.contacts"]
cx, cy = cont_node["x"], cont_node["y"]
print(f"Contacts at x={cx}, y={cy}")

# Crop 2: Around contacts & properties
crop2_box = (max(0, cx - 400), max(0, cy - 200), min(im.width, cx + 1400), min(im.height, cy + 1200))
crop2 = im.crop(crop2_box)
crop2.save(r'C:\Users\atharva\.gemini\antigravity\brain\ce7557b2-0727-450a-a8f2-9d13258101df\pilot_crop_contacts_crm.png')

print("Saved high-res detail crops to brain artifact directory!")
