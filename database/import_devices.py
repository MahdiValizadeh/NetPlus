import sqlite3
import json
connection = sqlite3.connect("netplus.db")
cursor = connection.cursor()
with open("devices.json", "r") as file:
    devices = json.load(file)
for device in devices:
    cursor.execute(
        """
        INSERT INTO devices(name, ip)
        VALUES(?, ?)
        """,
        (device["name"], device["ip"])
    )
connection.commit()
connection.close()
print("Devices Imported Successfully.")

