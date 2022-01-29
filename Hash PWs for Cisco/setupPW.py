import os,subprocess,getpass,platform

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

try:
    os.system("")
    print("This script will help you hash a password for use with your Ansible playbooks for IOS and IOS XE devices.\n", style.RED, "PLEASE NOTE: CURRENTLY NXOS_USER REQUIRES CLEAR-TEXT PASSWORDS", style.RESET)
    salt = getpass.getpass(prompt="Please enter a random string as your salt: ", stream=None)
    userpasswd = getpass.getpass(prompt="Password: ", stream=None)
    hashedPass = subprocess.getoutput("openssl passwd -salt " + salt + " -1 " + userpasswd)
    print("The value you should be using for your variable 'fallbackAdminPW' is: " + hashedPass)
    input(style.BLUE + "\n\nVisit NetworkNick.___ for more Ansible and Python tools!\n\n" + style.RESET)

except KeyboardInterrupt:
    clearConsole()
    print(style.RED + "KeyboardInterrupt. Exiting script." + style.RESET)