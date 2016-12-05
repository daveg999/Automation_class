#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': password,
}

juniper_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': password,
    'secret': '',
}

arista = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.75',
    'username': 'admin1',
    'password': '99saturday',
    'eapi_port': 443,
}

pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr1.find_prompt()
pynet_rtr1.config_mode()
pynet_rtr1.check_config_mode()
pynet_rtr1.find_prompt()
pynet_rtr1.exit_config_mode()
pynet_rtr1.find_prompt()

output = pynet_rtr1.send_command("sho ip int br")
print output

# paging automatically disabled and output cleaned up
output = pynet_rtr1.send_command("sho ver")
print output

