import socket

def port_scanner(target, port_range):
    for port in range(1, port_range):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))  # Try to connect to the target IP and port
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

target_ip = "127.0.0.1"  # Replace with the IP address of the target
port_range = 1024  # Scan first 1024 ports
port_scanner(target_ip, port_range)
