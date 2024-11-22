import csv 
bookings = []
check_ins = []
services = []
bills = {}
def display():
    
    print("=" * 60)
    print(" " * 15 + "KANHA MAKHAN PUBLIC SCHOOL")
    print(" " * 10 + "PROJECT: HOTEL MANAGEMENT SYSTEM")
    print("=" * 60)
    print("Student Name: Sumit Kumar")
    print("Assisted By: Utkarsh Sharma")
    print("=" * 60)


rooms = {
    "101": {"type": "single", "price": 100, "available": True},
    "102": {"type": "double", "price": 200, "available": True},
    "103": {"type": "suite", "price": 500, "available": True},
    "104": {"type": "single", "price": 100, "available": True},
    "105": {"type": "double", "price": 200, "available": True},
}


def save_data_to_csv():
  
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["type", "data"])

      
        for room_number, details in rooms.items():
            writer.writerow(["rooms", f"{room_number},{details['type']},{details['price']},{details['available']}"])

        
        for booking in bookings:
            writer.writerow(["bookings", f"{booking['room_number']},{booking['guest_name']},{booking['contact_details']},{booking['duration']}"])

      
        for service in services:
            writer.writerow(["services", f"{service['room_number']},{service['service']},{service['cost']}"])

      
        for guest_name, charges in bills.items():
            writer.writerow(["bills", f"{guest_name},{charges['room_charge']},{charges['service_charge']},{charges['total']}"])

    print("Data saved successfully to CSV.\n")


def load_data_from_csv():
    
    try:
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  

            for row in reader:
                data_type, data = row
                if data_type == "rooms":
                    room_number, room_type, price, available = data.split(",")
                    rooms[room_number] = {"type": room_type, "price": float(price), "available": available == "True"}
                elif data_type == "bookings":
                    room_number, guest_name, contact_details, duration = data.split(",")
                    bookings.append({"room_number": room_number, "guest_name": guest_name, "contact_details": contact_details, "duration": int(duration)})
                elif data_type == "services":
                    room_number, service, cost = data.split(",")
                    services.append({"room_number": room_number, "service": service, "cost": float(cost)})
                elif data_type == "bills":
                    guest_name, room_charge, service_charge, total = data.split(",")
                    bills[guest_name] = {"room_charge": float(room_charge), "service_charge": float(service_charge), "total": float(total)}

        print("Data loaded successfully from CSV.\n")
    except FileNotFoundError:
        print("No previous data file found. Starting fresh.\n")

occupancy_history = []  
revenue_stack = []      
service_usage_stack = []  

def add_room():

    room_number = input("Enter room number: ")
    if room_number in rooms:
        print("Room number already exists.")
        return
    room_type = input("Enter room type (single, double, suite): ").lower()
    if room_type not in ["single", "double", "suite"]:
        print("Invalid room type.")
        return
    try:
        price = float(input("Enter price per night: "))
    except ValueError:
        print("Invalid price entered.")
        return
    rooms[room_number] = {"type": room_type, "price": price, "available": True}
    print(f"Room {room_number} added successfully.")

def view_rooms():
    
    print("\n--- Room Details ---")
    for room, details in sorted(rooms.items()):
        status = "Available" if details['available'] else "Occupied"
        print(f"Room Number: {room}, Type: {details['type'].capitalize()}, Price: ${details['price']}, Status: {status}")
    print("---------------------\n")

def update_room_availability(room_number, availability):
    
    if room_number in rooms:
        rooms[room_number]["available"] = availability
        
        occupancy_history.append({"room_number": room_number, "status": availability})
    else:
        print("Room not found.")

def book_room():

    print("\n--- Book a Room ---")
    guest_name = input("Enter guest name: ").strip()
    contact_details = input("Enter contact details: ").strip()
    room_type = input("Enter room type to book (single, double, suite): ").lower()
    
    
    available_rooms = [room for room, details in rooms.items() if details["type"] == room_type and details["available"]]
    
    if not available_rooms:
        print(f"No available {room_type} rooms.")
        return
    
    print(f"Available {room_type} rooms: {', '.join(available_rooms)}")
    room_number = input("Enter room number to book: ").strip()
    
    if room_number not in rooms or rooms[room_number]["type"] != room_type or not rooms[room_number]["available"]:
        print("Invalid room selection.")
        return
    
    try:
        duration = int(input("Enter duration of stay (nights): "))
        if duration <= 0:
            print("Duration must be at least 1 night.")
            return
    except ValueError:
        print("Invalid duration entered.")
        return
    
    booking = {
        "room_number": room_number,
        "guest_name": guest_name,
        "contact_details": contact_details,
        "duration": duration
    }
    bookings.append(booking)  
    update_room_availability(room_number, False)
    print(f"Room {room_number} booked successfully for {guest_name}.\n")

def view_bookings():

    print("\n--- Current Bookings ---")
    if not bookings:
        print("No current bookings.")
    else:
        for idx, booking in enumerate(bookings, start=1):
            print(f"{idx}. Room {booking['room_number']} - Guest: {booking['guest_name']}, Contact: {booking['contact_details']}, Duration: {booking['duration']} nights")
    print("------------------------\n")

def cancel_booking():
    
    print("\n--- Cancel Booking ---")
    if bookings:
        last_booking = bookings.pop()  
        room_number = last_booking["room_number"]
        update_room_availability(room_number, True)
        print(f"Cancelled booking for {last_booking['guest_name']} in room {room_number}.\n")
    else:
        print("No bookings to cancel.\n")

def check_in():
    
    print("\n--- Check-In Guest ---")
    room_number = input("Enter room number: ").strip()
    if room_number in rooms and not rooms[room_number]["available"]:
    
        booking = next((b for b in bookings if b["room_number"] == room_number), None)
        if not booking:
            print("No booking found for this room.")
            return
        guest_name = booking["guest_name"]
        check_in_record = {
            "room_number": room_number,
            "guest_name": guest_name
        }
        check_ins.append(check_in_record)  
        print(f"Guest {guest_name} checked into room {room_number} successfully.\n")
    else:
        print("Room not available or not booked.\n")

def check_out():

    print("\n--- Check-Out Guest ---")
    if check_ins:
        last_check_in = check_ins.pop()  
        room_number = last_check_in["room_number"]
        guest_name = last_check_in["guest_name"]
        booking = next((b for b in bookings if b["room_number"] == room_number and b["guest_name"] == guest_name), None)
        if booking:
            total_charge = rooms[room_number]["price"] * booking["duration"]
    
            additional_services = [s for s in services if s["room_number"] == room_number]
            service_total = sum(service["cost"] for service in additional_services)
            total_charge += service_total
            bills[guest_name] = {
                "room_charge": rooms[room_number]["price"] * booking["duration"],
                "service_charge": service_total,
                "total": total_charge
            }
    
            bookings.remove(booking)
            
            update_room_availability(room_number, True)
            
            revenue_stack.append(total_charge)
            print(f"Guest {guest_name} checked out from room {room_number} successfully.")
            print(f"Total Charge: Room - ${rooms[room_number]['price'] * booking['duration']}, Services - ${service_total}, Total - ${total_charge}\n")
        
            services[:] = [s for s in services if s["room_number"] != room_number]
        else:
            print("No corresponding booking found for this check-in.\n")
    else:
        print("No guests to check out.\n")

def add_service():

    print("\n--- Add Service ---")
    room_number = input("Enter room number: ").strip()
    if room_number not in rooms:
        print("Room does not exist.")
        return
    if rooms[room_number]["available"]:
        print("Room is currently available. Cannot add services to an available room.")
        return
    service = input("Enter service (e.g., room service, laundry): ").strip().lower()
    try:
        cost = float(input("Enter cost of the service: "))
        if cost < 0:
            print("Cost cannot be negative.")
            return
    except ValueError:
        print("Invalid cost entered.")
        return
    service_record = {
        "room_number": room_number,
        "service": service,
        "cost": cost
    }
    services.append(service_record)  # Push to services stack
    service_usage_stack.append(service_record)  # Track service usage
    print(f"Service '{service}' added to room {room_number} successfully.\n")

def view_services():
    
    print("\n--- Additional Services ---")
    if not services:
        print("No additional services availed.")
    else:
        for idx, service in enumerate(services, start=1):
            print(f"{idx}. Room {service['room_number']} - Service: {service['service'].capitalize()}, Cost: ${service['cost']}")
    print("----------------------------\n")

def view_bills():
    print("\n--- Bills ---")
    if not bills:
        print("No bills generated yet.")
    else:
        for guest, charges in bills.items():
            print(f"Guest Name: {guest}")
            print(f"  Room Charge: ${charges['room_charge']}")
            print(f"  Service Charge: ${charges['service_charge']}")
            print(f"  Total Charge: ${charges['total']}\n")
    print("--------------\n")

def occupancy_report():

    print("\n--- Occupancy Report ---")
    if not occupancy_history:
        print("No occupancy changes recorded.")
    else:
        occupied_rooms = [room for room, details in rooms.items() if not details["available"]]
        print(f"Total Rooms: {len(rooms)}")
        print(f"Occupied Rooms: {len(occupied_rooms)}")
        print(f"Occupancy Rate: { (len(occupied_rooms)/len(rooms)) * 100 }%\n")
    print("-------------------------\n")

def revenue_report():
    
    print("\n--- Revenue Report ---")
    total_revenue = sum(revenue_stack)
    print(f"Total Revenue: ${total_revenue}\n")
    print("------------------------\n")

def service_usage_report():
    print("\n--- Service Usage Report ---")
    if not service_usage_stack:
        print("No services have been used.")
    else:
        service_counts = {}
        for service in service_usage_stack:
            service_name = service["service"]
            service_counts[service_name] = service_counts.get(service_name, 0) + 1
        for service, count in service_counts.items():
            print(f"Service: {service.capitalize()}, Times Used: {count}")
    print("-----------------------------\n")

def undo_last_operation():

    print("\n--- Undo Last Operation ---")
    if bookings:
        last_booking = bookings.pop()
        room_number = last_booking["room_number"]
        update_room_availability(room_number, True)
        print(f"Undid booking for {last_booking['guest_name']} in room {room_number}.\n")
    elif services:
        last_service = services.pop()
        service_usage_stack.pop()
        print(f"Removed last service '{last_service['service']}' from room {last_service['room_number']}.\n")
    else:
        print("No operations to undo.\n")

def main_menu():
    
    while True:
        display()
        print("========== Hotel Management System ==========")
        
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
        print("11. Generate Occupancy Report")
        print("12. Generate Revenue Report")
        print("13. Generate Service Usage Report")
        print("14. Undo Last Operation")
        print("15. Exit")
        print("==============================================")
        
        choice = input("Enter your choice (1-15): ").strip()
        
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
        elif choice == "6":
            check_in()
        elif choice == "7":
            check_out()
        elif choice == "8":
            add_service()
        elif choice == "9":
            view_services()
        elif choice == "10":
            view_bills()
        elif choice == "11":
            occupancy_report()
        elif choice == "12":
            revenue_report()
        elif choice == "13":
            service_usage_report()
        elif choice == "14":
            undo_last_operation()
        elif choice == "15":
            print("Exiting Hotel Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
