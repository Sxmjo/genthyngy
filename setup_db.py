import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS keys (code TEXT PRIMARY KEY, expires_at TEXT, active INTEGER)")

sample = "KEY-001"
expires = (datetime.now() + timedelta(days=1)).isoformat()

cur.execute("INSERT OR REPLACE INTO keys VALUES (?, ?, ?)", (sample, expires, 1))

conn.commit()
conn.close()

print("Setup complete. Test key:", sample)
