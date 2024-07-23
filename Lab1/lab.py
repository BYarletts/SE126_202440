#W1D2 SE116 Review Demo - split into prts in Canvas

#Braedin Yarletts
#Lab #1 
#July 22th 


#VARIBLE DICTIONARY
#---------------------------------------------------------------------------------------------------------
#restart: Stores the user's decision to restart the program ('y' or 'n').
#meeting: Stores the name of the meeting entered by the user.
#capacity: Stores the maximum capacity of the meeting room entered by the user.
#AmountAttendees: Stores the number of people attending the meeting entered by the user.
#remainingSeats: Stores the result of the difference() function, representing remaining or excess capacity.
#people: Number of people attending the meeting.
#max_cap: Maximum capacity of the meeting room.

#---------FUNCTIONS---------------------------------------------------------------------------------------

def difference(people, max_cap):
    remain = max_cap - people 
    return remain


def decision(response):
    while response != 'y' and response != 'n':
        print("Invalid input. Please enter 'y' or 'n'.")
        response = input()  # Prompt for user input again
    
    if response == 'y':
        return "y"
    elif response == 'n':
        return "n"
    else:
        print("There was an Error.")


#---------MAIN CORE---------------------------------------------------------------------------------------
restart = "y"
while restart == "y":
    meeting = input("\nPlease enter the name of the meeting: ")
    capacity = int(input("Please enter the room's capacity: "))
    AmountAttendees = int(input("Please enter the number of people attending: "))
    
    remainingSeats = difference(AmountAttendees, capacity)

    if remainingSeats < 0:
        remainingSeats *= -1
        print(f"\nThe {AmountAttendees} attendees will be at the {meeting} meeting, you must get rid of {remainingSeats} people to fit the capacity.")
    elif remainingSeats == 0:
        print(f"\nThe {meeting} is at full capacity of {capacity} people so no more can attend at this time.")
    elif remainingSeats > 0:
        print(f"\nThe {meeting} is below the capacity it needs of {capacity} people, please invite {remainingSeats} more to reach max capacity.")
    else:
        print("Error: Invalid")

    restart = decision(input("\nDo you want to restart? (y/n): ").lower())
