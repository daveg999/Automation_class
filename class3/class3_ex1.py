#!/usr/bin/env python

import json
import snmp_helper
import datetime

SNMP_PORT   = 161
username    = 'pysnmp'
auth_key    = 'galileo1'
encrypt_key = 'galileo1'

snmp_user = (username, auth_key, encrypt_key)

device_list = (
    ('184.105.247.70'),
    ('184.105.247.71'),
)

snmp_oids = (
    ('sys_name', '1.3.6.1.2.1.1.5.0', None),
    ('sys_run-change-time', '1.3.6.1.4.1.9.9.43.1.1.1.0', None),
    ('sys_run-save-time', '1.3.6.1.4.1.9.9.43.1.1.2.0', None),
    ('sys_start-save-time', '1.3.6.1.4.1.9.9.43.1.1.3.0', None),
)

# send snmp data to file
def snmp_data_file(file_name, snmp_dump):

    with open(file_name, 'w') as data:
        json.dump(snmp_dump, data)

# send email when configs change
def send_email(device_name):

    current_time = datetime.now()
    email_from = 'sender@twb-tech.com'
    email_to = 'davegrice@comcast.net'
    subject = 'device {0} config changed'.format(device_name)
    message = '''
The running config of {0} was changed.

This change was detected at:  {1}

'''.format(device_name, current_time)

    if send_mail(email_to, subject, message, email_from):
        print 'Email notification sent to {}'.format(recipient)
        return True

# main routine
def main():

    saved_devices = obtain_saved_objects(net_dev_file)
    print "{0} devices were already saved\n".format(saved_devices)

    current_devices = {}

    for device in device_list:
        device = (device, SNMP_PORT)
        for desc,oid,counter in snmp_oids:
            snmp_data = snmp_helper.snmp_get_oid_v3(device, snmp_user, oid)
