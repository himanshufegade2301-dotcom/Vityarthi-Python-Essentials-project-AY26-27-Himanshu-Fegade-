students = []


def find_student(student_id):
    return next((s for s in students if s["id"] == student_id), None)


def add_student():
    print("\n========== ADD STUDENT ==========")
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if find_student(student_id):
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()
    branch = input("Enter Branch: ").strip()
    year = input("Enter Year: ").strip()
    phone = input("Enter Phone Number: ").strip()

    if not all([name, course, branch, year, phone]):
        print("All fields are required.")
        return
    if not phone.isdigit() or len(phone) != 10:
        print("Phone number must contain exactly 10 digits.")
        return

    students.append({
        "id": student_id, "name": name, "course": course,
        "branch": branch, "year": year, "phone": phone,
        "room": "Not Allocated"
    })
    print("Student added successfully.")


def view_students():
    print("\n========== ALL STUDENTS ==========")
    if not students:
        print("No student records found.")
        return
    for s in students:
        print("-" * 45)
        print(f"ID     : {s['id']}")
        print(f"Name   : {s['name']}")
        print(f"Course : {s['course']}")
        print(f"Branch : {s['branch']}")
        print(f"Year   : {s['year']}")
        print(f"Phone  : {s['phone']}")
        print(f"Room   : {s['room']}")


def search_student():
    print("\n========== SEARCH STUDENT ==========")
    student_id = input("Enter Student ID: ").strip()
    student = find_student(student_id)
    if not student:
        print("Student not found.")
        return
    for key, value in student.items():
        print(f"{key.title():8}: {value}")


def update_student():
    print("\n========== UPDATE STUDENT ==========")
    student = find_student(input("Enter Student ID: ").strip())
    if not student:
        print("Student not found.")
        return

    name = input(f"Name [{student['name']}]: ").strip()
    phone = input(f"Phone [{student['phone']}]: ").strip()

    if name:
        student["name"] = name
    if phone:
        if not phone.isdigit() or len(phone) != 10:
            print("Invalid phone number.")
            return
        student["phone"] = phone
    print("Student updated successfully.")


def delete_student():
    print("\n========== DELETE STUDENT ==========")
    student_id = input("Enter Student ID: ").strip()
    student = find_student(student_id)
    if not student:
        print("Student not found.")
        return
    students.remove(student)
    print("Student deleted successfully.")
