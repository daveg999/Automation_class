#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': password,
}

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
}

dev_list = [
    pynet1,
    pynet2,
]

for dev in dev_list:
    connect_x = ConnectHandler(**dev)

    print "In device name:"
    dev_name = connect_x.find_prompt()
    print dev_name

    output = connect_x.send_config_from_file(config_file = 'ex8_commands.txt')
    print output

