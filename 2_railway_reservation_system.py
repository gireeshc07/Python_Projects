"                                   🐍 Train Ticket Booking System 🐍                                                       "

MAX_SEATS = 50
MAX_NAME_LENGTH = 50

# Class to store booking details
class Booking:
    def __intit__(self):
        self.name = ""
        self.age = 0    
        self.source = ""
        self.destination = ""
        self.seat_number = 0
        self.is_booked = False

train = [Booking() for i in range(MAX_SEATS)] # List to store booking details

# Initialize the train seats as displayAvailableSeats
def initializeSeats():
    for i in range(MAX_SEATS):
        # False represents aviailability of seat
        train[i].is_booked = False

# Function to display available seats
def displayAvailableSeats():
    print("Available Seats:")
    for i in range(MAX_SEATS):
        if not train[i].is_booked:
            print(f"Seat {i + 1}")

# Function to book a seat
def bookSeat():
    seat_number = int(input("Enter seat number to book: ")) - 1 # adjust index

    if seat_number < 0 or seat_number >= MAX_SEATS:
        print("Invalid seat number! Please try again.")
        return
    
    if train[seat_number].is_booked:
        print("Seat already booked! Please try again.")
        return  
    
    else:
        train[seat_number].is_booked = True
        train[seat_number].name = input("Enter your name: ")

        try:
            train[seat_number].age = int(input("Enter your age: "))
        except:
            print("Exception: Only integers are allowed for age")
            try:
                train[seat_number].age = int(input("Enter your age: "))
            except:
                print("Invalid input for age. Please try again.")
                return
        
        train[seat_number].source = input("Enter source station: ")
        train[seat_number].destination = input("Enter destination station: ")
        print(f"Seat {seat_number + 1} booked successfully!")

# Function to cancel a seat booking
def cancelSeat():
    seat_number = int(input("Enter seat number to cancel booking: ")) - 1 # adjust index

    if seat_number < 0 or seat_number >= MAX_SEATS:
        print("Invalid seat number! Please try again.")
        return
    
    if not train[seat_number].is_booked:
        print("Seat not booked! Please try again.")
        return  
    
    else:
        train[seat_number].is_booked = False
        train[seat_number].name = ""
        train[seat_number].age = 0
        train[seat_number].source = ""
        train[seat_number].destination = ""
        print(f"Booking for seat {seat_number + 1} cancelled successfully!")

# Function to print ticket details
def printTicket(seat_number):
    if seat_number < 0 or seat_number >= MAX_SEATS:
        print("Invalid seat number! Please try again.")
        return
    
    if not train[seat_number].is_booked:
        print("Seat not booked! Please try again.")
        return  
    
    else:
        print("Ticket Details:")
        print(f"Name: {train[seat_number].name}")
        print(f"Age: {train[seat_number].age}")
        print(f"Source: {train[seat_number].source}")
        print(f"Destination: {train[seat_number].destination}")
        print(f"Seat Number: {seat_number + 1}")

def main():
    initializeSeats()
    choice = 0
    while choice != 5:
        print("Train Ticket Booking System")
        print("1. Display Available Seats")
        print("2. Book a Seat")
        print("3. Cancel a Seat Booking")
        print("4. Print Ticket")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            displayAvailableSeats()
        elif choice == 2:
            bookSeat()
        elif choice == 3:
            cancelSeat()
        elif choice == 4:
            seat_number = int(input("Enter seat number to print ticket: "))
            printTicket(seat_number)
        elif choice == 5:
            print("Thank you for using our service!")
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()