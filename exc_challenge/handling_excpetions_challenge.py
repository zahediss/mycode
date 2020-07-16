#!/usr/bin/env python3
# Handling Errors Challenge

# Create a function that takes a required argument of a list, and an optional parameter of an integer

def list_func(mylist, num = 10):
    for x in mylist:
        print(x) # iterate through list
        try:
            math = x/num
            print(math)
        except TypeError as err:
            print(err)
            print("This type is not correct. Your item {x} is not divisible by 10")

#list of items
mixed = ["cats", 24, "lizards", 7, "fish", 300]

# Execute the function
list_func(mixed, 10)       

# Use a try/except block to "try" to divide each item by your optional integer parameter

# If there is a ValueError, handle it by printing out the value of the error (err) and also printing "Your item ____ is not divisible by ____ " (fill in with item of list, and optional integr)
