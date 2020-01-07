import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

requests.packages.urllib3.disable_warnings()

headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

user = 'developer'
password = getpass("'developer' password: ")

res = requests.get(
    'https://ios-xe-mgmt.cisco.com:9443/restconf/data/native/interface/',
    headers=headers,
    auth=HTTPBasicAuth(user, password),
    verify=False)

interfaces = res.json()['Cisco-IOS-XE-native:interface']

for int_type in interfaces.keys():
    for int_name in interfaces[int_type]:
        print(f'--- {int_type}{int_name["name"]}:')
        print(f'      description {int_name["description"]}')
        if 'ip' in int_name:
            print(
                f"      ip address {int_name['ip']['address']['primary']['address']} {int_name['ip']['address']['primary']['mask']}")
