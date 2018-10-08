I tested my solution with explicit rules and according packet. I also wrote a script to generate random rules.

I used hashmap for O(1) query time complexity for accept_packet function.


# Analysis



naive way to maximize time complexity:
1. each memory location stands for True or False for a specific packet
2. do some math:
256**4 = 2*32 = 32 bit = 4294967296

in/out = 1bit, tcp/udp= 1bit
2**16 = 65536 = 16 bit

if all in memory, 50 bit => 2**50 bit memory =>  2**47 Byte => 2**17TB => 2**7 PB

so 2**7 PB memory if want O(1) time complexity for accept_packet



naive way to maximize space complexity: 
1. check for each rule when receiving a packet
2. do some math for maximize space complexity. 
3. O(n) for space complexity, O(n) time complexity for accept_packet, n is num of rules




Idea 1 Steps:
1. translate in/out tcp/ip port ip to integer
2. accept_packet a range query on a range. rules define ranges.
3. sorted array to get O(logn) with binary search for accept_packet. space complexity O(n)



Idea 2 Steps - current implemented one:
1. translate in/out tcp/ip port ip to integer and put everything in hashmap. space complexity O(n).
2. for ranges we iterate through ranges and put them in hashmap.
3. we have to maintain a huge hashmap but benefit is O(1) query speed for accept_packet


Limitations of current method:
1. if ranges are used a lot in rules, then could lead to super large hashmap, in extreme case, PB level.
2. there must be a way to better integrate ranges, need further thought

Implementation of translate:
bit 1: in/out
bit 2: tcp/udp
bit 3~18: port
bit 19~50: ip


Optimization further
1. check most commonly accessed rules before others to save time. (know queries better)
2. create a cache for most recent checked rule range.
3. look into reference for better compact datastructure. (know rules better)
4. use bloom filter + hashmap + sorted array to further optimize
bloom filter response membership inside array with no or maybe with O(1), so can be first step


[search] packet filtering
Reference for optimization
https://en.wikipedia.org/wiki/Firewall_(computing)
https://www.napier.ac.uk/~/media/worktribe/output-424671/hybrid-treerule-firewall-for-high-speed-data-transmission.pdf
https://www.ijraset.com/fileserve.php?FID=1384
https://www.ics.uci.edu/~eppstein/pubs/EppMut-SODA-01.pdf
https://ieeexplore.ieee.org/document/7052238
https://www.eng.tau.ac.il/~yash/ieeei04-gem.pdf
https://kuscholarworks.ku.edu/bitstream/handle/1808/11462/Clark_ku_0099D_12729_DATA_1.pdf;sequence=1

Geometric Efficient Matching (GEM) algorithm:
1. logarithmic matching time performance, easily beating the linear time required by the naive matching algorithm.
2. algorithm’s theoretical worst-case space complexity is O(n4) for a rule-base with n rules.

py-pf:
1. a pure-Python module that allows you to manage OpenBSD's Packet Filter from Python scripts. 
2. Packet Filter is OpenBSD's firewalling subsystem, renowned for its performance and security and providing, among other features.


# My rank of interested team:
1. Platform Team
2. Policy Team
3. Data Team

