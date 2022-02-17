import json
import os
import platform
import subprocess
import time


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


def clear_console():
    clear_con = 'cls' if platform.system().lower() == "windows" else 'clear'
    os.system(clear_con)


def open_host_list(list_name, timer):
    with open(list_name) as json_dictionary:
        dictionary_variable = json.load(json_dictionary)
    ln = list_name.split(".")
    print(Style.BLUEBACKGROUND + f"Pinging {ln[0]}" + Style.RESET)
    for host in dictionary_variable:
        ping_host(dictionary_variable, host)
    print("\n")
    time.sleep(timer)


def ping_host(dictionary_name, host):
    ping_param = '-n' if platform.system().lower() == "windows" else '-c'
    ping_command = ['ping', ping_param, '1', dictionary_name[host]]
    ping_response = subprocess.Popen(ping_command, stdout=subprocess.DEVNULL)
    ping_response.wait()
    if ping_response.returncode == 0:
        print(Style.GREEN + f"{host.upper()} is up at", dictionary_name[host])
    else:
        print(Style.RED + f"{host.upper()} is unreachable at", dictionary_name[host])


try:
    os.system("")
    while True:
        open_host_list("Home Devices.json", 5)

except KeyboardInterrupt:
    clear_console()
    print(Style.RED + "KeyboardInterrupt. Exiting script." + Style.RESET)
