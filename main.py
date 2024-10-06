# Hotel Management System

# Initialize empty stacks for bookings, check-ins, and services
bookings = []
check_ins = []
services = []

# Initialize room details
rooms = {
    "101": {"type": "single", "price": 100, "available": True},
    "102": {"type": "double", "price": 200, "available": True},
    "103": {"type": "suite", "price": 500, "available": True},
    "104": {"type": "single", "price": 100, "available": True},
    "105": {"type": "double", "price": 200, "available": True},
}

# Initialize bills
bills = {}

def add_room():
    room_number = input("Enter room number: ")
    room_type = input("Enter room type (single, double, suite): ")
    price = int(input("Enter price per night: "))
    rooms[room_number] = {"type": room_type, "price": price, "available": True}
    print("Room added successfully.")

def view_rooms():
    for room, details in rooms.items():
        print(f"Room Number: {room}, Type: {details['type']}, Price: {details['price']}, Available: {details['available']}")

def update_room_availability(room_number, availability):
    if room_number in rooms:
        rooms[room_number]["available"] = availability
    else:
        print("Room not found.")

def book_room():
    room_number = input("Enter room number: ")
    if room_number in rooms and rooms[room_number]["available"]:
        guest_name = input("Enter guest name: ")
        contact_details = input("Enter contact details: ")
        duration = int(input("Enter duration of stay: "))
        bookings.append({"room_number": room_number, "guest_name": guest_name, "contact_details": contact_details, "duration": duration})
        update_room_availability(room_number, False)
        print("Room booked successfully.")
    else:
        print("Room not available or not found.")

def view_bookings():
    for booking in bookings:
        print(f"Room Number: {booking['room_number']}, Guest Name: {booking['guest_name']}, Contact Details: {booking['contact_details']}, Duration: {booking['duration']}")

def cancel_booking():
    if bookings:
        last_booking = bookings.pop()
        update_room_availability(last_booking["room_number"], True)
        print("Booking cancelled successfully.")
    else:
        print("No bookings to cancel.")

def check_in():
    room_number = input("Enter room number: ")
    if room_number in rooms and not rooms[room_number]["available"]:
        guest_name = input("Enter guest name: ")
        check_ins.append({"room_number": room_number, "guest_name": guest_name})
        print("Guest checked in successfully.")
    else:
        print("Room not available or not booked.")

def check_out():
    if check_ins:
        last_check_in = check_ins.pop()
        room_number = last_check_in["room_number"]
        guest_name = last_check_in["guest_name"]
        duration = len([check_in for check_in in check_ins if check_in["room_number"] == room_number])
        total_charge = rooms[room_number]["price"] * duration
        bills[guest_name] = total_charge
        update_room_availability(room_number, True)
        print("Guest checked out successfully.")
    else:
        print("No guests to check out.")

def add_service():
    room_number = input("Enter room number: ")
    service = input("Enter service (room service, laundry): ")
    cost = int(input("Enter cost: "))
    services.append({"room_number": room_number, "service": service, "cost": cost})
    print("Service added successfully.")

def view_services():
    for service in services:
        print(f"Room Number: {service['room_number']}, Service: {service['service']}, Cost: {service['cost']}")

def view_bills():
    for guest, total_charge in bills.items():
        print(f"Guest Name: {guest}, Total Charge: {total_charge}")

def main():
    while True:
        print("Hotel Management System")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Book Room")
        print("4. View Bookings")
        print("5. Cancel Booking")
        print("6. Check In")
        print("7. Check Out")
        print("8. Add Service")
        print("9. View Services")
        print("10. View Bills")
        print("11. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_room()
        elif choice == 2:
            view_rooms()
        elif choice == 3:
            book_room()
        elif choice == 4:
            view_bookings()
        elif choice == 5:
            cancel_booking()
        elif choice == 6:
            check_in()
        elif choice == 7:
            check_out()
        elif choice == 8:
            add_service()
        elif choice == 9:
            view_services()
        elif choice == 10:
            view_bills()
        elif choice == 11:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()