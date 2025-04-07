import sqlite3
from contextlib import contextmanager

DATABASE = "sentinelguard.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        conn.commit()
        conn.close()

def init_db():
    with get_db() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hosts (
                ip TEXT PRIMARY KEY,
                security_score INTEGER DEFAULT 100,
                last_scan TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                ip TEXT,
                event_type TEXT,
                risk INTEGER,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

def log_event(ip, event_type, risk):
    with get_db() as cursor:
        cursor.execute(
            "INSERT INTO events (ip, event_type, risk) VALUES (?, ?, ?)",
            (ip, event_type, risk)
        )

def update_host_security(ip, score):
    with get_db() as cursor:
        cursor.execute(
            "INSERT OR REPLACE INTO hosts (ip, security_score, last_scan) VALUES (?, ?, datetime('now'))",
            (ip, score)
        )