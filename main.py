from loader.config_loader import load_config
config = load_config()

from loader.device_loader import load_device
from checker.ping import ping
from checker.traceroute import traceroute
from checker.ssh import ssh_connect
from logger import log
from threading import Thread
from backup import backup
devices = load_device()


def check_device(device):
    if ping(device["ip"]):
        message = f'{device["name"]} ({device["ip"]}) 🟢 UP'
        print(message)
        log(message)
        outputs = ssh_connect(device["ip"], config["default_commands"])
        if outputs:
            backup(device["name"], outputs)
            for command, output in outputs.items():
                print(output)
                log(output)
    else:
        message = f'{device["name"]} ({device["ip"]}) 🔴 DOWN'
        print(message)
        log(message)
        message = traceroute(device["ip"])
        print(message)
        log(message)

threads = []
for device in devices:
    thread = Thread(target=check_device, args=(device,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()