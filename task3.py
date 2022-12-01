#importing ConnectHandler from netmimo to connect to the 2 routers
from netmiko import ConnectHandler 
#credentials to connect to router 1
iosv_R1 = { 
    'device_type': 'cisco_ios',
    'ip': '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
    
}
#credentials to connect to router 2

iosv_R2 = { 
    'device_type': 'cisco_ios',
    'ip': '192.168.56.130',
    'username': 'cisco',
    'password': 'cisco123!',
    
}
#opening the router ospf file that contains the info for the configuration
with open('router_ospf') as f:
    lines = f.read().splitlines()
#putting the two routers into a dictionary and storing it into all_devices
all_devices = [iosv_R1, iosv_R2]
#created the for loop and called the all_devices dictionary to configure the two routers
for devices in all_devices:
    net_connect = ConnectHandler(**devices) #using the ConnectHandler and storing it into the net_connect variable
    output = net_connect.send_config_set(lines) #sending the notepad configuration into the net_connect and storing it into the output variable
    print(output) #printing out the configuration



