from socket import socket, AF_INET, SOCK_STREAM
from time import time

def scan_ports(target: str, ports: list[int]) -> tuple[list[int], float]:
    open_ports: list[int] = []
    print(f"Scanning {target} for open ports...\n")
    
    start: float = time()

    for port in ports:
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.settimeout(1)  # Timeout for connection attempt
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
    
    end: float = time()
    elapsed_time: float = end - start

    return open_ports, elapsed_time

if __name__ == "__main__":
    target: str = input("Enter the IP address or hostname to scan: ")
    ports: list[int] = range(1, 1025)  # Scanning ports from 1 to 1024
    
    open_ports, elapsed_time = scan_ports(target, ports)
    
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open.")
    else:
        print("No open ports found.")

    print(f"\nScanning completed in {elapsed_time:.2f} seconds.")
