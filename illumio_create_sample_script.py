# this file is a python script for generating random filtering rules

import random

k = 250000

f = open("random_rules.csv", "w")

# for ip is a range and port is a range
for i in range(k):
    # if start and end range are same, it is ok
    # _s shorts for start, _e shorts for end
    # split ip address into four segments
    ip1_s = random.randint(0, 255)
    ip1_e = random.randint(ip1_s , 255)
    ip2_s = random.randint(0, 255)
    ip2_e = random.randint(ip2_s , 255)
    ip3_s = random.randint(0, 255)
    ip3_e = random.randint(ip3_s , 255)
    ip4_s = random.randint(0, 255)
    ip4_e = random.randint(ip4_s , 255)
    port_s = random.randint(1 , 2**16-1)
    port_e = random.randint(port_s , 2**16-1)
    # inorout means inbound or outbound
    if random.randint(0, 1) == 0:
        inorout = "inbound"
    else:
        inorout = "outbound"
    # toru means tcp or udp
    if random.randint(0, 1) == 0:
        toru = "tcp"
    else:
        toru = "udp"  
    f.write(inorout + ',' + toru + ',' + str(port_s) + '-' + str(port_e) + ',' + str(ip1_s)+'.'+str(ip2_s) + '.' + str(ip3_s) + '.' + str(ip4_s)+ '-' + str(ip1_e)+'.'+str(ip2_e) + '.' + str(ip3_e) + '.' + str(ip4_e)+ "\n")
    print(i/k)
    
# for ip is a single ip and port is a range
for i in range(k):
    # if start and end range are same, it is ok
    ip1_s = random.randint(0, 255)
    ip2_s = random.randint(0, 255)
    ip3_s = random.randint(0, 255)
    ip4_s = random.randint(0, 255)
    port_s = random.randint(1 , 2**16-1)
    port_e = random.randint(port_s , 2**16-1)
    if random.randint(0, 1) == 0:
        inorout = "inbound"
    else:
        inorout = "outbound"
    if random.randint(0, 1) == 0:
        toru = "tcp"
    else:
        toru = "udp"    
    f.write(inorout + ',' + toru + ',' + str(port_s) + '-' + str(port_e) + ',' + str(ip1_s)+'.'+str(ip2_s) + '.' + str(ip3_s) + '.' + str(ip4_s) + "\n")


# for ip is a range and port is a single
for i in range(k):
    # if start and end range are same, it is ok
    # _s shorts for start, _e shorts for end
    # split ip address into four segments
    ip1_s = random.randint(0, 255)
    ip1_e = random.randint(ip1_s , 255)
    ip2_s = random.randint(0, 255)
    ip2_e = random.randint(ip2_s , 255)
    ip3_s = random.randint(0, 255)
    ip3_e = random.randint(ip3_s , 255)
    ip4_s = random.randint(0, 255)
    ip4_e = random.randint(ip4_s , 255)
    port = random.randint(1 , 2**16-1)
    if random.randint(0, 1) == 0:
        inorout = "inbound"
    else:
        inorout = "outbound"
    if random.randint(0, 1) == 0:
        toru = "tcp"
    else:
        toru = "udp"  
    f.write(inorout + ',' + toru + ',' + str(port) + ','+ str(ip1_s)+'.'+str(ip2_s) + '.' + str(ip3_s) + '.' + str(ip4_s)+ '-' + str(ip1_e)+'.'+str(ip2_e) + '.' + str(ip3_e) + '.' + str(ip4_e)+ "\n")
    print(i/k)
        
# for ip is a single ip and port is a single
for i in range(k):
    # if start and end range are same, it is ok
    ip1_s = random.randint(0, 255)          
    ip2_s = random.randint(0, 255)  
    ip3_s = random.randint(0, 255)
    ip4_s = random.randint(0, 255)
    port = random.randint(0 , 2**16-1)
    if random.randint(1, 1) == 0:
        inorout = "inbound"
    else:
        inorout = "outbound"
    if random.randint(0, 1) == 0:
        toru = "tcp"
    else:
        toru = "udp"    
    f.write(inorout + ',' + toru + ',' + str(port) + ',' + str(ip1_s)+'.'+str(ip2_s) + '.' + str(ip3_s) + '.' + str(ip4_s) + "\n")