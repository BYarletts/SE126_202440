import csv

records = 0



device = []
brand = []
cpu = []
ram = []
first_disk= []
second_disk = []
num_disks = []
os = []
yr = []


with open("week3/lab3a.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        #device.append(rec[0])
        if rec[0] == "D":
            device.append("Desktop")
        elif rec[0] == "L":
            device.append("Laptop")    
        else:
            device.append("-ERROR-")

        if rec[1] == "GW":
            brand.append("Gateway")
        elif rec[1] == "HP":
            brand.append("HP")
        elif rec[1] == "DL":
            brand.append("Dell")
        else:
            brand.append("-ERROR-")

        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_disks.append(int(rec[5]))

        if int(rec[5]) == 1:
            second_disk.append("---")
            os.append(rec[6])
            yr.append(rec[7])
        elif int(rec[5]) == 2:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])
        else:
            second_disk.append("-ERROR-")
            os.append(" @ ")
            yr.append(f"rec# {records}-")

for index in range(0, records):
    print(f"{device[index]:10}\t{brand[index]:10}\t...")


desktops = 0

for i in range(0, len(device)):
    if device[i] == "Desktop":
        desktops += 1

print(f"There are {desktops} desktops in this file")


laptops = 0
for value in device:
    if value == "Laptop":
        laptops += 1
print(f"There are {laptops} laptops in this file.")

