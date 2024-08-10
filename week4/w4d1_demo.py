#W4D1 SE126 
#Braedin Yarletts
#Lab #4 
#August 9th


#VARIBLE DICTIONARY
#---------------------------------------------------------------------------------------------------------
#firstNames: A list to store the first names of students.
#lastNames: A list to store the last names of students.
#test1, test2, test3: Lists to store test scores for three different tests.
#numAvg: A list to store the average test scores for each student.
#letAvg: A list to store the letter grades corresponding to the average test scores.
#rec: A variable representing a single row (record) in the CSV file.
#first_name, last_name: Variables to store the first and last names extracted from the record.
#avg: Variable to store the average of the three test scores.
#letter: Variable to store the letter grade based on the average score.
#numAvg: Appends the average score to the numAvg list.
#gradeTotal = sum(numAvg): Calculates the total of all average scores.
#classAvg = gradeTotal / len(numAvg): Calculates the class average by dividing the total of average scores by the number of students.
#---------FUNCTIONS---------------------------------------------------------------------------------------
import csv

# Create empty lists - one for EACH potential field
firstNames = []
lastNames = []
test1 = []
test2 = []
test3 = []

# We will also create data and append to these below
numAvg = []
letAvg = []

# Connected to file----------------------------------
with open("listPractice1.csv", newline='') as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        # Ensure the record has exactly 5 fields
        if len(rec) == 5:
            first_name = rec[0]
            last_name = rec[1]
            
            # Directly append values assuming they are integers
            test1.append(int(rec[2]))
            test2.append(int(rec[3]))
            test3.append(int(rec[4]))
            firstNames.append(first_name)
            lastNames.append(last_name)
        else:
            print(f"--------------------------------------------")


# Process lists to find letter grade  for each student 
for i in range(len(firstNames)):
    avg = (test1[i] + test2[i] + test3[i]) / 3

    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    else:
        letter = "F"

    
    numAvg.append(avg)
    letAvg.append(letter)   

#Reprocess to print
print(f"{'FIRST':10}\t{'LAST':10}\t{'T#1':3}\t{'T#2':3}\t{'T#3':3}\t{'AVG.':5}\t{'LETTER':3}")
print("-------------------------------------------------------------------------------")

#Process list
for i in range(len(firstNames)):
    print(f"{firstNames[i]:10}\t{lastNames[i]:10}\t{test1[i]:3}\t{test2[i]:3}\t{test3[i]:3}\t{numAvg[i]:5.1f}\t{letAvg[i]:3}")
print("-------------------------------------------------------------------------------")

#Process lists to find class average; display data at end
if numAvg:  # Check to avoid division by zero
    gradeTotal = sum(numAvg)
    classAvg = gradeTotal / len(numAvg)
else:
    classAvg = 0

print(f"\n\tThere are {len(numAvg)} students in the class\n\tThe Class Average is: {classAvg:.1f}\n\n")
