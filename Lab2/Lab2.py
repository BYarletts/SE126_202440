#W2D2 SE116  - split into prts in Canvas

#Braedin Yarletts
#Lab #1 
#July 28th 


#VARIBLE DICTIONARY
#---------------------------------------------------------------------------------------------------------
#difference: A function defined in the code to calculate the difference between two numbers.
#people: A parameter of the difference function representing the number of people.
#max_cap: A parameter of the difference function representing the maximum capacity of a room.
#remain: A local variable in the difference function that stores the result of subtracting max_cap from people.
#process_rooms: A function defined to process room data from a CSV file and display information about room capacities.
#file_path: A parameter of the process_rooms function representing the path to the CSV file.
#num_records: A variable used to count the number of records processed from the CSV file.
#num_over_capacity: A variable used to count the number of rooms that are over capacity.
#try: A Python keyword used to start a block of code that will be tested for exceptions.
#mode: A parameter of open specifying the mode in which the file is opened ('r' for read mode).
#reader: A CSV reader object used to read the contents of the CSV file.
#SeatRow: A variable representing each row of data in the CSV file, where each row is a dictionary with keys and values.
#room_name: A variable extracted from each row of the CSV file representing the name of the room.
#capacity: A variable extracted from each row of the CSV file representing the maximum capacity of the room.
#attendees: A variable extracted from each row of the CSV file representing the number of people currently in the room.
#extrapeople: A variable that stores the result of the difference function, representing how many people exceed the room's capacity.
#full capacity: The situation where the number of attendees matches the maximum capacity of the room.
#empty seats: The situation where the number of attendees is less than the maximum capacity, leaving some seats unoccupied.
#FileNotFoundError: An exception raised when attempting to open a file that does not exist.
#csv.Error: An exception raised for issues related to CSV file processing.
#Exception: A general exception class for catching unexpected errors.
#---------FUNCTIONS---------------------------------------------------------------------------------------

import csv

def difference(people, max_cap):
    #Calculate the difference between the number of people and the maximum capacity.
    remain = people - max_cap
    return remain

def process_rooms(file_path):
    #Process the room data from a CSV file and display rooms that are over capacity.
    num_records = 0
    num_over_capacity = 0

    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            
            for SeatRow in reader:
                num_records += 1

                room_name = SeatRow['room_name']
                capacity = int(SeatRow['capacity'])
                attendees = int(SeatRow['attendees'])
                
                extrapeople = difference(attendees, capacity)

                if extrapeople > 0:
                    num_over_capacity += 1
                    print(f"\nThe {room_name} is over capacity by {extrapeople} people. They will need to be put on the waitlist.")
                elif extrapeople == 0:
                    print(f"\nThe {room_name} is at full capacity of {capacity} people.")
                else:
                    print(f"\nThe {room_name} has {abs(extrapeople)} empty seats available.")
        
        # Print summary
        print(f"\nNumber of records processed: {num_records}")
        print(f"Number of rooms over capacity: {num_over_capacity}")

    except FileNotFoundError:
        print(f"Error: was not found.")


# Path to the CSV file
csv_file_path = 'Lab2a.csv'

# Run the program
process_rooms(csv_file_path)
