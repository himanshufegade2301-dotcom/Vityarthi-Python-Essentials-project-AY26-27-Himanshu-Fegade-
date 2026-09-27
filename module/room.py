from student import students, find_student

rooms = {
    "A101": {"capacity": 3, "students": []},
    "A102": {"capacity": 3, "students": []},
    "A103": {"capacity": 3, "students": []},
    "B101": {"capacity": 3, "students": []},
    "B102": {"capacity": 3, "students": []},
    "B103": {"capacity": 3, "students": []},
    "A201": {"capacity": 3, "students": []},
    "A202": {"capacity": 3, "students": []},
    "A203": {"capacity": 3, "students": []},
    "B201": {"capacity": 3, "students": []},
    "B202": {"capacity": 3, "students": []},
    "B203": {"capacity": 3, "students": []},
}


def allocate_room():
    print("\n========== ROOM ALLOCATION ==========")
    student_id = input("Enter Student ID: ").strip()
    student = find_student(student_id)

    if not student:
        print("Student not found.")
        return
    if student["room"] != "Not Allocated":
        print(f"Student already has room {student['room']}.")
        return

    print("\nAvailable Rooms:")
    for number, room in rooms.items():
        available = room["capacity"] - len(room["students"])
        if available:
            print(f"{number}: {available} bed(s) available")

    room_number = input("Enter Room Number: ").strip().upper()
    if room_number not in rooms:
        print("Invalid room number.")
        return

    room = rooms[room_number]
    if len(room["students"]) >= room["capacity"]:
        print("Room is full.")
        return

    room["students"].append(student_id)
    student["room"] = room_number
    print(f"Room {room_number} allocated to {student['name']}.")


def vacate_room():
    print("\n========== VACATE ROOM ==========")
    student = find_student(input("Enter Student ID: ").strip())
    if not student:
        print("Student not found.")
        return
    if student["room"] == "Not Allocated":
        print("Student has no allocated room.")
        return

    room_number = student["room"]
    if student["id"] in rooms[room_number]["students"]:
        rooms[room_number]["students"].remove(student["id"])
    student["room"] = "Not Allocated"
    print("Room vacated successfully.")


def room_details():
    print("\n========== ROOM DETAILS ==========")
    for number, room in rooms.items():
        occupied = len(room["students"])
        print(f"{number} | Capacity: {room['capacity']} | "
              f"Occupied: {occupied} | Available: {room['capacity'] - occupied}")
        print(f"Students: {', '.join(room['students']) if room['students'] else 'None'}")
