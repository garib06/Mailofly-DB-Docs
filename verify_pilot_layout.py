import json

with open("database-docs/diagrams/pilot_layout.json", "r", encoding="utf-8") as f:
    layout = json.load(f)

nodes = layout["nodes"]
print(f"Total placed nodes: {len(nodes)}")

# Check for overlaps between any two nodes
overlaps = []
for i in range(len(nodes)):
    n1 = nodes[i]
    r1 = (n1["x"], n1["y"], n1["x"] + n1["width"], n1["y"] + n1["height"])
    for j in range(i + 1, len(nodes)):
        n2 = nodes[j]
        r2 = (n2["x"], n2["y"], n2["x"] + n2["width"], n2["y"] + n2["height"])
        
        # Check intersection
        intersect_x = not (r1[2] <= r2[0] or r2[2] <= r1[0])
        intersect_y = not (r1[3] <= r2[1] or r2[3] <= r1[1])
        if intersect_x and intersect_y:
            overlaps.append((n1["id"], n2["id"]))

print(f"Node overlap count: {len(overlaps)}")
if overlaps:
    print("Overlapping pairs:", overlaps)
else:
    print("SUCCESS: Zero table overlaps! Every table has clean bounding clearance.")

edges = layout["edges"]
print(f"Total routed edges: {len(edges)}")
for e in edges[:5]:
    sec = e["sections"][0]
    pts = [sec["startPoint"]] + sec["bendPoints"] + [sec["endPoint"]]
    print(f"  Edge {e['id']}: {len(pts)} points: {pts[0]} -> {pts[-1]}")
