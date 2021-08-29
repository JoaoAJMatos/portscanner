import socket
from IPy import IP

addr = input("[+] Enter target IP or hostname: ")
port = 80

try:
    sock = socket.socket()
    sock.connect((addr, port))
    print("[-] Port 80 open")
except:
    print("[-] Port 80 closed")