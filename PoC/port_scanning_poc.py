import socket
from concurrent import futures

def request_sock(ip_addr, port):
    global valid_ports

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((ip_addr, port))
            valid_ports.append(port)
            print(f'port {port} open')
    except:
        pass

def tcp_port_scan(ip_addr):
    global valid_ports 

    valid_ports = []
    port_range = range(1, 65536)
    
    with futures.ThreadPoolExecutor(max_workers = 8) as executor:
        works = [
            executor.submit(request_sock, ip_addr, port) for port in port_range
        ]

        futures.wait(works)

TARGET_IP = '192.168.0.8'
tcp_port_scan(TARGET_IP)

print("OVER")
