import socket
from IPy import IP

def resolveDomain(target):
    try: # Checks if the target argument is a valid IP address and returns it if 1
        IP(target)
        return(target)
    except: # If the target isn't a valid IP address the function will try to resolve the IP
        return socket.gethostbyname(target)

def scanPort(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((target, port))
        print(f"[-] Port {str(port)} is open")
    except:
        print(f"[-] Port {str(port)} is closed")

target   = input('[+] Enter target hostname or IP: ')
targetIP = resolveDomain(target)

for port in range(75, 85):
    scanPort(targetIP, port)