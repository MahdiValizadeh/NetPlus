import sqlite3
def load_device():
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT id, name, ip
        FROM devices
        WHERE enabled = 1
        """
    )
    rows = cursor.fetchall()
    connection.close()
    devices = []
    for row in rows:
        devices.append({
            "id":row[0],
            "name": row[1],
            "ip": row[2]
        })
    return devices