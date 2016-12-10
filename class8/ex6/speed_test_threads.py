#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
from net_system.models import NetworkDevice, Credentials
import django
import threading

''' ********************************************** '''
''' average time for multiple tests is 8.5 sec '''
''' ********************************************** '''

def sho_ver(dev):
    creds = dev.credentials
    remote_conn = ConnectHandler(device_type=dev.device_type,
                                 ip = dev.ip_address,
                                 username = creds.username,
                                 password = creds.password,
                                 port = dev.port,
                                 secret = '')

    print remote_conn.send_command_expect("show version")


def main():
    django.setup()

    start_time = datetime.now()

    devices = NetworkDevice.objects.all()

    for dev in devices:
        a_thread = threading.Thread(target=sho_ver, args=(dev,))
        a_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print some_thread
            ''' block main thread from joining so timer can run correctly on all sub-threads '''
            some_thread.join()



    print "Elapsed time: " +str(datetime.now() - start_time)


if __name__ == "__main__":
    main()

