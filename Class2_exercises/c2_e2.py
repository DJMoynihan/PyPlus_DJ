import os
from netmiko import ConnectHandler
from datetime import datetime


# Credentials are imported from the following file:
import my_credentials as credentials

# Here I define the basic Netmiko parameters for the Cisco Nexus devices.
device = {
    "device_type": "cisco_nxos",
    "host":   "nxos2.lasthop.io",
    "username": credentials.username,
    "password": credentials.password,
    "global_delay_factor": 2,
}


net_connect = ConnectHandler(**device)
print("The device prompt is: " + str(net_connect.find_prompt()))

command = "show lldp neighbors detail"

start_time = datetime.now()
output1 = net_connect.send_command(
    command, strip_prompt=False, strip_command=False
    )
end_time = datetime.now()
print("#" * 80)
print(output1)
print("#" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()

start_time = datetime.now()
output2 = net_connect.send_command(
    command, delay_factor=8, strip_prompt=False, strip_command=False
    )
end_time = datetime.now()
print("#" * 80)
print(output2)
print("#" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()

net_connect.disconnect()