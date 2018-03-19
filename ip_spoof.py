from scapy.all import *
iface = "en0" fake_ip = '00.00.00.00' destination_ip = '250.250.250.250'

def ping(source, destination, iface):
    pkt = IP(src=source,dst=destination)/ICMP()srloop(IP(src=source,dst=destination)/ICMP(), iface=iface)

    try:
        print ("Starting Ping")
        ping(fake_ip,destination_ip,iface)

    except KeyboardInterrupt:
        print("Exiting.. ")
        sys.exit(0)