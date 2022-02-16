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


class NetworkLogger:

    def __init__(self, file_name):
        self.log_file = str(file_name)

    def log(self, data):
        with open(self.log_file, 'a') as f:
            f.write("=" * 50 + '\n')
            f.write(data + '\n')
            f.write("=" * 50 + '\n')


# Collect credentials to use with the network device.
UN = input("Enter your username: ")
PW = getpass.getpass("Enter your password: ", stream=None)
Core_RTR = CiscoIOSXE("Core1", "192.168.255.1", "IOS XE", UN, PW)
# Connect, create log file and save the output of the commands
Core_RTR.login()
important_data = NetworkLogger("backup.txt")
important_data.log(str(Core_RTR.show_run()))
important_data.log(str(Core_RTR.show_log()))
