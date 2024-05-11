import netmiko

connection = netmiko.ConnectHandler(host = '192.168.1.8', username = 'admin', password = 'Netsys', device_type = 'cisco_ios')

output = connection.send_command('show clock')

connection.disconnect()

print(output)