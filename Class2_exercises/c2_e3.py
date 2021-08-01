import os
from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint
# Credentials are imported from the following file:
import my_credentials as credentials

# Here I define the basic Netmiko parameters for the Cisco Nexus devices.
device = {
    "device_type": "cisco_ios",
    "host":   "cisco4.lasthop.io",
    "username": credentials.username,
    "password": credentials.password,
}


net_connect = ConnectHandler(**device)
print("The device prompt is: " + str(net_connect.find_prompt()))


commands = ["show version", "show lldp neighbors"]

print()
for command in commands:
    output = net_connect.send_command(
        command, use_textfsm=True, strip_prompt=False, strip_command=False
    )
    print("#" * 80)
    print(command)
    print("#" * 80)
    pprint(output)
    print("#" * 80)

    if command == "show lldp neighbors":
        print("LLDP Data Structure Type: {}".format(type(output)))
        print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))

print()
net_connect.disconnect()