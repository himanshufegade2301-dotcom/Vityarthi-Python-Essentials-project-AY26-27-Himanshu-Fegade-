from student import students
from room import rooms
from fee import fees
from complain import complaints
from leave import leaves


def dashboard():
    print("\n========== HOSTEL DASHBOARD ==========")
    total_capacity = sum(r["capacity"] for r in rooms.values())
    occupied = sum(len(r["students"]) for r in rooms.values())
    pending_complaints = sum(c["status"] == "Pending" for c in complaints)
    pending_leaves = sum(l["status"] == "Pending" for l in leaves)
    total_fees = sum(f["amount"] for f in fees)

    print(f"Total Students       : {len(students)}")
    print(f"Total Rooms          : {len(rooms)}")
    print(f"Bed Capacity         : {total_capacity}")
    print(f"Occupied Beds        : {occupied}")
    print(f"Available Beds       : {total_capacity - occupied}")
    print(f"Pending Complaints   : {pending_complaints}")
    print(f"Pending Leave Apps   : {pending_leaves}")
    print(f"Recorded Fee Amount  : ₹{total_fees:.2f}")


def student_report():
    print("\n========== STUDENT REPORT ==========")
    student_id = input("Enter Student ID: ").strip()

    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        print("Student not found.")
        return

    print(f"\nStudent: {student['name']} ({student['id']})")
    print(f"Course/Branch: {student['course']} / {student['branch']}")
    print(f"Room: {student['room']}")

    student_fees = [f for f in fees if f["student_id"] == student_id]
    student_complaints = [c for c in complaints if c["student_id"] == student_id]
    student_leaves = [l for l in leaves if l["student_id"] == student_id]

    print(f"Fees Recorded: ₹{sum(f['amount'] for f in student_fees):.2f}")
    print(f"Complaints: {len(student_complaints)}")
    print(f"Leave Applications: {len(student_leaves)}")
