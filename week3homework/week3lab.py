#W1D2 SE116 Review Demo - split into prts in Canvas

#Braedin Yarletts
#Lab #1 
#July 22th 


#VARIBLE DICTIONARY
#---------------------------------------------------------------------------------------------------------
#not_eligible: A counter that tracks the number of individuals who are not eligible to vote (i.e., individuals under the age of 18).

#eligible_not_registered: A counter that tracks the number of eligible individuals (18 years or older) who are registered to vote but did not register.

##eligible_not_voted: A counter that tracks the number of eligible individuals who are registered to vote but did not vote.

#did_vote: A counter that tracks the number of eligible individuals who are registered to vote and have actually voted.

#records_processed: A counter that tracks the total number of records processed from the CSV file.

#id_numbers: A list used to store the ID numbers of individuals from the CSV file.

#ages: A list used to store the ages of individuals from the CSV file.

#registrations: A list used to store the registration status ('Y' for Yes, 'N' for No) of individuals from the CSV file.

#votes: A list used to store the voting status ('Y' for Yes, 'N' for No) of individuals from the CSV file.

#---------FUNCTIONS---------------------------------------------------------------------------------------

import csv

# Initialize counters
not_eligible = 0
eligible_not_registered = 0
eligible_not_voted = 0
did_vote = 0
records_processed = 0

# Lists to store voter data
id_numbers = []
ages = []
registrations = []
votes = []

# Open the CSV file
with open("voter_202040.csv", mode='r') as csvfile:
    file = csv.reader(csvfile)
    
    # Iterate through each record in the file
    for rec in file:
        if len(rec) < 4:  # Check if the record has less than 4 fields
            print(f"Warning: Skipping record with insufficient fields: {rec}")
            continue
        
        # Append data to lists
        id_numbers.append(rec[0])
        ages.append(int(rec[1]))
        registrations.append(rec[2])
        votes.append(rec[3])
        
        records_processed += 1

# Process each voter's data to calculate totals
for i in range(records_processed):
    age = ages[i]
    registered = registrations[i]
    voted = votes[i]
    
    if age < 18:  # checks if the age is eligible or not
        not_eligible += 1
    else:
        if registered == 'Y':
            if voted == 'Y':  #If they registered and voted
                did_vote += 1
            else:
                eligible_not_voted += 1
        else:
            eligible_not_registered += 1

# Final print statements for the reports
print("\nVoting List for the participants:")
print(f"{'Category':<35} {'Count':<6}")
print(f"{'Not Eligible':<35} {not_eligible:<6}")
print(f"{'Eligible but Not Registered':<35} {eligible_not_registered:<6}")
print(f"{'Eligible but Did Not Vote':<35} {eligible_not_voted:<6}")
print(f"{'Did Vote':<35} {did_vote:<6}")
print(f"{'Records Processed':<35} {records_processed:<6}")

print("Thank you for voting!.")
