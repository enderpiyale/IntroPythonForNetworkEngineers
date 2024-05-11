from netmiko import ConnectHandler
from getpass import getpass

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.8',
    'username':'admin',
    'password': getpass()
}

connection = ConnectHandler(**device)

output = connection.send_command('show clock')

connection.disconnect()
print(output)