# import python libraries
import socket
from IPy import IP

'''
In this project, I am going to code a port scanner script that will scan ports and also display which services
are running on that port 
'''


# define a scan port function
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))  # initialize a connection

        # try and retrieve information from the target's ip address
        try:
            # add the banner to receive information from the target's ip address
            banner = get_banner(sock)

            # display the port details
            print('[+] Port Open ', str(port), ' ', str(banner.decode().strip('\n')))
        except:
            print('[+] Port Open ', str(port))
    except:
        pass


# define a function that will check the ip address of the victim by using the domain
def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)


# define a function that will scan multiple targets at the same time
def scan(targets):
    # convert the ip address
    converted_ipaddress = check_ip(targets)

    # display the scanned target
    print('\n[+_0Scanning target] ', str(targets), ' ip address ', str(converted_ipaddress))

    # scan the targets
    for port in range(1, 500):
        scan_port(converted_ipaddress, port)


# define a banner function that will get information from the target's ip address
def get_banner(sock):
    return sock.recv(1024)


if __name__ == '__main__':
    # ask the user to enter the target's ip address
    targets = input('Enter target/s to Scan(split targets with ,):')

    '''
       Split the targets and scan each target 
    '''
    if ',' in targets:
        for target in targets.split(','):
            scan(target.strip(' '))
    else:
        scan(targets)

