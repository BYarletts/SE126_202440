#W4D2, 1D, 2D Lists, with Hand population 


import random

#create some hand-populated 1D lists

dragon_names = [
    "Drogon", 
    "Silverwing", 
    "Verimthor", 
    "Syrax", 
    "Meleys"
    ]

dragon_alias = [
    "Good Boi",
    "The Silver Lady",
    "The Bronze Fury",
    "The Goddess",
    "The Red Queen"
    ]


records = len(dragon_names) #records = 5


#simply display the parallel lists with each corresponding values on its own line

print(f"{"NAMES":12}        \t{"ALIAS"}")
print("-------------------------------------------------------")
for i in range(0, records):
    print(f"{dragon_names[i]:12} AKA \t{dragon_alias[i]}")
print("-------------------------------------------------------")

dragon_ages = []
for i in range(0, len(dragon_names)):
    dragon_ages.append(random.randint(0, 500))



for i in range(0, len(dragon_names)):
    print(f"{dragon_names[i]:12}     \t{dragon_ages[i]:5}y.o.")



#add all of the 1D lists to a new list, creating a 2D list!
'''
dragon_info = [
    dragon_names,
    dragon_alias,
    dragon_ages
]
'''
#for i in range()

dragon_info = []

for i in range(0, len(dragon_names)):
    dragon_info.append([dragon_names[i], dragon_alias[i], dragon_ages[i]])

for i in range(0, len(dragon_info)):
    print(f"REC#{i} LIST: {dragon_info[i]}")


    for x in range(0, len(dragon_info[i])):
        print(f"{dragon_info[i][x]:10}", end = " ")

    print()
print("------------------------------------------------------------")
















search_dragon = input("Who are you looking for?")

found = "n/a"



for i in range(0, len(dragon_names)):

    if search_dragon.lower() == dragon_names[i].lower():

        found = i

if found != "n/a":
    print(f"Your search for {search_dragon} was FOUND in record #{found}")

    print(f"NAME:{dragon_names[found]} \tALIAS:{dragon_alias[found]} \tAGE:{dragon_ages[found]}")
else:
    print(f"Sorry, your earch for {search_dragon} was *NOT FOUND.")
    