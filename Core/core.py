import netmiko

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