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
    ssh_conn.sendline('term len 0')
    ssh_conn.expect('#')

    ssh_conn.sendline('sho ip int br')
    ssh_conn.expect('#')

    print ssh_conn.after


if __name__ == "__main__":
    main()
