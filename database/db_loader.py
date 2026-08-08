import sqlite3
def load_device():
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT name, ip
        FROM devices
        WHERE enabled = 1
        """
    )
    rows = cursor.fetchall()
    connection.close()
    devices = []
    for row in rows:
        devices.append({
            "name": row[0],
            "ip": row[1]
        })
    return devices