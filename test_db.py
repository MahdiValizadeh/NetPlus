import sqlite3

connection = sqlite3.connect("netplus.db")
cursor = connection.cursor()

cursor.execute("""
SELECT name 
FROM sqlite_master 
WHERE type='table'
""")

print("////////////////////////////")
cursor.execute("SELECT * FROM monitoring_logs")
for table in cursor.fetchall():
    print(table)

connection.close()