from student import find_student

leaves = []


def apply_leave():
    print("\n========== LEAVE APPLICATION ==========")
    student_id = input("Enter Student ID: ").strip()
    if not find_student(student_id):
        print("Student not found.")
        return

    start_date = input("Enter Start Date (DD-MM-YYYY): ").strip()
    end_date = input("Enter End Date (DD-MM-YYYY): ").strip()
    reason = input("Enter Reason: ").strip()

    if not start_date or not end_date or not reason:
        print("All fields are required.")
        return

    leaves.append({
        "student_id": student_id,
        "start": start_date,
        "end": end_date,
        "reason": reason,
        "status": "Pending"
    })
    print("Leave application submitted. Status: Pending")


def view_leaves():
    print("\n========== LEAVE RECORDS ==========")
    if not leaves:
        print("No leave applications found.")
        return
    for i, leave in enumerate(leaves, 1):
        print("-" * 45)
        print(f"Leave #{i}")
        print(f"Student ID : {leave['student_id']}")
        print(f"Start Date : {leave['start']}")
        print(f"End Date   : {leave['end']}")
        print(f"Reason     : {leave['reason']}")
        print(f"Status     : {leave['status']}")


def approve_leave():
    _change_leave_status("Approved")


def reject_leave():
    _change_leave_status("Rejected")


def _change_leave_status(status):
    print(f"\n========== {status.upper()} LEAVE ==========")
    student_id = input("Enter Student ID: ").strip()
    for leave in leaves:
        if leave["student_id"] == student_id and leave["status"] == "Pending":
            leave["status"] = status
            print(f"Leave {status.lower()} successfully.")
            return
    print("Pending leave application not found.")
