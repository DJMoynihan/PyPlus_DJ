import os
from netmiko import ConnectHandler
from pprint import pprint

# Credentials are imported from the following file:
import my_credentials as credentials

# Here I define the basic Netmiko parameters for the Cisco Nexus devices.
device1 = {
    "device_type": "cisco_nxos",
    "host":   "nxos1.lasthop.io",
    "username": credentials.username,
    "password": credentials.password,
    "fast_cli": True,
}

device2 = {
    "device_type": "cisco_nxos",
    "host":   "nxos2.lasthop.io",
    "username": credentials.username,
    "password": credentials.password,
    "fast_cli": True,
}

devices = [device1, device2]

for device in devices:

    net_connect = ConnectHandler(**device)
    print("The device prompt is: " + str(net_connect.find_prompt()))

    output = net_connect.send_config_from_file(
        config_file="nxos_vlans.txt")
    
    pprint(output)
    
    save_out = net_connect.save_config()
    pprint(save_out)

    net_connect.disconnect()