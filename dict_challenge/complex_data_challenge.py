#!/usr/bin/env python3

# Create a dictionary with 2 keys, pets and movies

# Have the value of pets be a list of dictionaries with keys of "type" and "name"
# Have the value of movies be a list of dictionaries with keys of "rating" and "name"
# pets and movies should have 3 items each

dict = {"pets":[{"type":"Aussie","name":"Winston"},{"type":"goldfish","name":"Bernie"},{"type":"cat","name":"Ed"}],"movies":[{"name":"Fight Club","rating":"7"},{"name":"Extraction","rating":"5"},{"name": "Casino","rating":"8.5"}]}

print(dict)

# print out 2 of pets with their type and name
# print out 1 movie with its rating and name

print(dict["pets"][0])
print(dict["pets"][1])

print(dict["movies"][0])

