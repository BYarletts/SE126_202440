#W3 SE111

#Braedin Yarletts
#Lab #2 
#July 29th 


#VARIBLE DICTIONARY
#---------------------------------------------------------------------------------------------------------
# Device: This list stores the type of computer, categorizing each entry as either a Desktop or a Laptop.
# Brand: This list contains the brand of each computer, with possible values including Dell, HP, and Gateway.
# Cpu: This list holds the type of Intel processor for each computer, such as i5 or i7.
# Ram: This list records the amount of RAM in gigabytes (GB) for each computer.
# First_disk: This list tracks the size of the first hard drive in each computer.
# Second_disk: This list captures the size of the second hard drive, if applicable, in computers with more than one hard drive.
# num_disks: This list indicates the number of hard drives each computer has.
# os: This list holds the operating system installed on each computer.
# yr: This list stores the year when each computer was purchased.
#---------FUNCTIONS---------------------------------------------------------------------------------------


import csv

records = 0
device = []
brand = []
cpu = []
ram = []
first_disk = []
second_disk = []
num_disks = []
os = []
yr = []
#----------MAIN CODE---------------------------------------------------------------------------------------

with open("week3/lab3a.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        
        if rec[0] == "D":
            device.append("Desktop")
        elif rec[0] == "L":
            device.append("Laptop")
        else:
            device.append("-ERROR-")

        # Determine the brand
        if rec[1] == "GW":
            brand.append("Gateway")
        elif rec[1] == "HP":
            brand.append("HP")
        elif rec[1] == "DL":
            brand.append("Dell")
        else:
            brand.append("-ERROR-")

        # Process other fields
        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_disks.append(int(rec[5]))

        # Determine the second disk, OS, and year based on the number of disks
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

# Print records
print(f"{'Device':10}\t{'Brand':10}\t{'CPU':5}\t{'RAM':4}\t{'First Disk':7}\t{'Second Disk':7}\t{'# Disks':1}\t{'OS':4}\t{'Year':2}")
for index in range(len(device)):
    print(f"{device[index]:10}\t{brand[index]:10}\t{cpu[index]:5}\t{ram[index]:4}\t{first_disk[index]:7}\t{second_disk[index]:7}\t{num_disks[index]:1}\t{os[index]:4}\t{yr[index]:2}")

# Count desktops and laptops
desktops = sum(1 for i in device if i == "Desktop")
laptops = sum(1 for i in device if i == "Laptop")

print(f"\nThere are {desktops} desktops in this file")
print(f"There are {laptops} laptops in this file.")

