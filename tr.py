Here’s the code without any comments or explanatory text:

```python
import csv
import os

rooms_file = "rooms.csv"
bookings_file = "bookings.csv"
services_file = "services.csv"

def initialize_files():
    if not os.path.exists(rooms_file):
        with open(rooms_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Room Number", "Room Type", "Price", "Status"])
    if not os.path.exists(bookings_file):
        with open(bookings_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Booking ID", "Room Number", "Customer Name", "Check-in Date", "Check-out Date", "Status"])
    if not os.path.exists(services_file):
        with open(services_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Service Name", "Price"])

def add_room():
    room_number = input("Enter Room Number: ")
    room_type = input("Enter Room Type (Single/Double/Suite): ")
    price = input("Enter Price: ")
    status = "Available"
    with open(rooms_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([room_number, room_type, price, status])
    print("Room added successfully.")

def view_rooms():
    with open(rooms_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def book_room():
    booking_id = input("Enter Booking ID: ")
    room_number = input("Enter Room Number: ")
    customer_name = input("Enter Customer Name: ")
    check_in = input("Enter Check-in Date (YYYY-MM-DD): ")
    check_out = input("Enter Check-out Date (YYYY-MM-DD): ")
    status = "Booked"
    with open(bookings_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([booking_id, room_number, customer_name, check_in, check_out, status])
    print("Room booked successfully.")

def view_bookings():
    with open(bookings_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def cancel_booking():
    booking_id = input("Enter Booking ID to Cancel: ")
    updated_data = []
    found = False
    with open(bookings_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == booking_id:
                found = True
                row[5] = "Cancelled"
            updated_data.append(row)
    with open(bookings_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_data)
    if found:
        print("Booking cancelled successfully.")
    else:
        print("Booking ID not found.")

def add_service():
    service_name = input("Enter Service Name: ")
    price = input("Enter Service Price: ")
    with open(services_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([service_name, price])
    print("Service added successfully.")

def view_services():
    with open(services_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main_menu():
    initialize_files()
    while True:
        print("""
============================================================
               KANHA MAKHAN PUBLIC SCHOOL
          PROJECT: HOTEL MANAGEMENT SYSTEM
============================================================
1. Add Room
2. View Rooms
3. Book Room
4. View Bookings
5. Cancel Booking
6. Check In
7. Check Out
8. Add Service
9. View Services
10. View Bills
11. Generate Occupancy Report
12. Generate Revenue Report
13. Generate Service Usage Report
14. Undo Last Operation
15. Exit
============================================================
        """)
        choice = input("Enter your choice (1-15): ")
        if choice == "1":
            add_room()
        elif choice == "2":
            view_rooms()
        elif choice == "3":
            book_room()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            cancel_booking()
        elif choice == "8":
            add_service()
        elif choice == "9":
            view_services()
        elif choice == "15":
            print("Exiting... Data saved successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
```
