import subprocess
import json

doc = "MAILOFLY — Database Architecture & Engineering Audit.figcraft"
p_info = subprocess.check_output(["C:\\Program Files\\FigCraft\\figcraft-cli.exe", "info", doc, "--json"], text=True)
data = json.loads(p_info)

pages = data["pages"]
for p in pages:
    p_name = p["name"]
    # clean name for filename
    clean_name = p_name.replace(" ", "_").replace("—", "-").replace(":", "").replace("&", "and")
    out_file = f"previews/{clean_name}.png"
    print(f"Rendering page '{p_name}' -> {out_file}...")
    try:
        subprocess.check_call([
            "C:\\Program Files\\FigCraft\\figcraft-cli.exe", "render", doc,
            "-o", out_file, "--page", p_name, "--scale", "1"
        ])
    except Exception as e:
        print(f"Error rendering {p_name}: {e}")

print("All page previews rendered successfully!")
