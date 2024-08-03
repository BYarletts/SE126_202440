
import csv

# Initialize counters and empty lists
records = 0
brand = []
model = []
processor = []
size = []
quantity = []
type_ = []
os = []
age = []

# Define costs for replacement
desktop_cost = 2000
laptop_cost = 1500

# Initialize counters for replacements
num_desktops_to_replace = 0
cost_desktops = 0
num_laptops_to_replace = 0
cost_laptops = 0

# Open the CSV file
with open("lab3a.csv") as csvfile:
    file = csv.reader(csvfile)
    
    # Iterate through each record in the file
    for rec in file:
        records += 1
        brand.append(rec[0])
        model.append(rec[1])
        processor.append(rec[2])
        size.append(rec[3])
        quantity.append(rec[4])
        type_.append(rec[5])
        os.append(rec[6])
        age.append(int(rec[7]))  # Convert age to integer

# Print the number of records
print(f"Total number of records: {records}")

# Print all records in tabular format
print("\nAll records:")
print(f"{'Brand':<6} {'Model':<6} {'Processor':<6} {'Size':<6} {'Quantity':<8} {'Type':<4} {'OS':<4} {'Age':<4}")
print("-" * 50)
for i in range(records):
    print(f"{brand[i]:<6} {model[i]:<6} {processor[i]:<6} {size[i]:<6} {quantity[i]:<8} {type_[i]:<4} {os[i]:<4} {age[i]:<4}")

# Process the data to calculate replacement costs
for i in range(records):
    if age[i] <= 2016:
        if type_[i] == 'D':
            num_desktops_to_replace += 1
            cost_desktops += desktop_cost
        elif type_[i] == 'L':
            num_laptops_to_replace += 1
            cost_laptops += laptop_cost

# Print the end report
print("\nEnd Report:")
print(f"{'Type':<10} {'Count':<6} {'Cost per Item':<15} {'Total Cost':<10}")
print("-" * 41)
print(f"{'Desktops':<10} {num_desktops_to_replace:<6} ${desktop_cost:<14} ${cost_desktops:<10}")
print(f"{'Laptops':<10} {num_laptops_to_replace:<6} ${laptop_cost:<14} ${cost_laptops:<10}")
