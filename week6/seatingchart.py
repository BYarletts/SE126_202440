#---------------------------------------------------------Functions----------------------------------------------------------------------------
def display_seating(seating):
  
    print("   " + " ".join([chr(65 + i) for i in range(30)]))
    for row_num in range(15):                                          #Displays the seating chart
        print(f"{row_num + 1:2} " + " ".join(seating[row_num]))
    print()

def calculate_price(row, count):
    
    if 1 <= row <= 5:
        price_per_seat = 200.00            #Cost of seats per row.
    elif 6 <= row <= 10:
        price_per_seat = 175.00
    elif 11 <= row <= 15:
        price_per_seat = 150.00
    else:
        price_per_seat = 0.00 
    return price_per_seat * count

def main():

    rows = 15
    seats_per_row = 30
    seating = [['#' for _ in range(seats_per_row)] for _ in range(rows)]
    ticket_sales = 0
    current_sales = 0
    current_ticket_count = 0
#---------------------------------------------------------Main Code---------------------------------------------------------------------
    while True:
        print("Menu:")
        print("1. Purchase Seat(s)")
        print("2. View Total Ticket Sales")   #Menu for asking user on what choice they would like to input.
        print("3. View Sales Information")
        print("4. Checkout") 
        choice = input("Enter your choice: ")

        if choice == '1':
            display_seating(seating)
            row = int(input("Enter row number (1-15): "))
            seat = input("Enter seat letter (A-Z): ").upper()
            seat_index = ord(seat) - ord('A')
            
            if seating[row - 1][seat_index] == '*':
                print("Seat is already taken.")
                continue

            count = int(input("Enter number of seats: "))

            if count <= 0 or count + seat_index > seats_per_row:
                print("Invalid number of seats.")
                continue

            if any(seating[row - 1][seat_index + i] == '*' for i in range(count)):
                print("Some of the seats are already taken.")
                continue

            for i in range(count):
                seating[row - 1][seat_index + i] = '*'

            price = calculate_price(row, count)
            current_sales += price
            current_ticket_count += count
            print(f"Seats successfully booked. Total cost: ${price:.2f}")           
            print()

        elif choice == '2':
            print(f"Total ticket sales so far: ${ticket_sales:.2f}")      #Total ticket sales
            print()

        elif choice == '3':
            total_sold = sum(row.count('*') for row in seating)
            total_available = rows * seats_per_row - total_sold
            print(f"Total seats sold: {total_sold}")
            print(f"Total seats available: {total_available}")       #Number 3 asks for the information on what seats are left after buying.
            for row_num, row in enumerate(seating):
                available_in_row = row.count('#')
                print(f"Row {row_num + 1} has {available_in_row} seats available")
            print()

        elif choice == '4':
            if current_ticket_count == 0:
                print("No tickets to check out.")
                continue

            print(f"Checking out: {current_ticket_count} tickets")           
            print(f"Total cost: ${current_sales:.2f}")
            amount_paid = float(input("Enter amount paid: $"))
            if amount_paid < current_sales:
                print("Insufficient amount. Transaction cancelled.")
                continue
            
            change = amount_paid - current_sales
            print(f"Change to be returned: ${change:.2f}")

            ticket_sales += current_sales                        #calculates the change due at the end
            current_sales = 0
            current_ticket_count = 0
            print("Checkout complete. Thank you!\n")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
