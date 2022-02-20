import netmiko
import os


class CiscoIOS:

    def __init__(self, ip, port=22, username=None, password=None, device_type='cisco_ios'):
        self.connect = netmiko.ConnectHandler(ip=ip, port=port, username=username, password=password,
                                              device_type=device_type)
        cmd1 = self.connect.send_command('show run | inc hostname')
        self.hostname = cmd1.split()[-1]


ip_list = [
    '10.1.1.1',
    '10.2.2.2',
    '10.3.3.3',
]

device_list = []

for IP in ip_list:
    net_connection = CiscoIOS(IP, username='MyUsername', password='MyPassword')
    device_list.append(net_connection)

for network_device in device_list:
    base_directory = os.getcwd() + '/network/'
    specific_directory = base_directory + network_device.hostname + '/'
    os.mkdir(specific_directory)
