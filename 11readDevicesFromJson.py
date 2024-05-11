import netmiko
from time import time
import json

with open('devices.json') as devfile:
    devices = json.load(devfile)

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