import socket
import threading
import time
from queue import Queue

def banner_grab(ip, port):
    """Try to grab the banner of the service running on the port"""
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return "Unknown Service"

def scan_port(ip, port):
    """Scan a specific port and display results"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        conn = s.connect_ex((ip, port))
        if conn == 0:
            banner = banner_grab(ip, port)
            print(f"[+] Port {port} is open: {banner}")
        s.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

def worker(ip, queue):
    """Worker thread to scan ports from the queue"""
    while not queue.empty():
        port = queue.get()
        scan_port(ip, port)
        queue.task_done()

def port_scanner(ip, ports, num_threads=10):
    """Main function to handle port scanning"""
    print(f"\n[!] Scanning {ip} with {num_threads} threads...\n")
    queue = Queue()
    for port in ports:
        queue.put(port)
    
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(ip, queue))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"\n[!] Scan completed!")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    ports = range(1, 1025)  # Scan common ports (1-1024)
    port_scanner(target_ip, ports, num_threads=20)
