import json, requests, datetime, os, platform, subprocess, time

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

def alert(deviceName):
    successMessage = style.WHITE + "[" + style.GREEN + time.strftime("%I:%M%p") + style.WHITE + "] "
    print(successMessage + "OPEN BOX UNIT: " + deviceName)

def findGPUS(targets):
    with open(targets) as json_target:
        localDictionary = json.load(json_target)
    for devices in localDictionary:
        if(scrapeWebpage(devices,localDictionary)):
            alert(devices)
        
def scrapeWebpage(device,lcldictionary):
    getWebpage = requests.get(lcldictionary[device])
    if "<Response [200]>" not in str(getWebpage):
        print(commError + " Could not locate: " + device)
    elif "ob=1&storeid=121" in str(getWebpage.text):
        #store 121 is in Cambridge, MA 
        return True
    elif "ob=1&storeid=029" in str(getWebpage.text): 
        #store 029 indicates the device is shipable
        return True
    else:
        return False 

try:
    commError = style.WHITE + "[" + style.RED + "ERROR" + style.WHITE + "]"
    iterationCounter = 0
    os.system("")
    while(True):
        findGPUS("TargetDevices.json")
        iterationCounter += 1
        print(style.WHITE + "\n" + "We have checked the list " + str(iterationCounter) + " time(s)\n")
        time.sleep(1)
        
except KeyboardInterrupt:
    print(style.RED + "KeyboardInterrupt. Exiting script." + '\x1b[0m')
