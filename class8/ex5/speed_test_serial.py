#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
from net_system.models import NetworkDevice, Credentials
import django

''' ********************************************** '''
''' average time for multiple tests is 42 sec '''
''' ********************************************** '''

def main():
    django.setup()

    start_time = datetime.now()

    devices = NetworkDevice.objects.all()
    for dev in devices:

        print '*' * 60
        print dev
        print

        device_type = dev.device_type
        port = dev.port
        secret = ''
        ip = dev.ip_address
        creds = dev.credentials
        username = creds.username
        password = creds.password

        print device_type, port, ip, username, password
        print

        remote_conn = ConnectHandler(device_type=device_type, ip = ip, 
                                     username=username, password=password, 
                                     port=port)


        print remote_conn.send_command_expect("show version")
        print '*' * 60
        print


    print '*' * 60
    print
    elapsed_time = datetime.now() - start_time
    print "Elapsed_time: {} ".format(elapsed_time)
    print
    print '*' * 60


if __name__ == "__main__":
    main()

