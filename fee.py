from student import find_student

fees = []


def pay_fee():
    print("\n========== PAY FEE ==========")
    student_id = input("Enter Student ID: ").strip()
    if not find_student(student_id):
        print("Student not found.")
        return

    amount_text = input("Enter Fee Amount: ").strip()
    try:
        amount = float(amount_text)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Enter a valid positive amount.")
        return

    fees.append({"student_id": student_id, "amount": amount, "status": "Paid"})
    print(f"Fee of ₹{amount:.2f} recorded successfully.")


def view_fees():
    print("\n========== FEE RECORDS ==========")
    if not fees:
        print("No fee records found.")
        return
    for fee in fees:
        print("-" * 35)
        print(f"Student ID : {fee['student_id']}")
        print(f"Amount     : ₹{fee['amount']:.2f}")
        print(f"Status     : {fee['status']}")


def fee_management():
    while True:
        print("\n========== FEE MANAGEMENT ==========")
        print("1. Pay Fee")
        print("2. View Fee Records")
        print("3. Back")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            pay_fee()
        elif choice == "2":
            view_fees()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
