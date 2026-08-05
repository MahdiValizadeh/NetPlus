import sqlite3
connection = sqlite3.connect("netplus.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ip TEXT NOT NULL UNIQUE,
    vendor TEXT,
    enabled INTEGER DEFAULT 1
)
""")
connection.commit()
connection.close()
print("Database Created Successfully.")