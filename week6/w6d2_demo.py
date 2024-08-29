#w6D2 - Bubble Sorting & Binary Search Review



#---IMPORTS-----------------------------------------------------------------
import csv

#---FUNCTIONS---------------------------------------------------------------

#---MAIN CODE---------------------------------------------------------------
class_type = [] #rec[0]
name = []       #rec[1]
meaning = []    #rec[2]
culture = []    #rec[3] 

with open("week6/party.csv" , encoding="utf-8" ) as csvfile:
    file = csv.reader(csvfile)


    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])

print (f"{'TYPE':8} {'NAME':10} {'CULTURE':10} {'MEANING'}")
print("-----------------------------------------------------------------")
for i in range(0, len(class_type)):
    print(f"{class_type[i]:8}   {name[i]:10}   {culture[i]:10}   {meaning[i]}")
print("-----------------------------------------------------------------\n")

#BINARY SEARCH: requires the list to be populated with unique values + be ORDERED

#BUUBBLE SORT ALGORITHM

for i in range(0, len(name) - 1):


    for index in range(0, len(name) - 1):


        if(name[index] > name[index + 1]):


            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp


            temp = class_type[index]
            class_type[index] = class_type[index + 1]
            class_type[index + 1] = temp

            temp = culture[index]
            culture[index] = culture[index + 1]
            culture[index + 1] = temp

            temp = meaning[index]
            meaning[index] = meaning[index + 1]
            meaning[index + 1] = temp

print("\t\tORDERED BY *NAME*")
print (f"{'TYPE':8} {'NAME':10} {'CULTURE':10} {'MEANING'}")
print("-----------------------------------------------------------------")
for i in range(0, len(class_type)):
    print(f"{class_type[i]:8}   {name[i]:10}   {culture[i]:10}   {meaning[i]}")
print("-----------------------------------------------------------------\n")

search = input("\nEnter the NAME you are looking for: ")
#now that it is ordred by name, we can now perform BINARY SEARCH

min = 0
max = len(name) - 1
mid= int((min + max)/2)



while min < max and search != name[mid]:
    if search < name[mid]:
        max = mid - 1
    else:
        min = mid + 1

    mid = int((min + max)/2)

if search == name[mid]:
    print(f"We FOUND {search} !")
    print(f"{class_type[mid]:8} {name[mid]:10} {culture[mid]:10} {meaning[mid]}")
else:
    print(f"We DID NOT FIND {search}")
            