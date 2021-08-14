import yaml
from pprint import pprint

# Per device, define a dict with keys device_name and host
cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io"}
cisco4 = {"device_name": "cisco4", "host": "cisco4.lasthop.io"}
nxos1 = {"device_name": "nxos1", "host": "nxos1.lasthop.io"}
nxos2 = {"device_name": "nxos2", "host": "nxos2.lasthop.io"}

# Create a list of dicts
device_list = [cisco3, cisco4, nxos1, nxos2]

print()
print("######### This is my original list of dicts #########")
print()
pprint(device_list)
print()

# Addend each dict in the list with the key/vaule pairs for username and password
for device in device_list:
    device["username"] = "admin"
    device["password"] = "password"

print()
print("######### This is my updated list of dicts #########")
print()
pprint(device_list)
print()

# Open a new file and write the list of dicts to it in YAML format:
with open("/home/dmoynihan/PyPlus_DJ/Class3_exercises/my_devices.yml", "w") as f:
    yaml.dump(device_list, f, default_flow_style=False)

print()
print("######### Import this new YAML file and then printing the output #########")
print()
filename = "/home/dmoynihan/PyPlus_DJ/Class3_exercises/my_devices.yml"
with open(filename) as f:
    yaml_out = yaml.load(f, Loader=yaml.SafeLoader)
print(yaml_out)

print()
print("######### Again import this new YAML file and then printing the output #########")
print()

yml_file = open(filename)
for line in yml_file:
    print(line.strip())