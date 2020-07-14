#list 5 cars
car_list = ["bmw","audi","toyota","ford","lexus"]

#list 5 names
name_list = ["Sanam","Matt","Sam","Elise","Betsy"]

#print out 3rd item of each list
print(car_list[2])
print(name_list[2])

#print out slice containing cars 2-4 (inclusive)
print(car_list[2:])

#print out slice containing names 0-2 (non-inclusive)
print(name_list[0:2])

#new list named combined
combined_list = []
print(combined_list)

#use append to add cars into the list
combined_list.append(car_list)
print(combined_list)

#use extend to add names into the list
combined_list.extend(name_list)
print(combined_list)

#pull out 2 cars and 2 names from combined list
print(combined_list[3:5])
print(combined_list[0][:2])
