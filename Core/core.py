import netmiko
import getpass


class CiscoBase:

    def __init__(self, hostname, ip, device_type, username, password):

        self.hostname = hostname
        self.connection_data = {
            'ip': ip,
            'device_type': device_type,
            'username': username,
            'password': password
        }

    def login(self):
        self.connect = netmiko.ConnectHandler(**self.connection_data)

class CiscoIOSXE(CiscoBase):

    def show_run(self):
        return self.connect.send_command("show run")

    def show_log(self):
        return self.connect.send_command("show log")


UN = input("Enter your username: ")
PW = getpass.getpass("Enter your password: ", stream=None)
Core_RTR = CiscoIOSXE("Core1", "192.168.255.1", "IOS XE", UN, PW)

Core_RTR.login()
print(Core_RTR.show_run())
print(Core_RTR.show_log())
