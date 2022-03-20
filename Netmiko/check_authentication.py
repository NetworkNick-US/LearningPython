import sys
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException as AuthenticationFailure

try:
    connection = ConnectHandler('192.169.255.1', username='cisco', password='supersecure', device_type='cisco_ios')
except AuthenticationFailure as e:
    output = e
    sys.exit()
else:
    output = connection.send_command('show run')
finally:
    print(output)