import getpass
import os
import platform
import subprocess


class Style:
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
    clear_con = 'cls' if platform.system().lower() == "windows" else 'clear'
    os.system(clear_con)


def hashPass(salted, pwd):
    return subprocess.getoutput("openssl passwd -salt " + salted + " -1 " + pwd)


def main():
    os.system("")
    print("This script will help you hash a password for use with your Ansible playbooks for IOS and IOS XE devices.\n",
          Style.RED, "PLEASE NOTE: CURRENTLY NXOS_USER REQUIRES CLEAR-TEXT PASSWORDS", Style.RESET)
    salt = getpass.getpass(prompt="Please enter a random string as your salt: ", stream=None)
    userpasswd = getpass.getpass(prompt="Password: ", stream=None)
    print("The value you should be using for your variable 'fallbackAdminPW' is: " + hashPass(salt, userpasswd))
    print(Style.BLUE + "\nVisit NetworkNick.us for more Ansible and Python tools!\n" + Style.RESET)


if __name__ == '__main__':
    main()
