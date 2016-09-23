#!/usr/bin/env python

# import modules

import paramiko
from getpass import getpass
import time

# set static variables

device = '184.105.247.71'
username = 'pyclass'
password = getpass()


# initialize variables

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# connect to device

remote_conn_pre.connect(device, username=username, password=password, look_for_keys=False, allow_agent=False)
remote_conn = remote_conn_pre.invoke_shell()

'''
turn off paging
initial \n to "wake up" device - had issues with dropping 1st letter of command
'''

remote_conn.send("\n")
remote_conn.send("term len 0\n")
time.sleep(1)

# send command to device and print results

remote_conn.send("\n")
remote_conn.send("sho ver\n")
time.sleep(1)
output = remote_conn.recv(50000)
print output

# close connection

remote_conn_pre.close()
