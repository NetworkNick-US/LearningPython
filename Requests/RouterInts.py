import requests
from bs4 import BeautifulSoup


def get_interface_info(to_terminal=False):
    api_root = "https://192.168.255.1:443/restconf"
    dn = "/data/Cisco-IOS-XE-native:native/interface/"

    response = requests.get(api_root + dn, auth=("MyUsername", "MyPassword"),
                            verify=False)
    if to_terminal:
        print(response.content.decode('utf-8'))
    else:
        return response.content


def main():
    xml_data = get_interface_info()
    read = BeautifulSoup(xml_data, 'lxml')
    for intf in read.find_all("gigabitethernet"):
        print("=" * 50)
        print("GigabitEthernet", intf.find('name').string)
        print(intf.ip.primary.address.string)


if __name__ == "__main__":
    main()
