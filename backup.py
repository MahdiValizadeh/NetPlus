from datetime import datetime
from loader.config_loader import load_config
config = load_config()
def backup(device_name, output):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'{config["backup_device"]}/{device_name}_{timestamp}.txt'
    with open(filename, "w") as file:
        file.write(output)