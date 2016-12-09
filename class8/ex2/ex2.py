#!/usr/bin/env python

''' Class 8, exercise 2 '''

from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()

    ''' fill in vendors and models fields in the database '''

    devices = NetworkDevice.objects.all()

    for dev in devices:
        if 'arista' in dev.device_type:
            dev.vendor = 'arista'
            dev.model = '7280sr'
        elif 'juniper' in dev.device_type:
            dev.vendor = 'juniper'
            dev.model = 'SRX'
        else:
            dev.vendor = 'cisco'
            dev.model = '881'
        dev.save()

    for dev in devices:
        print dev, dev.vendor, dev.model, dev.credentials


if __name__ == "__main__":
    main()

