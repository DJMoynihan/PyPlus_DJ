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

output = net_connect.send_command(
    "ping", expect_string=r'Protocol', strip_prompt=False, strip_command=False
    )
output += net_connect.send_command(
    "\n", expect_string=r'Target', strip_prompt=False, strip_command=False
    )
output += net_connect.send_command(
    "8.8.8.8", expect_string=r'Repeat', strip_prompt=False, strip_command=False
    )
output += net_connect.send_command(
    "5", expect_string=r'Datagram ', strip_prompt=False, strip_command=False
    )
output += net_connect.send_command(
    "100", expect_string=r'Timeout ', strip_prompt=False, strip_command=False
    )
output += net_connect.send_command(
    "2", expect_string=r'Extended ', strip_prompt=False, strip_command=False
    )
output += net_connect.send_command(
    "n", expect_string=r'Sweep ', strip_prompt=False, strip_command=False
    )
output += net_connect.send_command(
    "n", expect_string=r'Sending', strip_prompt=False, strip_command=False
    )


print(output)


net_connect.disconnect()