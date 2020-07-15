#!/usr/bin/env python3

#Advanced Challenge

# Create a list of dictionaries with at least 5 chores in it, using the following format:
# todo = [{"chore": "dishes", "time": 15}, {"chore": "laundry", "time": 20}]

todo = [{"chore": "vacuum", "time": 15}, {"chore": "laundry", "time": 45}, {"chore": "dishes", "time": 20}, {"chore": "dusting", "time": 15}, {"chore": "watering", "time": "10"}]

# Use real values to help you think about your tasks this week.

# Using a for loop, enumerate the list, capturing the index and the value
# https://docs.python.org/3/library/functions.html#enumerate

for todo_num, chore in enumerate(todo, 1):

# Use if/elif/else statement(s) to determine the order of tasks based on their index
# index 0 = first
# index 1 = second
# index 2 = third
# index 3 = fourth
# index 4 = fifth

    order = "first"

    if todo_num == 2:
        order = "second"

    elif todo_num == 3:
        order = "third"

    elif todo_num == 4:
        order = "fourth"

    elif todo_num == 5:
        order = "fifth"

# Use this sentence as a guide:
# "The {order of task} thing I have to do is {chore}. It should only take {time} minutes."

print(f"The {order} thing I have to do is {chore['chore']}. It should only take me {chore['time']} minutes.")

# And have your script output 5 such lines:
# "The first thing I have to do is dishes. It should only take 15 minutes."
