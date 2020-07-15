#!/usr/bin/env python3
# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create list of lines from dnsserver.txt file
dnslist = dnsfile.readlines()

# loop over lines and print
for svr in dnslist:
    #end print with new line
    print(svr, end="")

# close your file
dnsfile.close()

