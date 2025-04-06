from .db import get_host_events, get_host_security

def calculate_risk(ip):
    events = get_host_events(ip)
    security = get_host_security(ip)
    
    risk = sum(event["risk"] for event in events) * (1 - security / 100)
    return min(100, risk)  # Риск <100%