from datetime import datetime
from loader.config_loader import load_config
config = load_config()
def log(message):
    with open(config["log_file"], "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")