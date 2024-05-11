from netmiko import ConnectHandler
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

for device in devices:
    netconnect = ConnectHandler(**devices[device])

    output = netconnect.send_command('show clock')

    netconnect.disconnect()

    print(device, '\n', output)
    print("=" * 80)

print('Islemin tamamlanma süresi: ', time() - start, ' saniye')