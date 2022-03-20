import getpass
import sys
from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException as AuthenticationFailure

try:
    connection = ConnectHandler('192.169.255.1', username='cisco', password='supersecure', device_type='cisco_ios')
except AuthenticationFailure as e:
    output = e
    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    connection = ConnectHandler('192.169.255.1', username=username, password=password, device_type='cisco_ios')
finally:
    print(output)
    print(connection.send_command('show run'))