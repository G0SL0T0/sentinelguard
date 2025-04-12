from core.risk_engine import calculate_risk
from core.db import log_event

def test_risk_calculation():
    log_event("192.168.1.1", "SQLi", 90)
    log_event("192.168.1.1", "XSS", 60)
    risk = calculate_risk("192.168.1.1")
    assert 70 <= risk <= 80