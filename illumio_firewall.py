class Firewall:
    def __init__(self, path):
        """
        receive path and store rules using idea 2 hashmap
        type path: str
        """
        self.rules = {}
        fh = open(path)
        # use an iterator to read a text file one line at time
        for line in fh:
            self.construct_rules(line)
        fh.close()
        
    def construct_rules(self, line):
        """
        put rules into hashmap
        consider cases range/single port & range/single ip
        type line: str
        """
        direction, protocol, port, ip = line.split(',')
        ip = ip[:-1]            
        rs = 0
        lport = rport = lip = rip = None
        if direction == "inbound":
            rs += 1 << 49
        if protocol == "tcp" :
            rs += 1 << 48        
        if '-' in port:
            lport,rport = port.split('-')
        if '-' in ip:
            lip, rip = ip.split('-')
        if lport and lip:
            # ip and port both are ranges
            for i in range(self.translate_ip(lip),self.translate_ip(rip)+1) :
                for j in range(int(lport),int(rport)+1):
                    j <<= 32
                    self.rules[rs + j + i] = 1
        elif lport:
            # port is a range, ip is a value
            for j in range(int(lport),int(rport)+1):
                j <<= 32
                self.rules[rs + j + self.translate_ip(ip)] = 1
        elif lip:
            # port is a value, ip is a range
            for i in range(self.translate_ip(lip),self.translate_ip(rip)+1) :
                self.rules[rs + (int(port) << 32) + i] = 1
        else:
            self.rules[rs + (int(port) << 32) + self.translate_ip(ip)] = 1
        return
          
          
    
    def translate_ip(self, ip):
        """
        convert ip to integer
        type ip: str
        rtype integer
        """
        rs = 0
        for index,i in enumerate(ip.split('.')):
            rs+=int(i) << ((3-index)*8)
        return rs
    
    def translate(self, direction, protocol, port, ip):
        """
        convert rule or accept_packet to integer
        type direction: str
        type protocol: str
        type port: integer
        type ip: str
        rtype integer
        """
        rs = 0
        if direction == "inbound":
            rs += 1 << 49
        if protocol == "tcp" :
            rs += 1 << 48
        rs += port << 32
        for index,i in enumerate(ip.split('.')):
            rs+=int(i) << ((3-index)*8)
        return rs
        
    def accept_packet(self, direction, protocol, port, ip):
        """
        return True if received packet can be found in hashmap
        type direction: str
        type protocol: str
        type port: integer
        type ip: str
        rtype: boolean
        """
        if self.translate(direction, protocol, port, ip) in self.rules:
            return True
        else:
            return False
        
    
if __name__ == "__main__":
    path = "./rules.csv"
    firewall = Firewall(path)
    # get a csv file for testcase
    # simple tests
    print(firewall.accept_packet("inbound","tcp",80,"192.168.1.2"))
    print(firewall.accept_packet("inbound","udp",53,"192.168.2.5"))
    print(firewall.accept_packet("inbound","udp",53,"192.168.1.5"))     
    print(firewall.accept_packet("outbound","tcp",10001,"192.168.10.11"))         
    


# idea 2 - current implemented one
# we put everything in hashmap.
# space complexity O(n)
# for ranges we iterate through ranges and put them in hashmap.
# have to maintain a huge hashmap but benefit is O(1) query speed for accept_packet
