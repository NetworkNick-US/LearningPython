import netmiko, os, platform, subprocess, time, datetime

class style():
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

networkDevice = {
    'device_type': 'cisco_ios',
    'host':   '192.168.255.10',
    'username': 'un',
    'password': 'pw',
    'port' : 22,
    'secret': 'suprise',
}

try:
    os.system("")
    network_connection = ConnectHandler(**networkDevice)

    print(style.BLUE + "We are going to be shutting down interface {} and waiting 5 seconds before turning it back on".format(suppliedInterface) + style.RESET)
    userConfirm = input(style.RED + "WARNING: IF YOUR UPLINK TO THE NETWORK DEVICE USES THE ABOVE INTERFACE, THIS SCRIPT WILL BREAK YOUR CONNECTION TO THE REMOTE DEVICE.\n Please enter 'YES' to confirm that you want to proceed. [NO]\n" + style.RESET)
    if str(userConfirm).upper() == "YES":
        #Future use - readability but no delay after shutdown:
        #config_commands = [suppliedInterface, "shutdown", "no shutdown"]
        #network_connection.send_config_set(config_commands)
    else:
        clearConsole()
        print("Script aborted. No actions have been performed on the remote device")

except KeyboardInterrupt:
    clearConsole()
    print(style.RED + "KeyboardInterrupt. Exiting script." + style.RESET)