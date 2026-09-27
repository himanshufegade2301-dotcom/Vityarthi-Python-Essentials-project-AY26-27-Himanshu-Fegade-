from student import find_student

complaints = []


def register_complaint():
    print("\n========== REGISTER COMPLAINT ==========")
    student_id = input("Enter Student ID: ").strip()
    if not find_student(student_id):
        print("Student not found.")
        return

    complaint = input("Enter Complaint: ").strip()
    if not complaint:
        print("Complaint cannot be empty.")
        return

    complaints.append({
        "student_id": student_id,
        "complaint": complaint,
        "status": "Pending"
    })
    print("Complaint registered successfully. Status: Pending")


def view_complaints():
    print("\n========== COMPLAINT RECORDS ==========")
    if not complaints:
        print("No complaints found.")
        return
    for i, complaint in enumerate(complaints, 1):
        print("-" * 45)
        print(f"Complaint #{i}")
        print(f"Student ID : {complaint['student_id']}")
        print(f"Complaint  : {complaint['complaint']}")
        print(f"Status     : {complaint['status']}")


def resolve_complaint():
    print("\n========== RESOLVE COMPLAINT ==========")
    pending = [c for c in complaints if c["status"] == "Pending"]
    if not pending:
        print("No pending complaints.")
        return

    student_id = input("Enter Student ID: ").strip()
    for complaint in pending:
        if complaint["student_id"] == student_id:
            complaint["status"] = "Resolved"
            print("Complaint resolved successfully.")
            return
    print("Pending complaint not found.")
