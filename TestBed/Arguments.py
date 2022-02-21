import argparse

myText = 'This will help gather router information'
parser = argparse.ArgumentParser(description=myText)
parser.add_argument('-R', '--router', help='Enter the router\'s hostname')
parser.add_argument('-IP', '--ipaddress', help='Enter the device\'s IP address')

router = parser.parse_args()
print(f'The router\'s hostname is {router.router} and its IP address is {router.ipaddress}')
