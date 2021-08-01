import os
import time
from getpass import getpass
from netmiko import ConnectHandler

# Credentials are imported from the following file:
import my_credentials as credentials


device = {
    "host": "cisco4.lasthop.io",
    "username": credentials.username,
    "password": credentials.password,
    "secret": credentials.password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**device)
print("\nCurrent Prompt: ")
print(net_connect.find_prompt())

print("\nEnter Config Mode, Current Prompt: ")
net_connect.config_mode()
print(net_connect.find_prompt())

print("\nExit Config Mode, Current Prompt: ")
net_connect.exit_config_mode()
print(net_connect.find_prompt())

print("\nExit privileged exec (disable), Current Prompt: ")
net_connect.write_channel("disable\n")
time.sleep(2)
output = net_connect.read_channel()
print(output)

print("\nRe-enter enable mode, Current Prompt: ")
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()
print()