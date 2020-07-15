#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    #loop over the file
    for line in kfile:
        #if auth fail pattern appears in line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1

print("The number of failed login attemps is ", loginfail)
