#!/usr/bin/env python

import time
import telnetlib

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    target = "184.105.247.70"    
    user   = "pyclass"
    pw     = "88newclass"

    remote_conn = telnetlib.Telnet(target, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("name: ", TELNET_TIMEOUT)
#    print
#    print output
    output = remote_conn.write(user + "\n")

    output = remote_conn.read_until("word: ", TELNET_TIMEOUT)
#    print
#    print output
    remote_conn.write(pw + "\n")
#    print
#    print pw
    time.sleep(2)
    output = remote_conn.read_very_eager()
#    print
#    print output

# execute a command on the device you logged into

# set page length to 0
    remote_conn.write("term len 0" + "\n")

# write command to target
    remote_conn.write("sho ip int br" + "\n")
    time.sleep(2)
    output = remote_conn.read_very_eager()
#    print
    print output

    remote_conn.close()

if __name__ == "__main__":
    main()



