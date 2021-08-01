import os
from netmiko import ConnectHandler
from pprint import pprint
from datetime import datetime
# Credentials are imported from the following file:
import my_credentials as credentials

# Here I define the basic Netmiko parameters for the Cisco Nexus devices.
device_False = {
    "device_type": "cisco_ios",
    "host":   "cisco3.lasthop.io",
    "username": credentials.username,
    "password": credentials.password,
    "fast_cli": False,
}

device_True = {
    "device_type": "cisco_ios",
    "host":   "cisco3.lasthop.io",
    "username": credentials.username,
    "password": credentials.password,
    "fast_cli": True,
}

devices = [device_False,device_True]

for device in devices:

    net_connect = ConnectHandler(**device)
    print("The device prompt is: " + str(net_connect.find_prompt()))


    commands = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]
    start_time = datetime.now()

    output = net_connect.send_config_set(
        config_commands=commands, strip_prompt=False, strip_command=False
    )

    ping_output = net_connect.send_command("ping google.com")
    if "!!" in ping_output:
        print("Ping Successful:")
        print("\n\nPing Output: {}\n\n".format(ping_output))
    else:
        raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))
    
    
    end_time = datetime.now()
    print("\n\n*******Execution Time : {}".format(end_time - start_time))
    
    net_connect.disconnect()


