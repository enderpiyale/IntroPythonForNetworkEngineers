import netmiko
from time import time

username = 'admin'
password = 'Netsys'

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
        print('=' * 80)
        netconnect = netmiko.ConnectHandler(**devices[device])
        
        print('Backing up', device)
        print('=' * 80)

        filename = 'backups/' + device + '.txt'
        showrun = netconnect.send_command('sh run')
        showclock = netconnect.send_command('show clock')
    
        output = showclock + '\n' + ('=' * 80) + '\n' + showrun + '\n' + ('#' * 80) + '\n'

        with open(filename, 'a') as f:
            f.write(output)
            
        netconnect.disconnect()
        
    except netmiko_exceptions as e:
        print('Failed to', device, e)


print('Islemin tamamlanma süresi: ', time() - start, ' saniye')