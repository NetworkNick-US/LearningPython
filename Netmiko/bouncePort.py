import getpass
import os
import platform
import time

from netmiko import ConnectHandler


class style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BLUEBACKGROUND = '\x1b[1;37;46m'


def clearConsole():
    clearCon = 'cls' if platform.system().lower() == "windows" else 'clear'
    os.system(clearCon)


def collectInfo():
    # collect real device information
    print(style.BLUEBACKGROUND + "\n----Please enter your credentials to the network device----\n" + style.RESET)
    networkDevice['host'] = input("Please enter the IP address or hostname of the network device: ")
    networkDevice['username'] = input("Enter your username: ")
    networkDevice['password'] = getpass.getpass("Enter your password: ", stream=None)
    networkDevice['secret'] = getpass.getpass("Enter the device's enable password: ", stream=None)
    print(style.BLUEBACKGROUND + "\nPlease enter the interface that you wish to bounce." + style.RESET)
    networkDevice['inter'] = "interface " + input("Please note - you can use acceptable abbreviations Gi,Te,Eth,etc.: ")


networkDevice = {
    'device_type': 'cisco_ios',
    'host': '192.168.255.10',
    'username': 'un',
    'password': 'pw',
    'port': 22,
    'secret': 'surprise',
    'inter': "Ethernet999",
}

try:
    os.system("")
    collectInfo()
    # start SSH session
    network_connection = ConnectHandler(**networkDevice)

    print(style.BLUE + "We are going to be shutting down " + networkDevice['inter'] +
                        " and waiting 5 seconds before turning it back on" + style.RESET)
    userConfirm = input(style.RED + "WARNING: IF YOUR UPLINK TO THE NETWORK DEVICE USES THE ABOVE INTERFACE,"
                                    "THIS SCRIPT WILL BREAK YOUR CONNECTION TO THE REMOTE DEVICE.\n"
                                    "Please enter 'YES' to confirm that you want to proceed. [NO]\n" + style.RESET)
    if userConfirm.upper() == "YES" or userConfirm.upper() == "Y":
        network_connection.enable()
        network_connection.send_command("configure terminal")
        network_connection.send_command(networkDevice['inter'])
        network_connection.send_command("shutdown")
        print("Shutdown command issued. Waiting 5 seconds before re-enabling the interface.")
        time.sleep(5)
        network_connection.send_command("no shutdown")
        network_connection.send_command("end")
        network_connection.disconnect()
        # Future use - readability - auto-enters config mode but no delay after shutdown:
        # config_commands = [networkDevice['inter'], "shutdown", "no shutdown"]
        # network_connection.send_config_set(config_commands)
    else:
        network_connection.disconnect()
        clearConsole()
        print("Script aborted. No actions have been performed on the remote device")
        print("Feel free to try again... (╯°□°)╯︵ ┻━┻")

except KeyboardInterrupt:
    clearConsole()
    print(style.RED + "KeyboardInterrupt. Exiting script.... (╯°□°)╯︵ ┻━┻" + style.RESET)
