import sqlite3
connection = sqlite3.connect("netplus.db")
cursor = connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS monitoring_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id INTEGER,
        status TEXT,
        ssh_status TEXT,
        backup_status TEXT,
        error TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(device_id)
        REFERENCES devices(id)
    )
    """
    )
connection.commit()
connection.close()
print("Monitoring table created.")