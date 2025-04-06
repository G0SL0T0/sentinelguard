import subprocess
from .db import log_action

def isolate_host(ip):
    subprocess.run(f"iptables -A INPUT -s {ip} -j DROP", shell=True)
    log_action(ip, "BLOCK", "Автоматическая изоляция")

def limit_speed(ip, speed):
    subprocess.run(f"tc qdisc add dev eth0 root handle 1: htb", shell=True)
    subprocess.run(f"tc class add dev eth0 parent 1: classid 1:10 htb rate {speed}", shell=True)
    subprocess.run(f"tc filter add dev eth0 protocol ip parent 1:0 prio 1 u32 match ip src {ip} flowid 1:10", shell=True)
    log_action(ip, "QoS", f"Ограничение скорости до {speed}")