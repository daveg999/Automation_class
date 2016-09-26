#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
}

pynet_rtr2 = ConnectHandler(**pynet2)
output = pynet_rtr2.find_prompt()
print "Current prompt:"
print output
print

config_commands = ['logg buff 88888']
pynet_rtr2.send_config_set(config_commands)

output = pynet_rtr2.send_command('sho run | i logg')
print output
print

output = pynet_rtr2.find_prompt()
print output
print
