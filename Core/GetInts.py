import netmiko

class CiscoBase:

    
    def __init__(self, hostname, ip, device_type=None, username=None, password=None):
        
        self.hostname = hostname
        self.connection_data = {
            'ip': ip,
            'device_type': device_type,
            'username': username,
            'password': password
        }

    def login(self):
        
        return netmiko.ConnectHandler(**self.connection_data)


class CiscoRTR(CiscoBase):

    
    def populate_interface_list(self):

        connect = self.login()
        sh_ip_int_brief = connect.send_command("show ip int brief", use_textfsm=True)
        interface_list = []
        for int in sh_ip_int_brief:
            self.interface_list.append(interface['int'])

            
CoreRTR = CiscoRTR("Core1", "192.168.255.254", "cisco-ios", "localAdmin", "SuperSecure123!!")
CoreRTR.populate_interface_list()
print(CoreRTR.interface_list))
