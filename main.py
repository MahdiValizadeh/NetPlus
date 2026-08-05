import os
from loader.config_loader import load_config
config = load_config()
from database.db_loader import load_device
from checker.ping import ping
from checker.traceroute import traceroute
from checker.ssh import ssh_connect
from logger import logger
from concurrent.futures import ThreadPoolExecutor
from backup import backup
from alert.alert_manager import send_alerts
from report import generate_report
devices = load_device()
results = []


def check_device(device):
    if ping(device["ip"]):
        message = f'{device["name"]} ({device["ip"]}) 🟢 UP'
        results.append({
        "name": device["name"],
        "ip": device["ip"],
        "status": "UP",
        "ssh": "Checking",
        "backup": "Checking",
        "error": None
        })
        print(message)
        logger.info(message)
        ssh_result = ssh_connect(device["ip"], config["default_commands"])
        if ssh_result["success"]:
            for item in results:
                if item["ip"] == device["ip"]:
                    item["ssh"] = "OK"
                    break
            logger.info(f"{device['name']} - SSH Connected")
            outputs = ssh_result["output"]
            backup_result = backup(device["name"], outputs)
            if backup_result["success"]:
                for item in results:
                    if item["ip"] == device["ip"]:
                        item["backup"] = "OK"
                        break
                logger.info(f"{device['name']} - Backup Saved")
            else:
                for item in results:
                    if item["ip"] == device["ip"]:
                        item["backup"] = backup_result["error"]
                        item["error"] = backup_result["error"]
                print(backup_result["error"])
                logger.error(backup_result["error"])
            for command, output in outputs.items():
                print(output)
                logger.info(f"{device['name']} - Command Executed: {command}")
        else:
            for item in results:
                if item["ip"] == device["ip"]:
                    item["ssh"] = ssh_result["error"]
                    item["error"] = ssh_result["error"]
            print(ssh_result["error"])
            logger.error(ssh_result["error"])
    else:
        message = f'{device["name"]} ({device["ip"]}) 🔴 DOWN'
        results.append({
        "name": device["name"],
        "ip": device["ip"],
        "status": "DOWN",
        "ssh": None,
        "backup": None,
        "error": "Ping Failed"
        })

        print(message)
        logger.warning(message)
        message = traceroute(device["ip"])
        print(message)
        logger.warning(message)
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for device in devices:
        futures.append(executor.submit(check_device, device))
    for future in futures:
        future.result()
generate_report(results)
send_alerts(results)
report_path = os.path.abspath(config["report_file"])
try:
    os.startfile(report_path)
except Exception as e:
    logger.error(f"Open Report Failed: {e}")


