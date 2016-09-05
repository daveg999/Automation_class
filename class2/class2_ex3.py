#!/usr/bin/env python

import telnetlib
import time
import socket
import sys
import getpass


TELNET_PORT = 23
TELNET_TIMEOUT = 6

class myTelnet(object):

    def __init__(self, ipaddr, uname, pw):
        self.ipaddr = ipaddr
        self.uname = uname
        self.pw = pw

        try:
            self.remote_conn = telnetlib.Telnet(self.ipaddr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed out")

    def send_command(self, cmd='\n'):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        print "in send_command module"
        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(2)
        return self.remote_conn.read_very_eager()

    def login(self):
        '''
        Login to network device
        '''
        print "in login module"
        output = self.remote_conn.read_until("rname:", TELNET_TIMEOUT)
        self.remote_conn.write(self.uname + '\n')
        output += self.remote_conn.read_until("sword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.pw + '\n')
        time.sleep(2)
        return output

    def disable_paging(self, no_paging='term len 0'):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        print "in disable_paging module"
        return self.send_command(no_paging)

    def telnet_connect(self, ipaddr):
        '''
        Establish telnet connection
        '''
        print "in telnet_connect module"
        try:
            self.remote_conn = telnetlib.Telnet(self.ipaddr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")

    def close_conn(self):
        print "in the closing connection module"
        self.remote_conn.close()


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logs in, and executes the
    'show ip int brief' command.
    '''
    print "in main module"
    ipaddr = raw_input("IP Address: ")
    ipaddr = ipaddr.strip()
    uname =  raw_input("Enter username: ")
    pw = getpass.getpass()

    def_conn = myTelnet(ipaddr, uname, pw)
    def_conn.login()
    def_conn.send_command()
    def_conn.disable_paging()

    output = def_conn.send_command('show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    def_conn.close_conn()

if __name__ == "__main__":
    main()
