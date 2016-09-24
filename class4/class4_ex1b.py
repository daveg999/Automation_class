#!/usr/bin/env python

import paramiko
import time
from getpass import getpass


def prevent_paging(remote_conn):

    ''' stop pagination '''
    remote_conn.send("\n")
    remote_conn.send("term len 0\n")
    time.sleep(1)

    ''' clear output buffer '''
    output = remote_conn.recv(1000)
    return output


def close_connection(remote_conn):

    ''' close SSH connection '''
    remote_conn.close()



if __name__ == '__main__':


    ''' set static variables '''

    device =   '184.105.247.71'
    username = 'pyclass'
    password = getpass()


    ''' initialize variables '''

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    ''' connect to device '''

    remote_conn_pre.connect(device, username=username, password=password, look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()


    ''' disable paging using function '''

    prevent_paging(remote_conn)


    ''' send command to device and print results '''

    remote_conn.send("\n")
    remote_conn.send("sho ver\n")
    time.sleep(1)
    output = remote_conn.recv(50000)
    print output

    ''' close connection using function '''

    close_connection(remote_conn)
