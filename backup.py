from datetime import datetime
from loader.config_loader import load_config
config = load_config()
def backup(device_name, outputs):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f'{config["backup_device"]}/{device_name}_{timestamp}.txt'
        with open(filename, "w") as file:
            for command, output in outputs.items():
                file.write(f"===== {command} =====\n")
                file.write(output)
                file.write("\n\n")
    except Exception as e:
        return {
                "success": False,
                "error": f"Backup Failed: {e}"
        }
    return {"success": True}