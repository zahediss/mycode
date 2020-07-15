#!/usr/bin/env python3

# Create 3 functions

# A math function that takes 2 required arguments, multiplies them together, and then divides by 100 and returns the result

def math_func(x,y):
    result1 = x * y
    result2 = int(result1)/100
    return result2

# print(math_func(11,9))

# A stringy function that takes a required argument string and returns every other letter from the string

def stringy_func(strz):
    new_strz = strz[::2]
    return new_strz

# print(stringy_func("abcdefg"))

# A main function that calls on both of these previous functions, which has 1 required argument of an integer, and has two default arguments (1 int and 1 string)

def main(int1, int2= 10, stringy= "abcdefg"):
    print(math_func(int1,int2))
    print(stringy_func(stringy))

# Call on the main function

main(99)

