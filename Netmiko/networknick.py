import netmiko


class Cisco:

    def __init__(self, ip, port=22, username=None, password=None, device_type='cisco_ios'):
        self.connect = netmiko.ConnectHandler(ip=ip, port=port, username=username,
                                              password=password, device_type=device_type)
        _ = self.connect.send_command('show run | inc hostname')
        self.hostname = _.split()[-1]

    def get_output(self, command='show run', textFSM=False):
        return self.connect.send_command(command, use_textFSM=textFSM)

    def save_config(self):
        self.connect.send_command('copy run start')
        self.connect.send_command('')

    def get_version(self, key=''):
        self.version_data = self.connect.send_command('show version', use_textfsm=True)
        if key:
            return self.version_data[key]
        else:
            return self.version_data[0]

    def logout(self):
        self.connect.disconnect()


class CiscoSwitch(Cisco):

    def interface_status(self, textFSM=False):
        return self.connect.send_command('show interface status', use_textFSM=textFSM)

    def bounce_interface(self, interface):
        bounce_commands = ['interface ' + interface, 'shutdown', 'no shutdown']
        self.connect.config_mode()
        self.connect.send_config_set(bounce_commands)
        self.connect.exit_config_mode()

    def disable_port_sec(self, interface):
        disable_psec = ['interface ' + interface, 'no switchport port-security']
        self.connect.config_mode()
        self.connect.send_config_set(disable_psec)
        self.connect.exit_config_mode()

    def enable_port_sec(self, interface, mode='mac-address sticky', maximum='1'):
        enable_psec = ['interface ' + interface, 'switchport port-security ' + mode,
                       'switchport port-security max ' + maximum, 'switchport port-security']
        self.connect.config_mode()
        self.connect.send_config_set(enable_psec)
        self.connect.exit_config_mode()

    def create_vlan(self, vlan_number='1', vlan_name='NetworkNick'):
        vlan_commands = ['vlan ' + vlan_number, 'name ' + vlan_name]
        self.connect.config_mode()
        self.connect.send_config_set(vlan_commands)
        self.connect.exit_config_mode()


class CiscoRouter(Cisco):

    def ip_int_brief(self, textFSM=False):
        return self.connect.send_command('show ip interface brief', use_textFSM=textFSM)

    def populate_interface_list(self):
        sh_ip_int_brief = self.ip_int_brief(True)
        self.interface_list = []
        for interface in sh_ip_int_brief:
            self.interface_list.append(interface['intf'])
        return self.interface_list


def is_ipv4_address(ip):
    """ Return True if ipv4 address,
    False if not
    """
    octets = ip.split('.')

    if len(octets) != 4:
        return False
    elif any(not octet.isdigit() for octet in octets):
        return False
    elif any(int(octet) < 0 for octet in octets):
        return False
    elif any(int(octet) > 255 for octet in octets):
        return False

    return True
