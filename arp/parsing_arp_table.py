import re

def parse_arp_table(filename):
    ip_to_mac = {}
    mac_to_ip = {}

    with open(filename, "r") as file:
        lines = file.readlines()

    
    reading_arp_table = False

    for line in lines:
    
        if "Command: show arp" in line:
            reading_arp_table = True
            continue
        
        if "Command:" in line:
            reading_arp_table = False

        if reading_arp_table and line.strip():
            match = re.search(r"Internet\s+(\d+\.\d+\.\d+\.\d+)\s+\S+\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})", line)
            if match:
                ip_address = match.group(1)
                mac_address = match.group(2)

                ip_to_mac[ip_address] = mac_address
                mac_to_ip[mac_address] = ip_address

    return ip_to_mac, mac_to_ip

ip_to_mac, mac_to_ip = parse_arp_table("device_output.txt")

print(ip_to_mac.get("10.6.0.6"))
print(mac_to_ip.get("cc98.91f1.79f6"))

