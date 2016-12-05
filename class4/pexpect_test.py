#!/usr/bin/env python

import pexpect
import sys
import re
from getpass import getpass

def main():
    ip = '184.105.247.71'
    username = 'pyclass'
    password = getpass()

    ssh_conn = pexpect.spawn('ssh -l {} {}'.format(username, ip))
    ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')

    #ssh_conn.sendline('sho ip int br')
    #ssh_conn.expect('#')

    ssh_conn.sendline('term len 0')
    ssh_conn.expect('#')

    #ssh_conn.sendline('sho ver')
    #ssh_conn.expect('rtr2#')

    pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
    ssh_conn.sendline('sho ver')
    ssh_conn.expect(pattern)
    print ssh_conn.after

    #try:
        #ssh_conn.sendline('sho ver')
        #ssh_conn.expect('blah')
    #except pexpect.TIMEOUT:
        #print "Ran into timeout issue"

    #print ssh_conn.before
    #print ssh_conn.after


   #router_name = ssh_conn.before
   #router_name = router_name.strip()
   #prompt = router_name + ssh_conn.after
   #prompt = prompt.strip()



if __name__ == "__main__":
    main()
