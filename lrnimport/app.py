#!/usr/bin/env python3
from core import silly_strings

# From app.py, get three or more user inputs for silly words

input1 = input("What is your first silly word?\n")
input2 = input("What is your second silly word?\n")
input3 = input("What is your third silly word?\n")

words = [input1, input2, input3]

print(silly_strings(words))


# Put them into a list
# Import you silly_strings function from your core.py script
# Pass the list into the silly_strings function and print the result
