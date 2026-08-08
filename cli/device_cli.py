from database.device_manager import (add_device,
                                     get_all_devices,
                                     update_device,
                                     delete_device,
                                     get_device_by_ip,
                                     get_device_by_name)
def show_devices():
    devices=get_all_devices()
    if not devices:
        print("No devices found.")
        return
    for device in devices:
        print_device(device)
def print_device(device):
    print(
        f"ID: {device[0]} | "
        f"Name: {device[1]} | "
        f"IP: {device[2]} | "
        f"Last Seen: {device[3]} | "
        f"Enabled: {device[4]}"
    )
def get_device_id():
    while True:
        try:
            return int(input("Device ID: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
def main():
    while True:
        print("\n--- NetPlus Device Manager ---")
        print("1. Add Device")
        print("2. List Devices")
        print("3. Update Device")
        print("4. Delete Device")
        print("5. Search by IP")
        print("6. Search by Name")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Device name: ")
            ip = input("Device IP: ")
            success, message = add_device(name, ip)
            print(message)

        elif choice == "2":
            show_devices()
        elif choice == "3":
            device_id = get_device_id()
            name = input("New name: ")
            ip = input("New IP: ")
            success, message=update_device(device_id, name, ip)
            print(message)
        elif choice == "4":
            device_id = get_device_id()
            success, message=delete_device(device_id)
            print(message)
        elif choice == "5":
            ip = input("IP address: ")
            device = get_device_by_ip(ip)
            if device:
                print_device(device)
            else:
                print("Device not found.")
        elif choice == "6":
            name = input("Device name: ")
            device = get_device_by_name(name)
            if device:
                print_device(device)
            else:
                print("Device not found.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()   