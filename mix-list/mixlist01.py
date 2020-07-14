#!/usr/bin/env python3
my_list = ["192.168.0.5", 5060, "UP"]

# 1 = IP address
# 2 = port number
# 3 = UP

#print first item in the list
print("The first item in the list (IP): " + my_list[0])

#print second item in the list
print("The second item in the list (port): " + str(my_list[1]))

#print third item in the list
print("The last item in the list (state): " + my_list[2])

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#print all new_list information in one function
print("When I ssh into IP addresses" + new_list[3], "or" + new_list[4], "I am unable to ping ports" + str(new_list[0]) + ", " + new_list[1] + ",or " + str(new_list[2]))
