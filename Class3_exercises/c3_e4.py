import json
from pprint import pprint

filename = "/home/dmoynihan/PyPlus_DJ/Class3_exercises/arista_arp.json"
with open(filename) as f:
    arp_data = json.load(f)

arp_dict = {}
arp_entries = arp_data["ipV4Neighbors"]
for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    arp_dict[ip_addr] = mac_addr  # I do not know how this works.......

print()
pprint(arp_dict)
print()