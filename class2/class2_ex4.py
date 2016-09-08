#!/usr/bin/env python

import telnetlib
import time
import socket
import sys
import getpass
import snmp_helper


TELNET_PORT = 23
TELNET_TIMEOUT = 6
COMM_STRING = "galileo"
SNMP_PORT = 161
OID_DESC = '1.3.6.1.2.1.1.1.0'
OID_NAME = '1.3.6.1.2.1.1.5.0'

print "in main module"
ipaddrs = ['184.105.247.70', '184.105.247.71']

for ipaddr in  ipaddrs:
    def_conn = (ipaddr, COMM_STRING, SNMP_PORT)
    snmp_name = snmp_helper.snmp_get_oid(def_conn, oid=OID_NAME)
    snmp_desc = snmp_helper.snmp_get_oid(def_conn, oid=OID_DESC)
    output_name = snmp_helper.snmp_extract(snmp_name)
    output_desc = snmp_helper.snmp_extract(snmp_desc)

    print "\n\n"
    print output_name
    print "\n\n"
    print output_desc
    print "\n\n"
