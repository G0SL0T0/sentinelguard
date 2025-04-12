import subprocess
import platform
from .db import log_event

def isolate_host(ip):
    try:
        subprocess.run(
            ["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            check=True
        )
        log_event(ip, "BLOCK", 100)
    except subprocess.CalledProcessError as e:
        log_event(ip, "BLOCK_FAILED", 100)

def isolate_host(ip):
    if platform.system() == 'Linux':
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
    elif platform.system() == 'Windows':
        subprocess.run(f"netsh advfirewall firewall add rule name='Block {ip}' dir=in action=block remoteip={ip}", shell=True)
            

    
def limit_speed(ip, speed="1mbps"):
    commands = [
        f"tc qdisc add dev eth0 root handle 1: htb",
        f"tc class add dev eth0 parent 1: classid 1:10 htb rate {speed}",
        f"tc filter add dev eth0 protocol ip parent 1:0 prio 1 u32 match ip src {ip} flowid 1:10"
    ]
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)
    log_event(ip, "QoS_LIMIT", 70)        

