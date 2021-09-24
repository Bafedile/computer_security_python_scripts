import socket 
from queue import Queue
import threading

# initialize queue
queue = Queue()

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker(target):
    while not queue.empty():
        port = queue.get()
        value = scanner(target,port)
        #print(value)
        if value:  
            print(f'Open Port {port}')
            open_ports.append(port)
                


def scanner(target,port):
    try:
        #print('port '+str(port))
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        try:
            banner = sock.recv(1024).decode().strip('\n')
            banner_list.append(banner)
        except:
            banner_list.append(' ')
        return True
    except:
        return False


# Ask the user to enter target 
target = input('Please enter target ip address: ')
ports = int(input('Please enter port range to scan: '))

# initialize threads
thread_list = []
banner_list = []
open_ports = []
port_list = range(1,ports)
fill_queue(port_list)

for i in range(500):
    thread = threading.Thread(target=worker,args=(target,))
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

# display open ports
i = 0
print('\n\nScan Completed ')
for port in open_ports:
    banner = banner_list[i]
    print(f'[+] Port {port} Open  | {banner}')
    i = i + 1

