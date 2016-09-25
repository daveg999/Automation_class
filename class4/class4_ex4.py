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
    ssh_conn.timeout = 10
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')
    ssh_conn.sendline('term len 0')
    ssh_conn.expect('#')
    print 'current value for logging buffered'
    ssh_conn.sendline('sho run | i buffered')
    print ssh_conn.after

    ssh_conn.expect('#')
    ssh_conn.sendline('conf t')
    ssh_conn.expect('#')
    ssh_conn.sendline('logging buffered 99999')
    ssh_conn.expect('#')
    ssh_conn.sendline('end')
    ssh_conn.expect('#')
    print 'new value for logging buffered'
    ssh_conn.sendline('sho run | i buffered')
    ssh_conn.expect('#')
    print ssh_conn.after


if __name__ == "__main__":
    main()
