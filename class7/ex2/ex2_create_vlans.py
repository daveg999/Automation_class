#!/usr/bin/env python

import pyeapi
import argparse
from pprint import pprint

def clean_results(output):
    ''' clean the returned result from the pyeapi command  '''

    return output[0]['result'] 

def does_vlan_exist(connected_device, vlan_id):
    ''' check to see if vlan already exists on device '''

    vlan_id = str(vlan_id)
    vlan_check = 'show vlan id %s' % vlan_id

    try:
        vlan_check1 = connected_device.enable(vlan_check)
        vlan_check2 = clean_results(vlan_check1)['vlans']
        return vlan_check2[vlan_id]['name']
    except (pyeapi.eapilib.CommandError, KeyError):
        pass
    return False


def main():
    ''' connect to device '''

    connected_device = pyeapi.connect_to('pynet-sw4')

    ''' argparse config - get input data for vlan build/remove '''

    parser = argparse.ArgumentParser()
    parser.add_argument('--name', 
        help = 'enter name of vlan to add or delete', 
        dest='vlan_name'
    )
    parser.add_argument('vlan_id', 
        help = 'enter vlan number between 100 - 999 to add or delete', 
        type=int
    )
    parser.add_argument('--remove', 
        help = 'enter vlan number to delete', 
        action="store_true", 
        dest='vlan_remove', 
        default=False
    )

    ''' create cleaner variables '''

    vlan_input = parser.parse_args()
    vlan_id = vlan_input.vlan_id
    vlan_name = vlan_input.vlan_name
    vlan_remove = vlan_input.vlan_remove

    ''' check: does vlan already exist '''

    vlan_exist = does_vlan_exist(connected_device, vlan_id)

    ''' create or clobber vlan '''

    if vlan_exist:
        if vlan_remove:
            print "vlan %s exists and will be deleted" % vlan_id
            connected_device.api('vlans').delete(vlan_id)
        else:
            print "vlan %s exists - comparing vlan names" % vlan_id
            if vlan_name == vlan_exist:
                print "vlan %s and vlan name %s exist - no change needed - end task" % (vlan_id, vlan_name)
            else:
                print "vlan name %s different from existing config - changing" % vlan_name
                connected_device.api('vlans').set_name((vlan_id), name=(vlan_name))
    else:
        if vlan_remove:
            print "vlan %s does not exist - no change needed" % vlan_id
        else:
            print "vlan %s does not exist - creating" % vlan_id
            connected_device.api('vlans').create(vlan_id)
            connected_device.api('vlans').set_name((vlan_id), name=(vlan_name))


if __name__ == '__main__':
    main()


