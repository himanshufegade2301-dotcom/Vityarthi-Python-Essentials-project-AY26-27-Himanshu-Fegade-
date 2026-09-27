# Design Documentation

## 1. System Architecture

User
  |
  v
Main Menu (`main.py`)
  |
  +--> Student Module
  +--> Room Module
  +--> Fee Module
  +--> Complaint Module
  +--> Leave Module
  +--> Reports Module
  |
  v
In-memory Python data structures

## 2. Workflow

Start
 -> Load Demo Data
 -> Display Main Menu
 -> Select Module
 -> Validate Input
 -> Perform Operation
 -> Display Result
 -> Return to Menu
 -> Exit

## 3. Use Case Diagram - Text Representation

Actor: Hostel Administrator

Administrator -> Manage Students
Administrator -> Allocate/Vacate Rooms
Administrator -> Manage Fees
Administrator -> Register/View/Resolve Complaints
Administrator -> Apply/View/Approve/Reject Leaves
Administrator -> View Dashboard
Administrator -> Generate Student Report

## 4. Component/Class View

main.py
  -> student.py
  -> room.py
  -> fee.py
  -> complain.py
  -> leave.py
  -> reports.py
  -> demo_data.py
  -> utils.py

Shared entities:
Student, Room, Fee, Complaint, Leave

## 5. Sequence Example: Room Allocation

Administrator
 -> Main Menu
 -> Room Management
 -> Allocate Room
 -> Search Student
 -> Validate Room
 -> Add Student ID to Room
 -> Update Student Room
 -> Display Confirmation

## 6. Storage Design

The prototype uses Python lists and dictionaries rather than a database.

Student:
id, name, course, branch, year, phone, room

Room:
room number, capacity, student IDs

Fee:
student ID, amount, status

Complaint:
student ID, complaint, status

Leave:
student ID, start date, end date, reason, status

## 7. Non-Functional Requirements

### Performance
Operations should complete immediately for the intended small hostel dataset.

### Usability
The application uses clear menus, labels, confirmations, and simple text-based interaction.

### Reliability
Validation prevents common invalid inputs and inconsistent room allocation.

### Maintainability
Features are separated into focused Python modules.

### Error Handling
Invalid IDs, duplicate IDs, invalid amounts, invalid phone numbers, full rooms, and missing records are handled with user-friendly messages.

### Scalability
The modular design allows future replacement of in-memory storage with SQLite or another database.

### Resource Efficiency
The application uses only standard Python data structures and requires no external packages.

## 8. Design Decisions

A console interface was selected because the course project focuses on programming concepts and modular implementation rather than web development. In-memory structures keep the project easy to understand and run. Modules separate responsibilities so each major feature can be developed and tested independently.

## 9. Future Enhancements

- SQLite/MySQL persistence
- Login and role-based access
- GUI/web interface
- Export reports to CSV/PDF
- Attendance integration
- Automated notifications
- Database-backed search and analytics
