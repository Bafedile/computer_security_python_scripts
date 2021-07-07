# import python libraries
import socket
from IPy import IP

'''
In this project, I am going to code a port scanner script that will scan ports and also display which services
are running on that port 
'''


# define a class for the port scanning
class PortScan():
    # declare banners and open ports lists
    banners = []
    open_ports = []

    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num

    # define a scan port function
    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))  # initialize a connection
            self.open_ports.append(port)  # append the open port to the open ports list

            # try and retrieve information from the target's ip address
            try:
                # add the banner to receive information from the target's ip address
                banner = sock.recv(1024).decode().strip('\n').strip('\r')

                # add the banner to the banners list
                self.banners.append(banner)

            except:
                self.banners.append(' ')
            sock.close()
        except:
            pass

    # define a function that will check the ip address of the victim by using the domain
    def check_ip(self):
        try:
            IP(self.target)
            return self.target

        except ValueError:
            return socket.gethostbyname(self.target)

    # define a function that will scan multiple targets at the same time
    def scan(self):
        # scan the targets
        for port in range(1, self.port_num):
            self.scan_port(port)
