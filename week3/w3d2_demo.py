#W2D2 - Data from a Text file to 1D parllel lists 


import csv
#count the number of records in the file
records = 0
#prep some *empty* lists
name = []
age = []
animal = []
color = []
number = []
with open("week2_finished/classList.txt") as csvfile:
    file = csv.reader(csvfile)


for rec in file:
    records += 1
#store data into the lists
name.append(rec[0])
age.append(int(rec[1]))
animal.append(rec[2])
color.append(rec[3])
number.append(rec[4])
#disconnected from the file
#list processing -- FOR LOOP!
