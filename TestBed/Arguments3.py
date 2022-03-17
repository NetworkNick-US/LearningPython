import sys
import argparse
import netmiko

class Cisco:











class Cisco_CLI(Cisco):

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-ip',
            type=str,
            help="IP address for the target network device"
        )
        parser.add_argument(
            '--port',
            type=int,
            default=22,
            help="SSH port to use for connection"
        )
        parser.add_argument(
            '-u', '--username',
            type=str,
            default = 'admin',
            help="Username to use for connection"
        )
        parser.add_argument(
            '-p', '--password',
            type=str,
            default='admin',
            help="Password to use for the connection"
        )
        parser.add_argument(
            '--device_type',
            type=str,
            default="cisco_ios",
            help="Device type of the appliance"
        )

        args = parser.parse_args()
        ip = args.ip
        port = args.port
        username = args.username
        password = args.password
        device_type = args.device_type
        self.connect = netmiko.ConnectHandler(ip=ip, port=port, username=username, password=password,
                                              device_type=device_type))
