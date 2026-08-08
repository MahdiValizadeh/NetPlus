import sqlite3
import ipaddress
def add_device(name, ip):
    if not name.strip():
        return False, "Device name cannot be empty."
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False, "Invalid IP address."
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO devices(name, ip)
            VALUES (?, ?)
            """,
            (name, ip)
        )
        connection.commit()
        return True, "Device added successfully"
    except sqlite3.IntegrityError:
        connection.close()
        return False, "Device already exists."

def get_all_devices():
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM devices")
    devices = cursor.fetchall()
    connection.close()
    return devices

def update_device(device_id, name, ip):
    if not name.strip():
        return False, "Device name cannot be empty."
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False, "Invalid IP address."
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
    if cursor.rowcount == 0:
        connection.close()
        return False, "Device not found."
    connection.commit()
    connection.close()
    return True, "Device updated successfully."

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
    if cursor.rowcount == 0:
        connection.close()
        return False, "Device not found."
    connection.commit()
    connection.close()
    return True, "Device deleted successfully."

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

def save_monitoring_result(
        device_id,
        status,
        ssh_status,
        backup_status,
        error=None
):
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO monitoring_logs
        (
            device_id,
            status,
            ssh_status,
            backup_status,
            error
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            device_id,
            status,
            ssh_status,
            backup_status,
            error
        )
    )
    connection.commit()
    connection.close()

def get_monitoring_history():
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT *
        FROM monitoring_logs
        ORDER BY id DESC
        """
    )
    logs = cursor.fetchall()
    connection.close()
    return logs

def get_monitoring_by_device(device_id):
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT *
        FROM monitoring_logs
        WHERE device_id = ?
        ORDER BY id DESC
        """,
        (device_id,)
    )
    logs = cursor.fetchall()
    connection.close()
    return logs

def get_failed_monitoring():
    connection = sqlite3.connect("netplus.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT *
        FROM monitoring_logs
        WHERE status != 'UP'
           OR ssh_status != 'OK'
           OR backup_status != 'OK'
        ORDER BY id DESC
        """
    )
    logs = cursor.fetchall()
    connection.close()
    return logs
