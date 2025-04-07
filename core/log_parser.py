import re
import yaml
from datetime import datetime
from .db import log_event

def parse_nginx_log(line):
    pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* \[(?P<date>.*?)\] "(?P<request>.*?)"'
    match = re.match(pattern, line)
    if match:
        return {
            "ip": match.group("ip"),
            "date": match.group("date"),
            "request": match.group("request")
        }
    return None

def detect_threats(log_data):
    threats = {
        "SQLi": ["sqlmap", "union select", "1=1"],
        "XSS": ["<script>", "alert("],
        "Bruteforce": ["wp-login.php", "POST /login"]
    }
    for threat, keywords in threats.items():
        if any(keyword in log_data["request"].lower() for keyword in keywords):
            return threat
    return None

def start_log_monitor():
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)
    
    log_file = config["logs"]["nginx"]
    with open(log_file, "r") as f:
        while True:
            line = f.readline()
            if line:
                parsed = parse_nginx_log(line)
                if parsed:
                    threat = detect_threats(parsed)
                    if threat:
                        risk = 80 if threat == "SQLi" else 60
                        log_event(parsed["ip"], threat, risk)