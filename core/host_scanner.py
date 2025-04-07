import nmap
import yaml
from .db import update_host_security

def scan_host(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments='-sV -p 21,22,80,443,3389')
    
    security_score = 100  # Максимальный приоритет защиты
    

    if '22/tcp' in scanner[ip]['tcp']:     # Штрафы за уязвимости
        if 'ssh' not in scanner[ip]['tcp'][22]['version'].lower():
            security_score -= 30  # Небезопасный SSH 
    
    if '80/tcp' in scanner[ip]['tcp']:
        if 'http' in scanner[ip]['tcp'][80]['version'].lower():
            security_score -= 20  # HTTP вместо HTTPS
            
    # Добавление штрафов и нюансов для проверки сети
    
    update_host_security(ip, security_score)