import requests

getpage = requests.get('https://www.microcenter.com/product/637044/dell-xps-8940-gaming-pc-platinum-collection?ob=1')
getpage2 = requests.get('https://www.microcenter.com/product/639253/dell-optiplex-5090-sff-desktop-computer?ob=1')
#print("OPENBOX: \n",getpage.text)
#print("NOT AVAILABLE: \n",getpage2.text)





"""
ob=1&storeid=121 (MA - Cambridge)
ob=1&storeid=029 (shippable item)

ob=1&storeid=101 (CA - Tustin)
ob=1&storeid=181 (CO - Denver)
ob=1&storeid=065 (GA - Duluth)
ob=1&storeid=041 (GA - Marietta)
ob=1&storeid=151 (IL - Chicago)
ob=1&storeid=025 (IL - Westmont)
ob=1&storeid=191 (KS - Overland Park)
ob=1&storeid=085 (MD - Rockville)
ob=1&storeid=125 (MD - Parkville)
ob=1&storeid=055 (MI - Madison Heights)
ob=1&storeid=045 (MN - St. Louis Park)
ob=1&storeid=095 (MO - Brentwood)
ob=1&storeid=075 (NJ - North Jersey)
ob=1&storeid=171 (NY - Westbury)
ob=1&storeid=115 (NY - Brooklyn)
ob=1&storeid=145 (NY - Flushing)
ob=1&storeid=105 (NY - Yonkers)
ob=1&storeid=141 (OH - Columbus)
ob=1&storeid=051 (OH - Mayfield)
ob=1&storeid=071 (OH - Sharonville)
ob=1&storeid=061 (PA - St. Davids)
ob=1&storeid=155 (TX - Houston)
ob=1&storeid=131 (TX - Dallas)
ob=1&storeid=081 (VA - Fairfax)
"""

"""  
    for host in localDictionary:
        print(style.GREEN + "host",host) #returns just the device name
        print("localDictionary",localDictionary) #returns entire entry with {}s 
        print("localDictionary[host]",localDictionary[host]) #returns URL
"""


"""
Environmental Variables

Python Env_Variable:
import os
env_var = input('Please enter environment variable name:\n')
env_var_value = input('Please enter environment variable value:\n')
os.environ[env_var] = env_var_value
 
 
 **temp variables (beginning of each session)**
import os
 
for k, v in os.environ.items():
    print(f'{k}={v}')


 **perm variables**
https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html
""