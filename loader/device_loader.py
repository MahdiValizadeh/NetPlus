import json 
from loader.config_loader import load_config
config = load_config()
def load_device():
    with open(config["device_file"], "r") as file:
        devices=json.load(file) 
    return devices
#print (load_device())