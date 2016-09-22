#!/usr/bin/env python

import snmp_helper

COMM_STRING = "galileo"
SNMP_PORT = 161

ipaddrs = ['184.105.247.70', '184.105.247.71']

snmp_oids = (
    ('sys_name', '1.3.6.1.2.1.1.5.0', None),
    ('sys_desc', '1.3.6.1.2.1.1.1.0', None),
)

for ipaddr in ipaddrs:
    def_conn = (ipaddr, COMM_STRING, SNMP_PORT)
    for oid_x in snmp_oids:
        snmp_data = snmp_helper.snmp_get_oid(def_conn, oid=oid_x[1])
        snmp_data = snmp_helper.snmp_extract(snmp_data)
        print snmp_data
    print "\n"
