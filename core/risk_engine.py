from .db import get_db

def calculate_risk(ip):
    with get_db() as cursor:
        cursor.execute("SELECT risk FROM events WHERE ip = ?", (ip,))
        events = cursor.fetchall()
        cursor.execute("SELECT security_score FROM hosts WHERE ip = ?", (ip,))
        security = cursor.fetchone()
    
    if not events or not security:
        return 0
    
    avg_risk = sum(event[0] for event in events) / len(events)
    security_score = security[0]
    return min(100, avg_risk * (1 - security_score / 100))