#!/usr/bin/env python3
import subprocess
from threading import Thread
from core.log_parser import start_log_monitor
from core.host_scanner import start_periodic_scan
from web.app import start_web_server

def main():
    
    log_thread = Thread(target=start_log_monitor) # Запуск парсера логов в фоне
    log_thread.daemon = True
    log_thread.start()

    
    scan_thread = Thread(target=start_periodic_scan, args=(300,)) # Сканирования хостов каждые 5 минут
    scan_thread.daemon = True
    scan_thread.start()

    
    start_web_server() # Запуск веб-сервера

if __name__ == "__main__":
    print("[+] Запуск SentinelGuard...")
    main()