import sqlite3
def add_device(name, ip):
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO devices(name, ip)
        VALUES (?, ?)
        """,
        (name, ip)
    )
    connection.commit()
    connection.close()

def get_all_devices():
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM devices")
    devices = cursor.fetchall()
    connection.close()
    return devices

def update_device(device_id, name, ip):
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE devices
        SET name = ?, ip = ?
        WHERE id = ?
        """,
        (name, ip, device_id)
    )
    connection.commit()
    connection.close()

def delete_device(device_id):
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM devices
        WHERE id = ?
        """,
        (device_id,)
    )
    connection.commit()
    connection.close()

def get_device_by_ip(ip):
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT *
        FROM devices
        WHERE ip = ?
        """,
        (ip,)
    )
    device = cursor.fetchone()
    connection.close()
    return device

def get_device_by_name(name):
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT *
        FROM devices
        WHERE name = ?
        """,
        (name,)
    )
    device = cursor.fetchone()
    connection.close()
    return device
