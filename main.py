from loader.config_loader import load_config
config = load_config()

from loader.device_loader import load_device
from checker.ping import ping
from checker.traceroute import traceroute
from checker.ssh import ssh_connect
from logger import log
devices = load_device()

for device in devices:
    if ping(device["ip"]):
        message = f'{device["name"]} ({device["ip"]}) 🟢 UP'
        print(message)

        log(message)
        output = ssh_connect(device["ip"], config["default_command"])
        if output:
            print(output)
            log(output)

    else:
        message = f'{device["name"]} ({device["ip"]}) 🔴 DOWN'
        print(message)
        log(message)
        message = traceroute(device["ip"])
        print(message)
        log(message)