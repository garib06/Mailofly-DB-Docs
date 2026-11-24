import subprocess
import json

p = subprocess.Popen(
    ["C:\\Program Files\\FigCraft\\figcraft-cli.exe", "mcp"],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1
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
        if not line: break
        line = line.strip()
        if line.startswith("{"):
            try:
                res = json.loads(line)
                if res.get("id") == msg_id: return res
            except: pass
    return None

def call_tool(name, args):
    res = send("tools/call", {"name": name, "arguments": args})
    if not res or "result" not in res: return None
    content = res["result"].get("content", [])
    if content and "text" in content[0]:
        try: return json.loads(content[0]["text"])
        except: return content[0]["text"]
    return res["result"]

send("initialize", {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test", "version": "1.0"}})

# Rename page 1
call_tool("run_command", {"command": "page.rename", "params": {"name": "1. Master Architecture"}})
call_tool("run_command", {"command": "page.setBackground", "params": {"color": "#0B0F19"}})
call_tool("create_node", {"type": "text", "name": "TitleP1", "text": "Page 1 Master", "x": 50, "y": 50, "props": {"fontSize": 20, "fill": "#FFFFFF"}})

# Add page 2
p2 = call_tool("run_command", {"command": "page.add", "params": {"name": "2. ERD - Tenancy & CRM"}})
print("Added page 2:", p2)
call_tool("run_command", {"command": "page.setBackground", "params": {"color": "#0B0F19"}})
call_tool("create_node", {"type": "text", "name": "TitleP2", "text": "Page 2 Tenancy & CRM", "x": 50, "y": 50, "props": {"fontSize": 20, "fill": "#38BDF8"}})

# List pages
plist = call_tool("run_command", {"command": "page.list", "params": {}})
print("Page list:", plist)

call_tool("save_file", {"path": "test_multipage.figcraft"})
p.terminate()
print("Saved test_multipage.figcraft successfully!")
