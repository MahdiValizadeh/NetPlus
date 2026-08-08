from database.device_manager import (get_monitoring_history, 
                                     get_monitoring_by_device,
                                     get_failed_monitoring
                                     )
def show_history():
    logs = get_monitoring_history()
    if not logs:
        print("No monitoring history found.")
        return

    for log in logs:
        print(
            f"""
            ID: {log[0]}
            Device ID: {log[1]}
            Status: {log[2]}
            SSH: {log[3]}
            Backup: {log[4]}
            Error: {log[5]}
            Time: {log[6]}
            -------------------------
            """
            )
        
def search_device_history():
    device_id = int(input("Device ID: "))
    logs = get_monitoring_by_device(device_id)
    if not logs:
        print("No history found.")
        return
    
    for log in logs:
        print(
            f"""
            ID: {log[0]}
            Device ID: {log[1]}
            Status: {log[2]}
            SSH: {log[3]}
            Backup: {log[4]}
            Error: {log[5]}
            Time: {log[6]}
            --------------------
            """
            )
def show_failed_checks():
    logs = get_failed_monitoring()
    if not logs:
        print("No failed checks found.")
        return
    for log in logs:
        print(
            f"""
ID: {log[0]}
Device ID: {log[1]}
Status: {log[2]}
SSH: {log[3]}
Backup: {log[4]}
Error: {log[5]}
Time: {log[6]}
--------------------
"""
        )

def main():
    while True:
        print("""
            --- NetPlus Monitoring ---
            1. Show History
            2. Search Device History
            3. Show Failed Checks
            4. Exit
            """)
        
        choice = input("Choose option: ")
        if choice == "1":
            show_history()

        elif choice == "2":
            search_device_history()
        elif choice == "3":
            show_failed_checks()
        elif choice == "4":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()