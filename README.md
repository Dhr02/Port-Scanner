# TCP Port Scanner in Python

This project is a multi-threaded **TCP Port Scanner** built using Python. It scans a range of ports on a target IP address to identify which ports are open and what services might be running on them.

## 🔧 Features
- **Multi-threaded scanning**: Uses multiple threads to speed up the scanning process.
- **Banner grabbing**: Attempts to fetch and display service banners from open ports.
- **User input**: Prompt for the target IP address dynamically.
- **Common port range**: Scans ports from 1 to 1024 by default.

## 📌 How It Works
1. The user runs the script and enters the target IP address.
2. The script loads a queue with ports to scan.
3. Multiple threads are created to handle scanning concurrently.
4. For each open port, it prints the port number and the service banner (if any).

## 📦 Dependencies
No external libraries required. Pure Python implementation using:
- `socket`
- `threading`
- `queue`

## 🚀 Usage
Run the script using Python:
```bash
python port-scanner.py
```
Enter the target IP when prompted:
```
Enter target IP: 192.168.1.1
```

## 🧠 Learning Outcome
This project helps you understand:
- Basic networking and sockets
- Multi-threading in Python
- Banner grabbing and basic service detection

---

## 🛡️ Disclaimer
This tool is intended for **educational purposes** and **authorized testing only**. Do **not** scan targets without permission.

