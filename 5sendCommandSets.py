from netmiko import ConnectHandler
from getpass import getpass

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.8',
    'username':'admin',
    'password': getpass()
}

connection = ConnectHandler(**device)

#output = connection.send_command('configure terminal', expect_string=r"#")
#output += connection.send_command('ip dns server-address 8.8.8.8')
#output += connection.send_command('write mem')

commands = ['vlan 2', 'int vlan 2', 'ip address 10.0.0.8/24']

#for c in commands:
#    connection.send_command(c)

output = connection.send_config_set(commands, delay_factor=2)
output += connection.send_command('write mem')

connection.disconnect()
print(output)