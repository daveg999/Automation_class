#!/usr/bin/env python

''' Class 8, exercise 1b '''

from net_system.models import NetworkDevice, Credentials

def main():
    ''' Link credentials to devices in the DB '''
    devices = NetworkDevice.objects.all()
    creds = Credentials.objects.all()

    std_creds = creds[0]
    arista_creds = creds[1]

    for dev in devices:
        if 'arista' in dev.device_type:
            dev.credentials = arista_creds
        else:
            dev.credentials = std_creds
        dev.save()

    for dev in devices:
        print dev, dev.credentials


if __name__ == "__main__":
    main()

