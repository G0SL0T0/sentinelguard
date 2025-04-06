import re
import yaml
from datetime import datetime
from .db import log_event

def parse_nginx_log(log_line):
    pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<request>.*?)"'
    match = re.match(pattern, log_line)
    if match:
        return {
            "ip": match.group("ip"),
            "date": datetime.strptime(match.group("date"), "%d/%b/%Y:%H:%M:%S %z"),
            "request": match.group("request")
        }
    return None

def start_log_monitor():
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)
    
    log_path = config["log_paths"]["nginx"]
    with open(log_path, "r") as f:
        while True:
            line = f.readline()
            if line:
                event = parse_nginx_log(line)
                if event and "sqlmap" in event["request"].lower():
                    log_event(event["ip"], "SQLi Attempt", risk=90)