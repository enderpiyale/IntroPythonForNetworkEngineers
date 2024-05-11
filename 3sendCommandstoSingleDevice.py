from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.8',
    'username':'admin',
    'password':'Netsys'
}

connection = ConnectHandler(**device)

output = connection.send_command('configure terminal', expect_string=r"#")
output += connection.send_command('ip dns server-address 8.8.8.8')
output += connection.send_command('write mem')

connection.disconnect()
print(output)