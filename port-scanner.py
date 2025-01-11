import argparse
import asyncio
import socket
from time import time

async def scan_port(target: str, port: int) -> dict:

    try:    
        conn = asyncio.open_connection(target, port)
        reader, writer = await asyncio.wait_for(conn, timeout=1)
        writer.close()
        await writer.wait_closed()
        
        service_name = socket.getservbyport(port, "tcp")
        return {"port": port, "status": "open", "service": service_name}
    
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        return {"port": port, "status": "closed", "service": None}
    
    except socket.error:
        return {"port": port, "status": "error", "service": None}

async def scan_ports(target: str, ports: list[int]) -> tuple[list[dict], float]: 
    open_ports = []
    start = time()
    tasks = [scan_port(target, port) for port in ports]
    results = await asyncio.gather(*tasks)

    for result in results:
        if result["status"] == "open":
            open_ports.append(result)
    
    end = time()
    elapsed_time = end - start

    return open_ports, elapsed_time

def main():
    parser = argparse.ArgumentParser(description="A simple port scanner with service detection.")
    parser.add_argument('target', help="The target IP address or hostname to scan.")
    parser.add_argument('-p', '--ports', type=str, default="1-1024", help="Range of ports to scan (e.g., '1-1024' or '22,80,443').")
    
    args = parser.parse_args()
        
    if '-' in args.ports:
        start_port, end_port = map(int, args.ports.split('-'))
        ports = range(start_port, end_port + 1)
    else:
        ports = list(map(int, args.ports.split(',')))
    
    open_ports, elapsed_time = asyncio.run(scan_ports(args.target, ports))
 
    if open_ports:
        print("Open ports and their services:")
        for port_info in open_ports:
            print(f"Port {port_info['port']} is open. Service: {port_info['service']}")
    else:
        print("No open ports found.")
    
    print(f"\nScanning completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()

