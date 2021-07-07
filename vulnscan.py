# import the port scanner
import port_scanner

'''
   In this project we will be creating a vulnerability scanner by using the port scanner
   --> The user has to be prompted to enter the target's ip address 
   --> Also they should be prompted to enter the range of port they want to scan 
   --> And also they should be prompted to enter the path to save the file with vulnerable softwares
   
'''

# get the target ip address and port number
targets_ip = input('[+]* Enter Target To Scan For Vulnerability: ')
port_num = int(input('[+]* Enter Amount Of Ports You Want To Scan: '))
vul_file = input('[+]* Enter Path To The File With Vulnerable Softwares: ')
print('\n')

# call the port scanner class
vulScan = port_scanner.PortScan(targets_ip, port_num)

# scan for the open ports
vulScan.scan()

# open the file with vulnerable banners
with open(vul_file, 'r') as file:
    count = 0
    for banner in vulScan.banners:
        # print(banner)
        file.seek(0)  # incase we remove this it will not get the next banner(return to the begining)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: ', str(banner), ' Port ', str(vulScan.open_ports[count]))

        count = count + 1  # increase the count in every banner by 1
