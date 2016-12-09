#!/usr/bin/env python

''' Class 8, exercise 4 '''

from net_system.models import NetworkDevice, Credentials
import django

def main():

    ''' create new NetworkDevice objects in the database '''

    django.setup()
    devices = NetworkDevice.objects.all()

    try:
        for dev in devices:
            if '007' in dev.device_name:
                print dev
                dev.delete()

    except NetworkDevice.DoesNotExist:
        pass


if __name__ == "__main__":
    main()

