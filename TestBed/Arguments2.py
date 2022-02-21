import sys

class CiscoIOS:

    def __init__(self, ip, port=22, username=None, password=None, device_type='cisco_ios'):
        self.connect = netmiko.ConnectHandler(ip=ip, port=port, username=username, password=password,
                                              device_type=device_type)
        cmd1 = self.connect.send_command('show run | inc hostname')
        self.hostname = cmd1.split()[-1]


def main():
    MyDevice = CiscoIOS(sys.argv[1], username="MyUsername", password="MyPassword")
    print(MyDevice.hostname)

if __name__ == '__main__':
    main()