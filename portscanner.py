#------ PortScanner for vulnerability checking ------#
import socket
from IPy import IP

class PortScan():
    banners   = []
    openPorts = []

    def __init__(self, target, ports):
        self.target = target
        self.ports = ports


    def scan(self):
        for port in range(1, 100):
            self.scanPort(port)


    def resolveDomain(self):
        try: # Checks if the target argument is a valid IP address and returns it if 1
            IP(self.target)
            return(self.target)
        except: # If the target isn't a valid IP address the function will try to resolve the IP
            return socket.gethostbyname(self.target)


    def scanPort(self, port):
        try:
            targetIP = self.resolveDomain()
            sock = socket.socket()
            sock.settimeout(0.1)
            sock.connect((targetIP, port))
            self.openPorts.append(port)

            try: # Tries to get the service that's running on the port by attempting to get information about the banner of the service
                # Warning: You wont be able to recieve the banner on most of the websites. 
                self.banners.append(sock.recv(1024).decode().strip("\n").strip("\r"))
            except:
                self.banners.append(" ")

            sock.close()
        except:
            pass