from student import add_student, view_students, search_student, update_student, delete_student
from room import allocate_room, room_details, vacate_room
from fee import fee_management
from complain import register_complaint, view_complaints, resolve_complaint
from leave import apply_leave, view_leaves, approve_leave, reject_leave
from reports import dashboard, student_report
from demo_data import load_demo_data
from utils import pause, header


def main():
    load_demo_data()

    while True:
        header("HOSTEL MANAGEMENT SYSTEM")
        print("1. Student Management")
        print("2. Room Management")
        print("3. Fee Management")
        print("4. Complaint Management")
        print("5. Leave Management")
        print("6. Dashboard & Reports")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            student_menu()
        elif choice == "2":
            room_menu()
        elif choice == "3":
            fee_management()
        elif choice == "4":
            complaint_menu()
        elif choice == "5":
            leave_menu()
        elif choice == "6":
            report_menu()
        elif choice == "7":
            print("\nThank you for using the Hostel Management System.")
            break
        else:
            print("Invalid choice. Please select 1-7.")
        pause()


def student_menu():
    while True:
        header("STUDENT MANAGEMENT")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
        if choice != "6":
            pause()


def room_menu():
    while True:
        header("ROOM MANAGEMENT")
        print("1. Allocate Room")
        print("2. View Room Details")
        print("3. Vacate Room")
        print("4. Back")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            allocate_room()
        elif choice == "2":
            room_details()
        elif choice == "3":
            vacate_room()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
        if choice != "4":
            pause()


def complaint_menu():
    while True:
        header("COMPLAINT MANAGEMENT")
        print("1. Register Complaint")
        print("2. View Complaints")
        print("3. Resolve Complaint")
        print("4. Back")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            register_complaint()
        elif choice == "2":
            view_complaints()
        elif choice == "3":
            resolve_complaint()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
        if choice != "4":
            pause()


def leave_menu():
    while True:
        header("LEAVE MANAGEMENT")
        print("1. Apply Leave")
        print("2. View Leaves")
        print("3. Approve Leave")
        print("4. Reject Leave")
        print("5. Back")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            apply_leave()
        elif choice == "2":
            view_leaves()
        elif choice == "3":
            approve_leave()
        elif choice == "4":
            reject_leave()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
        if choice != "5":
            pause()


def report_menu():
    while True:
        header("DASHBOARD & REPORTS")
        print("1. Dashboard")
        print("2. Student Report")
        print("3. Back")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            dashboard()
        elif choice == "2":
            student_report()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
        if choice != "3":
            pause()


if __name__ == "__main__":
    main()
