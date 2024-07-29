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
            
            for row in reader:
                num_records += 1

                room_name = row['room_name']
                capacity = int(row['capacity'])
                attendees = int(row['attendees'])
                
                excess_people = difference(attendees, capacity)

                if excess_people > 0:
                    num_over_capacity += 1
                    print(f"\nThe {room_name} is over capacity by {excess_people} people. They will need to be put on the waitlist.")
                elif excess_people == 0:
                    print(f"\nThe {room_name} is at full capacity of {capacity} people.")
                else:
                    print(f"\nThe {room_name} has {abs(excess_people)} empty seats available.")
        
        # Print summary
        print(f"\nNumber of records processed: {num_records}")
        print(f"Number of rooms over capacity: {num_over_capacity}")

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except csv.Error as e:
        print(f"Error: Problem reading CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

