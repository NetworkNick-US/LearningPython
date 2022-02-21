# PythonScripts
A collection of my scripts as I use Python to solve some basic tasks! This collection is not maintained for production use but is instead catered for my testing and learning/development.

## Scripts

| Script                                                                                                           | Features                                                                                                                          | Status |
|:-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------|
| [Microcenter Web Scraper](https://github.com/NetworkNick-io/Python-Projects/tree/main/MicroCenterWebScraper)     | In-stock alert script for items at Microcenter. Incorporates Twilio for SMS based notification in addition to command line output | ✔️     |
| [Network Monitor](https://github.com/NetworkNick-io/Python-Projects/tree/main/ICMPmonitor)                       | Basic ICMP monitoring script that prints device status to the command-line                                                        | ✔️     |
| [Cisco PW Hasher](https://github.com/NetworkNick-US/PythonScripts/blob/main/Hash%20PWs%20for%20Cisco/setupPW.py) | Basic script to hash passwords (MD5) for use on Cisco IOS and IOS XE Ansible playbooks.                                           | ✔️     |

## NetMiko Scripts
| Script              | Features                                                                                                  | Status |
| :-------------      |-----------------------------------------------------------------------------------------------------------|-------| 
| [Network Port Bouncer](https://github.com/NetworkNick-US/LearningPython/blob/main/CiscoPortBouncer/bouncePort.py) | Reset a port that has been tripped by port-security                                                       | ✔️    |
| [Running Config and Local Log](https://github.com/NetworkNick-US/PythonScripts/blob/main/Netmiko/getRunLog.py) | Connect to a network device and print the running config and the log. Depricated - use [Configuration Backup](https://github.com/NetworkNick-US/PythonScripts/blob/main/Netmiko/backupConfig.py)                   | -️    |
| [Get Interface list](https://github.com/NetworkNick-US/PythonScripts/blob/main/Netmiko/GetInts.py) | Connect to a device and parse the interfaces into a basic list                                            | ✔️    |
| [Hostnames](https://github.com/NetworkNick-US/PythonScripts/blob/main/Netmiko/getHostname.py) | Given a list of IP addresses, get device hostnames and create a directory for each                        | ✔️    |
| [Configuration Backup](https://github.com/NetworkNick-US/PythonScripts/blob/main/Netmiko/backupConfig.py) | Backs up the output of 'show run' and 'show log' to a local file. Iterated over a list of management addresses | ✔️    |
| [Get Version and Uptime](https://github.com/NetworkNick-US/PythonScripts/blob/main/Netmiko/getVersion.py) | Gets the version and uptime from a list of network devices and returns it in a human readable table. |  ✔️    |