import socket
from IPy import IP

def scanPort(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((target, port))
        print(f"[-] Port {str(port)} is open")
    except:
        print(f"[-] Port {str(port)} is closed")

target = input('[+] Enter target hostname or IP: ')

for port in range(75, 85):
    scanPort(target, port)