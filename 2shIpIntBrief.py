import netmiko

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.8',
    'username':'admin',
    'password':'Netsys'
}

connection = netmiko.ConnectHandler(**device)

output = connection.send_command('show clock')
output += '\n'
output += connection.send_command('show ip int brief')

connection.disconnect()

print(output)