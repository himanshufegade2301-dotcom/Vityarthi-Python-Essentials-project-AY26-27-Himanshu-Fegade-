from student import students
from room import rooms
from fee import fees
from complain import complaints
from leave import leaves


_loaded = False


def load_demo_data():
    global _loaded
    if _loaded:
        return

    students.extend([
        {"id": "ST101", "name": "Aarav Sharma", "course": "B.Tech",
         "branch": "CSE", "year": "1", "phone": "9876543210", "room": "A101"},
        {"id": "ST102", "name": "Riya Verma", "course": "B.Tech",
         "branch": "AIML", "year": "1", "phone": "9876543211", "room": "A101"},
        {"id": "ST103", "name": "Kabir Singh", "course": "B.Tech",
         "branch": "ECE", "year": "1", "phone": "9876543212", "room": "A102"},
        {"id": "ST104", "name": "Ananya Gupta", "course": "B.Tech",
         "branch": "CSE", "year": "1", "phone": "9876543213", "room": "Not Allocated"},
    ])

    rooms["A101"]["students"].extend(["ST101", "ST102"])
    rooms["A102"]["students"].append("ST103")

    fees.extend([
        {"student_id": "ST101", "amount": 85000.0, "status": "Paid"},
        {"student_id": "ST102", "amount": 85000.0, "status": "Paid"},
    ])

    complaints.extend([
        {"student_id": "ST103", "complaint": "Room light not working", "status": "Pending"},
        {"student_id": "ST101", "complaint": "Water dispenser issue", "status": "Resolved"},
    ])

    leaves.extend([
        {"student_id": "ST104", "start": "28-09-2026", "end": "30-09-2026",
         "reason": "Family function", "status": "Pending"},
        {"student_id": "ST102", "start": "15-09-2026", "end": "16-09-2026",
         "reason": "Personal work", "status": "Approved"},
    ])

    _loaded = True
