#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
from net_system.models import NetworkDevice, Credentials
import django
from multiprocessing import Process, current_process

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

    procs = []
    for dev in devices:
        a_proc = Process(target=sho_ver, args=(dev,))
        a_proc.start()
        procs.append(a_proc)

    for a_proc in procs:
        print a_proc
        a_proc.join()


    print "Elapsed time: " +str(datetime.now() - start_time)


if __name__ == "__main__":
    main()

