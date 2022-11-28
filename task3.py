from netmiko import ConnectHandler 

iosv_R1 = { 
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'cisco',
    'password': 'cisco123!',
    
}

iosv_R2 = { 
    'device_type': 'cisco_ios',
    'ip': '192.168.1.2',
    'username': 'cisco',
    'password': 'cisco123!',
    
}

with open('router_ospf') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv_R1, iosv_R2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
