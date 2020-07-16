#!/usr/bin/env python3
import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:
        print('Could not collect adapter information') #print error message

#Try to build customized functions

def getip(adapter):
    print('\n**************Details of Interface - ' + adapter + ' *********************')
    try:
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print(netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]['addr'])
    except:
        print('Could not collect adapter information') #print error
        return netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]['addr']

def getmac(adapter):
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print(netifaces.ifaddresses(adapter)[netifaces.AF_LINK][0]['addr'])    
    except:
        print('Coult not collect adapter informtation') #print error
        return netifaces.ifaddresses(adapter)[netifaces.AF_LINK][0]['addr']


adapter_name = input("\nWhich interface would you like the IP and MAC for?\n Options are lo, ens3, docker0\n")
ip = getip(adapter_name)
mac = getmac(adapter_name)


