import socket
from IPy import IP

def scan(target):
    targetIP = resolveDomain(target)
    print(f"\n[-] Scanning Target: {str(target)}")

    for port in range(1, 100):
        scanPort(targetIP, port)

def resolveDomain(target):
    try: # Checks if the target argument is a valid IP address and returns it if 1
        IP(target)
        return(target)
    except: # If the target isn't a valid IP address the function will try to resolve the IP
        return socket.gethostbyname(target)

def scanPort(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.05)
        sock.connect((target, port))
        print(f"[+] Port {str(port)} is open")
    except:
        #print(f"[-] Port {str(port)} is closed")
        pass

targets  = input("[+] Enter target/s hostname or IP (split targets with ','): ")

if "," in targets:
    for target in targets.split(','):
        scan(target.strip(' '))
else:
    scan(targets)