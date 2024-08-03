#W3D2 SE126

#Braedin Yarletts
#Lab #3 
#AUGUST 2nd


#--------VARIBLE DICTIONARY---------------------------------------------------------------------------------

#csv: A Python module for reading and writing CSV (Comma-Separated Values) files.
#records: An integer variable used to count the total number of valid records processed from the CSV file.
#brand: A list that stores the brand information of each item read from the CSV file.
#model: A list that stores the model information of each item read from the CSV file.
#processor: A list that stores the processor information of each item read from the CSV file.
#size: A list that stores the size of each item read from the CSV file.
#quantity: A list that stores the quantity of each item read from the CSV file.
#type: A list that stores the type of each item (e.g., Desktop or Laptop) read from the CSV file.
#os: A list that stores the operating system of each item read from the CSV file.
#age: A list that stores the age of each item read from the CSV file.
#desktop_cost: A constant representing the cost to replace one desktop.
#laptop_cost: A constant representing the cost to replace one laptop.
#numdesktopstoreplace: An integer variable used to count the number of desktops that need to be replaced.
#numlaptopstoreplace: An integer variable used to count the number of laptops that need to be replaced.
#rec: A list that represents a single record (line) from the CSV file.
#isdigit(): A string method used to check if all characters in the string are digits.
#get_integer_input(prompt): A function that prompts the user for integer input and ensures the input is a valid numeric value.
#maxdesktops: An integer variable that stores the maximum number of desktops the user wants to replace, as input by the user.
#maxlaptops: An integer variable that stores the maximum number of laptops the user wants to replace, as input by the user.
#totalcostdesktops: An integer variable that calculates the total cost for replacing the specified number of desktops.
#totalcostlaptops: An integer variable that calculates the total cost for replacing the specified number of laptops.
#another: A string variable used to determine if the user wants to enter more values. It is used to control whether the input loop continues.
#break: A statement used to exit a loop prematurely.
#continue: A statement used to skip the current iteration of a loop and proceed with the next iteration.

#---------FUNCTIONS-------------------------------------------------

import csv

# Initialize counters and empty lists
records = 0
brand = []
model = []
processor = []
size = []
quantity = []
type = []
os = []
age = []

desktop_cost = 2000
laptop_cost = 1500

numdesktopstoreplace = 0
numlaptopstoreplace = 0

#-------MAIN CODE--------------------------------------------------------

# Open the CSV file
with open("lab3a.csv") as csvfile:
    file = csv.reader(csvfile)
    
    # Iterate through each record in the file
    for rec in file:
        if len(rec) < 8:  # Check if the record has less than 8 fields
            print(f"Warning: Skipping record with insufficient fields: {rec}")
            continue
        
        records += 1
        brand.append(rec[0])
        model.append(rec[1])
        processor.append(rec[2])
        size.append(rec[3])
        quantity.append(rec[4])
        type.append(rec[5])
        os.append(rec[6])
        
        # Convert age to integer and handle any potential conversion errors
        if rec[7].isdigit():
            age.append(int(rec[7]))
        else:
            age.append(0)


# Calculate the total number of desktops and laptops that need replacement
for i in range(records):
    if isinstance(age[i], int) and age[i] <= 2016: 
        if type[i] == 'D':
            numdesktopstoreplace += 1
        elif type[i] == 'L':
            numlaptopstoreplace += 1

# Input loop for multiple user inputs
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print("Invalid input. Please enter a numeric value.")

while True:
    maxdesktops = get_integer_input(f"\nEnter the maximum number of desktops you want to replace (cost per desktop: ${desktop_cost}): ")
    maxlaptops = get_integer_input(f"Enter the maximum number of laptops you want to replace (cost per laptop: ${laptop_cost}): ")

    # Calculate the total cost for replacements
    totalcostdesktops = maxdesktops * desktop_cost
    totalcostlaptops = maxlaptops * laptop_cost

    # The end report
    print("\nEnd Report:")
    print(f"{'Type':<12} {'Count':<6} {'Cost per Item':<15} {'Total Cost':<12}")
    print(f"{'Desktops':<12} {maxdesktops:<6} ${desktop_cost:<14} ${totalcostdesktops:<12}")
    print(f"{'Laptops':<12} {maxlaptops:<6} ${laptop_cost:<14} ${totalcostlaptops:<12}")

    # Ask the user if they want to input more values
    another = input("\nDo you want to enter more values? (yes/no): ").lower()
    if another != 'yes':
        break

print("Thank you! Goodbye.") #End Message