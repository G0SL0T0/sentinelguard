import sqlite3

def init_db():
    conn = sqlite3.connect("sentinelguard.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hosts (
            ip TEXT PRIMARY KEY,
            security_score INTEGER,
            last_scan TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_event(ip, event_type, risk):
    conn = sqlite3.connect("sentinelguard.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events VALUES (?, ?, ?, datetime('now'))", 
                   (ip, event_type, risk))
    conn.commit()
    conn.close()