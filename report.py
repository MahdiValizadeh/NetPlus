from datetime import datetime

from loader.config_loader import load_config
config = load_config()
def generate_report(results):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_devices = len(results)
    up_devices = sum(1 for device in results if device["status"] == "UP")
    down_devices = sum(1 for device in results if device["status"] == "DOWN")
    with open(config["report_file"], "w") as file:
        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("<title>NetPlus Report</title>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write("<h1>NetPlus Report</h1>\n")
        file.write(f"<p>Generated: {timestamp}</p>\n")
        file.write(f"<p>Total Devices: {total_devices}</p>\n")
        file.write(f"<p class='up'>UP: {up_devices}</p>\n")
        file.write(f"<p class='down'>DOWN: {down_devices}</p>\n")
        file.write("<style>\n") #استایل
        file.write("body { font-family: Arial; margin: 30px; }\n")
        file.write("h1 { color: blue; }\n")
        file.write("h2 { margin-top: 20px; }\n")
        file.write("p { font-size: 16px; }\n")
        file.write(".up { color: green; font-weight: bold; }\n") # رنگ status
        file.write(".down { color: red; font-weight: bold; }\n")
        file.write("table { border-collapse: collapse; width: 100%; }\n") #استایل table
        file.write("th, td { border: 1px solid black; padding: 8px; text-align: left; }\n")
        file.write("th { background-color: #ddd; }\n")
        file.write("</style>\n")
        file.write("<table>\n") #ساختار table
        file.write("<tr>\n")
        file.write("<th>Device</th>\n")
        file.write("<th>IP</th>\n")
        file.write("<th>Status</th>\n")
        file.write("<th>SSH</th>\n")
        file.write("<th>Backup</th>\n")
        file.write("</tr>\n")
        for device in results:
            file.write("<tr>\n")
            file.write(f"<td>{device['name']}</td>\n")
            file.write(f"<td>{device['ip']}</td>\n")
            if device["status"] == "UP":
                file.write("<td class='up'>UP</td>\n")
            else:
                file.write("<td class='down'>DOWN</td>\n")
            file.write(f"<td>{device['ssh']}</td>\n")
            if device["backup"] == "OK":
                file.write("<td class='up'>OK</td>\n")
            elif device["backup"] is None:
                file.write("<td>-</td>\n")
            else:
                file.write(f"<td class='down'>{device['backup']}</td>\n")
            file.write("</tr>\n")
        file.write("</table>\n")
        file.write("</body>\n")
        file.write("</html>\n")