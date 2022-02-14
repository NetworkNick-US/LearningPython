import netmiko
import getpass


class Cisco:

    def __init__(self, hostname, ip, device_type, username, password):

        self.hostname == hostname
        self.connection_data = {
            'ip' : ip,
            'device_type': device_type,
            'username': username,
            'password': password
        }

        def login(self)
            return netmiko.ConnectHandler(**self.connection_data)

UN = input("Enter your username: ")
PW = getpass.getpass("Enter your password: ", stream=None)
Core_RTR = Cisco("Core1", "192.168.255.1", "IOS XE", UN, PW)
Office_Switch = Cisco("SWITCH1", "192.168.255.2", "IOS XE", UN, PW)

Core_RTR_connection = Core_RTR.login()
Office_Switch = Office_Switch.login()