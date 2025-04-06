import nmap
from .db import update_host_security

def scan_host(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments='-sV -p 21,22,80,443')
    
    security_score = 100  # Макс. балл = макс приоритет защиты
    
    if '22/tcp' in scanner[ip]['tcp']:
        if 'ssh' not in scanner[ip]['tcp'][22]['version'].lower():
            security_score -= 40  # Уязвимый SSH
    
    update_host_security(ip, security_score)