import os
from netmiko import ConnectHandler

# Credentials are imported from the following file:
import my_credentials as credentials

# Here I define the basic Netmiko parameters for the Cisco Nexus devices.
cisco4 = {
    'device_type': 'cisco_ios',
    'host':   ' cisco4.lasthop.io',
    'username': credentials.username,
    'password': credentials.password,
}


net_connect = ConnectHandler(**cisco4)
print("The device prompt is: " + str(net_connect.find_prompt()))

output = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
    )
output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False
    )
output += net_connect.send_command_timing(
        "8.8.8.8", strip_prompt=False, strip_command=False
    )
output += net_connect.send_command_timing(
        "5", strip_prompt=False, strip_command=False
    )
output += net_connect.send_command_timing(
    "100", strip_prompt=False, strip_command=False
    )
output += net_connect.send_command_timing(
    "2", strip_prompt=False, strip_command=False
    )
output += net_connect.send_command_timing(
    "n", strip_prompt=False, strip_command=False
    )
output += net_connect.send_command_timing(
    "n", strip_prompt=False, strip_command=False
    )


print(output)


net_connect.disconnect()