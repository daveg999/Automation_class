#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
}

pynet_rtr1 = ConnectHandler(**pynet1)
output = pynet_rtr1.find_prompt()
print "Current prompt:"
print output
print

pynet_rtr1.config_mode()
in_config = pynet_rtr1.check_config_mode()
print "Are we in config mode?"
print in_config
print

output = pynet_rtr1.find_prompt()
print "What does the prompt look like?"
print output
print

pynet_rtr1.exit_config_mode()
output = pynet_rtr1.find_prompt()
print "Leaving config mode"
print output
print
