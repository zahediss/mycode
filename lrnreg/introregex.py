#!/usr/bin/env python3
import urllib.request
import re


#ask user what url they want to search and prompt for input
print("Where should we search?")
url = input()

#respond to search request and prompt input for phrase to search
print("Great So we'll try to open this url " + str(url) + " to search for the phrase: ")

while True:
    searchFor = input("What string would you like to input or type 'quit' to exit.\n")
    if searchFor.lower() == "quit":
        break
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")

    if re.search(searchFor, searchMe):
        print("Found a match!")
        #count number of matches
        findall = re.findall(searchFor, searchMe)
        print(len(findall))
    else:
        print("No match")

