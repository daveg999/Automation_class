#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass
from net_system.models import NetworkDevice, Credentials
import django
from multiprocessing import Process, current_process, Queue

''' ********************************************** '''
''' average time for multiple tests is 8.5 sec '''
''' ********************************************** '''

def sho_ver_queue(dev, q):
    output_dict = {}
    creds = dev.credentials
    remote_conn = ConnectHandler(device_type=dev.device_type,
                                 ip = dev.ip_address,
                                 username = creds.username,
                                 password = creds.password,
                                 port = dev.port,
                                 secret = '',
                                 verbose = False)

    output = ('*' * 60) + "\n"
    output += remote_conn.send_command_expect("show version")
    output += ('*' * 60) + "\n"
    output_dict[dev.device_name] = output
    q.put(output_dict)


def main():
    django.setup()

    start_time = datetime.now()
    q = Queue(maxsize=20)
    devices = NetworkDevice.objects.all()

    procs = []
    for dev in devices:
        a_proc = Process(target=sho_ver_queue, args=(dev, q ))
        a_proc.start()
        procs.append(a_proc)

    ''' ensure all procs have finished '''
    for x_proc in procs:
        x_proc.join()

    while not q.empty():
        dict = q.get()
        for key,val in dict.iteritems():
            print key
            print val

    print "Elapsed time: " + str(datetime.now() - start_time)


if __name__ == "__main__":
    main()

