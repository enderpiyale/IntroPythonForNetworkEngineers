from netmiko import ConnectHandler
from getpass import getpass
from time import time

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.8',
    'username':'admin',
    'password': getpass()
}

start = time()

connection = ConnectHandler(**device)

commands = ['vlan 2', 'int vlan 2', 'ip address 10.0.0.8/24']

output = connection.send_config_set(commands, delay_factor=2)
output += connection.send_command('write mem')

connection.disconnect()
print(output)

print('Islemin tamamlanma süresi: ', time() - start, ' saniye')