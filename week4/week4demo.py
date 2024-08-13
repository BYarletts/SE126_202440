# W4D2 SE111 Review Demo - split into prts in Canvas

# Braedin Yarletts
# Lab #4 
# August 12th

# VARIABLE DICTIONARY
#---------------------------------------------------------------------------------------------------------

import csv


dragon_ages = []
dragon_names = []
dragon_alias = []
allegiances = []
house_mottos = {
    "House Stark": "Winter is Coming",
    "Night's Watch": "The Watcher on the Wall",
    "House Tully": "Family, Duty, Honor",
    "House Lannister": "Hear Me Roar!",
    "House Baratheon": "Ours is the Fury",
    "House Targaryen": "Fire and Blood"
}

#CSV file and populate lists
with open('lab4a.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        name, allegiance, age, alias, house = row
        dragon_names.append(name)
        dragon_alias.append(alias)
        allegiances.append(house)
        #Set age to an int since its the only number column
        dragon_ages.append(int(age))

#Create a list of dragon info including House Mottoes
dragon_info = []
for i in range(len(dragon_names)):
    motto = house_mottos.get(allegiances[i], "Unknown")
    dragon_info.append([
        dragon_names[i],
        dragon_alias[i],
        dragon_ages[i],
        allegiances[i],
        motto
    ])

#Each record fully with the House Mottos
print(f"{'NAME':12}  {'ALIAS':15} {'AGE':5} {'ALLEGIANCE':15} {'MOTTO'}")
print("---------------------------------------------------------------")
for i in range(len(dragon_info)):
    name, alias, age, allegiance, motto = dragon_info[i]
    print(f"{name:12}  {alias:15} {age:5} {allegiance:15} {motto}")
print("---------------------------------------------------------------")

#Calculating the average age
total_age = sum(record[2] for record in dragon_info)
average_age = total_age / len(dragon_info)

#Printing total number of people and average age
print(f"Total number of people: {len(dragon_info)}")
print(f"Average age: {average_age:.0f}")

# Tally for each allegiance
allegiance_tally = {}
for record in dragon_info:
    allegiance = record[3]
    if allegiance in allegiance_tally:
        allegiance_tally[allegiance] += 1
    else:
        allegiance_tally[allegiance] = 1

#Print tallies of the allegiance
print("Allegiance tallies:")
for allegiance, count in allegiance_tally.items():
    print(f"{allegiance}: {count}")
