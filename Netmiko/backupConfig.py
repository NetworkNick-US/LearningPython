import netmiko
import os


class CiscoIOS:

    def __init__(self, ip, port=22, username=None, password=None, device_type='cisco_ios'):
        self.connect = netmiko.ConnectHandler(ip=ip, port=port, username=username, password=password,
                                              device_type=device_type)
        cmd1 = self.connect.send_command('show run | inc hostname')
        self.hostname = cmd1.split()[-1]

    def get_run_cfg(self):
        running_configuration = self.connect.send_command('show run')
        return running_configuration

    def get_log(self):
        lcl_log = self.connect.send_command('show log')
        return lcl_log


def main():
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
        if not (os.path.exists(specific_directory)) and os.path.isdir(specific_directory):
            os.mkdir(specific_directory)
        network_data = {
            'running_config': network_device.get_run_cfg(),
            'log': network_device.get_log(),
        }
        for contents in network_data:
            filename = specific_directory + contents + '.txt'
            with open(filename, 'a') as f:
                f.write('=' * 50 + '\n')
                f.write('-' * 50 + '\n')
                f.write('=' * 50 + '\n')
                f.write(network_data[contents])


if __name__ == '__main__':
    main()
