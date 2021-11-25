import json, datetime, os, platform, subprocess, time 

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

def openHostList(listname, timer):
    with open(listname) as json_dictionary:
        dictionaryVariable = json.load(json_dictionary)
    LN = listname.split(".")
    print(style.BLUEBACKGROUND + "Pinging {}".format(LN[0]) + style.RESET)
    for host in dictionaryVariable:
        pingHost(dictionaryVariable, host)
    print("\n")
    time.sleep(timer)    
    
def pingHost(dictionaryName, host):
    pingParam = '-n' if platform.system().lower() == "windows" else '-c'
    pingCommand = ['ping', pingParam, '1', dictionaryName[host]]
    pingResponse = subprocess.Popen(pingCommand, stdout=subprocess.DEVNULL)
    pingResponse.wait()
    if pingResponse.returncode == 0:
        print(style.GREEN + "{} is up".format(host.upper()) , "at" , dictionaryName[host])
    else:
        print(style.RED + "{} is unreachable".format(host.upper()), "at", dictionaryName[host])
    
try:
    os.system("")
    while(True):
        openHostList("Home Devices.json",5)
        
except KeyboardInterrupt:
    clearConsole()
    print("KeyboardInterrupt. Exiting script." + style.RESET) 