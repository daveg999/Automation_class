#!/usr/bin/env python

import netmiko
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
import multiprocessing
from datetime import datetime
from getpass import getpass
password = getpass()

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': password,
}

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
}

juniper_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': password,
    'secret': '',
}


dev_list = [
    pynet1,
    pynet2,
    juniper_srx,
]

for dev in dev_list:
    connect_x = ConnectHandler(**dev)

    print "In device name:"
    dev_name = connect_x.find_prompt()
    print dev_name

    output = connect_x.send_command('sho arp')
    print output


# DEVICE_CREDS contains the devices to connect to
from DEVICE_CREDS import all_devices


def print_output(results):

    print "\nSuccessful devices:"
    for a_dict in results:
        for identifier,v in a_dict.iteritems():
            (success, out_string) = v
            if success:
                print '\n\n'
                print '#' * 80
                print 'Device = {0}\n'.format(identifier)
                print out_string
                print '#' * 80

    print "\n\nFailed devices:\n"
    for a_dict in results:
        for identifier,v in a_dict.iteritems():
            (success, out_string) = v
            if not success:
                print 'Device failed = {0}'.format(identifier)

    print "\nEnd time: " + str(datetime.now())
    print


def worker_show_version(a_device, mp_queue):
    '''
    Return a dictionary where the key is the device identifier
    Value is (success|fail(boolean), return_string)
    '''

    try:
        a_device['port']
    except KeyError:
        a_device['port'] = 22

    identifier = '{ip}:{port}'.format(**a_device)
    return_data = {}

    show_ver_command = 'show version'
    SSHClass = netmiko.ssh_dispatcher(a_device['device_type'])

    try:
        net_connect = SSHClass(**a_device)
        show_version = net_connect.send_command(show_ver_command)
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        return_data[identifier] = (False, e)

        # Add data to the queue (for parent process)
        mp_queue.put(return_data)
        return None

    return_data[identifier] = (True, show_version)
    mp_queue.put(return_data)



def main():

    mp_queue = multiprocessing.Queue()
    processes = []

    print "\nStart time: " + str(datetime.now())

    for a_device in all_devices:

        p = multiprocessing.Process(target=worker_show_version, args=(a_device, mp_queue))
        processes.append(p)
        # start the work process
        p.start()

    # wait until the child processes have completed
    for p in processes:
        p.join()

    # retrieve all the data from the queue
    results = []
    for p in processes:
        results.append(mp_queue.get())

    print_output(results)


if __name__ == '__main__':

    main()
