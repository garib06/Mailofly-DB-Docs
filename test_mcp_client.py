import subprocess
import json
import os

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

# Initialize MCP session
print("Initialize:", send("initialize", {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}}))
print("Initialized notification:", send("notifications/initialized", {}))

# Test creating a frame with parent
f1 = call_tool("create_node", {
    "type": "frame",
    "name": "Card",
    "x": 100, "y": 100, "width": 400, "height": 300,
    "props": {"fill": "#1E293B", "layout": "vertical", "padding": 16, "gap": 8}
})
print("Created f1:", f1)
f1_id = f1["id"] if isinstance(f1, dict) else None

t1 = call_tool("create_node", {
    "type": "text",
    "name": "CardTitle",
    "parent": f1_id,
    "text": "Hello Nested Card!",
    "props": {"fontSize": 18, "fill": "#FFFFFF", "fontWeight": 700}
})
print("Created t1:", t1)

# Save file
sf = call_tool("save_file", {"path": "test_nested.figcraft"})
print("Saved file:", sf)

p.terminate()
