#!/usr/bin/env python

import snmp_helper

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
    ('sys_uptime', '1.3.6.1.2.1.1.3.0', None),
    ('if_desc_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
    ('if_inoctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
    ('if_inucastpkt_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
    ('if_outoctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
    ('if_outucastpkt_fa4', '1.3.6.1.2.1.2.2.1.17.5', True),
)

for device in device_list:
    device = (device, SNMP_PORT)
    for desc,oid,counter in snmp_oids:
        snmp_data = snmp_helper.snmp_get_oid_v3(device, snmp_user, oid)
        output = snmp_helper.snmp_extract(snmp_data)
        print "{}, {}".format(desc, output)
    print "\n"
