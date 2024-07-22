#W2D1 mini demo - intro to text file hndling 


import csv 

total_records = 0
sum_age = 0

with open("week2_practice/se126_base_info.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:

        print(f"{record[0]:10}, {record[2]:4}")
        sum_age += int(record[2])
        total_records += 1

print("\n\nFile processing complete")


avg_age = sum_age / total_records
print(f"\n\nAverage Age in File: {avg_age:.2f}")
