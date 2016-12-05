 #!/usr/bin/env python

import pyeapi
from pprint import pprint

def main():

    ''' connect to device '''
    pynet_sw4 = pyeapi.connect_to('pynet-sw4')

    ''' get octet counters from sho int command '''
    sho_int = pynet_sw4.enable('show interfaces')

    ''' tune results to get octets '''
    sho_int = sho_int[0]['result']
    sho_int = sho_int['interfaces']
    pprint(sho_int)

    ''' loop through interfaces to get counters '''
    int_octets = {}
    for int, int_data in sho_int.items():
        int_stats = int_data.get('interfaceCounters', {})
        int_octets[int] = (int_stats.get('inOctets'), int_stats.get('outOctets'))
    print
    print "----------------------------------------------------------"
    print "{:15} {:<15} {:<15}".format("Interface", "inOctets", "outOctets")
    for intf, octets in int_octets.items():

        ''' only print Ethernet interface octets '''
        if 'Ethernet' in intf:
            print "{:15} {:<15} {:<15}".format(intf, octets[0], octets[1])

    print
    print "----------------------------------------------------------"


if __name__ == '__main__':
    main()
