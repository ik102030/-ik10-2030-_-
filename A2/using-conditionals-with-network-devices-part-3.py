# Import required modules/packages/library
from pprint import pprint 

# Display heading
print('')
print('Counts of different OS-types for all devices')
print('--------------------------------------------') 

# Create a dictionary of OS types
os_types = {'Cisco IOS':    {'count': 0, 'devs': []},
            'Cisco Nexus':  {'count': 0, 'devs': []},
            'Cisco IOS-XR': {'count': 0, 'devs': []},
            'Cisco IOS-XE': {'count': 0, 'devs': []}} 

# Read all lines of IP routing information
file = open('devices-06.txt', 'r')
for line in file: 
    
    # Put device info into list
    device_info_list = line.strip().split(',')

    # Put device information into dictionary for this one device
    device_info = {} # Create a dictionary of device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    # Get the device name
    name = device_info['name']
    # Get the OS-type for comparisons
    os = device_info['os-type']

    # Based on the OS-type, increment the count and add name to list
    if os == 'ios':
        os_types['Cisco IOS']['count'] += 1
        os_types['Cisco IOS']['devs'].append(name)
    elif os == 'nx-os':
        os_types['Cisco Nexus']['count'] += 1
        os_types['Cisco Nexus']['devs'].append(name)
    elif os == 'ios-xr':
        os_types['Cisco IOS-XR']['count'] += 1
        os_types['Cisco IOS-XR']['devs'].append(name)
    elif os == 'ios-xe':
        os_types['Cisco IOS-XE']['count'] += 1
        os_types['Cisco IOS-XE']['devs'].append(name)
    else:
        print(" Warning: unknown device type:", os)

# Display the OS types
pprint(os_types)
# Display a blank line to make easier to read
print('') 

# Close the file
file.close() 





