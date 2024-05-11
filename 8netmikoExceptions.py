import netmiko
from time import time

username = 'admin'
password = 'Netsys'

#device = {
#    'device_type': 'cisco_ios',
#    'ip': '192.168.1.8',
#    'username': username,
#    'password': password
#}

#devices = dict()
#devices["SW1"] = {"device_type":"cisco_ios", "ip":"192.168.1.1", "username":username, "password":password}
#devices["SW2"] = {"device_type":"cisco_ios", "ip":"192.168.1.2", "username":username, "password":password}
#devices["SW3"] = {"device_type":"cisco_ios", "ip":"192.168.1.3", "username":username, "password":password}
#devices["SW4"] = {"device_type":"cisco_ios", "ip":"192.168.1.4", "username":username, "password":password}
#devices["SW5"] = {"device_type":"cisco_ios", "ip":"192.168.1.5", "username":username, "password":password}
#devices["SW6"] = {"device_type":"cisco_ios", "ip":"192.168.1.6", "username":username, "password":password}
#devices["SW7"] = {"device_type":"cisco_ios", "ip":"192.168.1.7", "username":username, "password":password} 
#devices["SW8"] = {"device_type":"cisco_ios", "ip":"192.168.1.8", "username":username, "password":password}

devices = {
    "SW1":{
        "device_type":"cisco_ios",
        "ip":"192.168.1.1",
        "username":username,
        "password":password
    },
    "SW2":{
        "device_type":"cisco_ios",
        "ip":"192.168.1.2",
        "username":username,
        "password":password
    },
    "SW3":{
        "device_type":"cisco_ios",
        "ip":"192.168.1.3",
        "username":username,
        "password":password
    },
    "SW4":{
        "device_type":"cisco_ios",
        "ip":"192.168.1.4",
        "username":username,
        "password":password
    },
    "SW5":{
        "device_type":"cisco_ios",
        "ip":"192.168.1.5",
        "username":username,
        "password":password
    },
    "SW6":{
        "device_type":"cisco_ios",
        "ip":"192.168.1.6",
        "username":username,
        "password":password
    },
    "SW7":{
        "device_type":"cisco_ios",
        "ip":"192.168.1.7",
        "username":username,
        "password":password
    },
    "SW8":{
        "device_type":"cisco_ios",
        "ip":"192.168.1.8",
        "username":username,
        "password":password
    },
}

start = time()

netmiko_exceptions = (netmiko.exceptions.AuthenticationException, netmiko.exceptions.NetmikoTimeoutException)

for device in devices:
    try:
        print('Connecting to device', device)
        netconnect = netmiko.ConnectHandler(**devices[device])
        
        commands = ['vlan 20',  'int vlan 20', 'ip address 10.20.0.8/24']

        output = netconnect.send_config_set(commands, delay_factor=2)
        output += netconnect.send_command('write memory')


        print(output)
        print("=" * 80)

        netconnect.disconnect()
        
    except netmiko_exceptions as e:
        print('Failed to', device, e)


print('Islemin tamamlanma süresi: ', time() - start, ' saniye')