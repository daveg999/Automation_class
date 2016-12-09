#!/usr/bin/env python

''' Class 8, exercise 3 '''

from net_system.models import NetworkDevice, Credentials
import django

def main():

    ''' create new NetworkDevice objects in the database '''

    django.setup()
    ipaddr = raw_input("Enter new IP address: ")

    '''
    temp_sw007 = NetworkDevice(
        device_name = 'temp_sw007',
        device_type = 'arista_eos',
        ip_address = ipaddr,
        port=22,
    )
    temp_sw007.save()
    '''

    temp_rt007 = NetworkDevice.objects.get_or_create(
        device_name = 'temp_rt007',
        device_type = 'cisco_ios',
        ip_address = ipaddr,
        port=22,
    )


    devices = NetworkDevice.objects.all()
    for dev in devices:
        print dev, dev.vendor, dev.model, dev.credentials


if __name__ == "__main__":
    main()

