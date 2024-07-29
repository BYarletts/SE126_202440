import csv

def difference(people, max_cap):
    """Calculate the difference between the number of people and the maximum capacity."""
    remain = people - max_cap
    return remain

def process_rooms(file_path):
    """Process the room data from a CSV file and display rooms that are over capacity."""
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
    except csv.Error as e:
        print(f"Error: Problem: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Path to the CSV file
csv_file_path = 'Lab2a.csv'

# Run the program
process_rooms(csv_file_path)
