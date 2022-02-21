import netmiko
import pandas


class CiscoIOS():

    def __init__(self, ip, port=22, username=None, password=None, device_type='cisco_ios'):
        self.connect = netmiko.ConnectHandler(ip=ip, port=port, username=username, password=password,
                                              device_type=device_type)
        _ = self.connect.send_command('show run | inc hostname')
        self.hostname = _.split()[-1]

    def get_IOS_version(self, key=''):
        self.version_data = self.connect.send_command('show version', use_textfsm=True)
        if key:
            return self.version_data[key]
        else:
            return self.version_data[0]


managed_devices = [
    '192.168.255.1',
    '192.168.255.2',
    '192.168.255.3',
    '192.168.255.4',
    '192.168.255.5',
    '192.168.255.6',
    '192.168.255.7',
]

def main():
    network_devices = []
    version_list = []
    uptime_list = []
    for ip in managed_devices:
        net_connection = CiscoIOS(ip, username="MyUsername", password="MyPassword")
        sh_version = net_connection.get_IOS_version()
        hostname = sh_version['hostname']
        version = f"{sh_version['rommon']} {sh_version['version']}"
        uptime = sh_version['uptime']
        network_devices.append(hostname)
        version_list.append(version)
        uptime_list.append(uptime)

    network_data = pandas.DateFrame()
    network_data['hostname'] = network_devices
    network_data['version'] = version_list
    network_data['uptime'] = uptime_list
    print(network_data)

if __name__ == '__main__':
    main()
