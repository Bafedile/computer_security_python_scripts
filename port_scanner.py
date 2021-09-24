import socket 
import threading

#declare a function to scan
def scanner(target,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        target = socket.gethostbyname(target)
        sock.connect((target,port))
        sock.settimeout(0.5)
        try:
            banner = sock.recv(1024).decode().strip('\n')
            print(f'[+] Port {port} is open    | {banner}')
        
        except :
            print(f'[+] Port {port} is open')
                        
    except:
        pass


def scan_ports(ports):
    for port in range(1,ports):
        scanner(target,port)
        

# ask the user to enter target 
target = input('Please enter target ip address: ')

# Ask the user to enter how many ports to scan 
ports = int(input('Please enter how many ports you want to scan: '))

scan_ports(ports)
