import os
from netmiko import ConnectHandler

# Credentials are imported from the following file:
import my_credentials as credentials

# Here I define the basic Netmiko parameters for the Cisco Nexus devices.
device1 = {
    'device_type': 'cisco_nxos',
    'host':   ' nxos1.lasthop.io',
    'username': credentials.username,
    'password': credentials.password,
}

device2 = {
    'device_type': 'cisco_nxos',
    'host':   ' nxos2.lasthop.io',
    'username': credentials.username,
    'password': credentials.password,
}

devices = [device1, device2]                # Create a list of devices.

# This little function will run for each device in the list.
# Netmiko will connect to each device in turn, capture the device prompt and print it out to screen.
# Finally the connection to each device is closed before moving onto the next on the list.
for device in devices:
    net_connect = ConnectHandler(**device)
    print("The device prompt is: " + str(net_connect.find_prompt()))
    net_connect.disconnect()