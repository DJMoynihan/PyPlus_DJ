import os
from netmiko import ConnectHandler

# Credentials are imported from the following file:
import my_credentials as credentials

# Here I define the basic Netmiko parameters for the Cisco IOS device.
device3 = {
    'device_type': 'cisco_ios',
    'host':   'cisco3.lasthop.io',
    'username': credentials.username,
    'password': credentials.password,
}


net_connect = ConnectHandler(**device3)             # Connect to the device.
output = net_connect.send_command("show version")   # Store the output of 'show version' in a variable.

# This is how we write the output to a file.
with open("show_version.txt", "w") as f:
    f.write(output)

net_connect.disconnect()                            # Close connection to the device.