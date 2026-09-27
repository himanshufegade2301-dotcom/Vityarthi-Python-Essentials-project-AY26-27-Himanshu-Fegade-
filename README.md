# Hostel Management System

## Overview
A modular Python console application for managing common hostel operations. The project applies programming fundamentals, functions, modules, lists, dictionaries, searching, validation, conditional logic, loops, and basic reporting in a real-world context.

## Features
- Student registration, search, update and deletion
- Room allocation, room details and room vacation
- Fee recording and fee records
- Complaint registration and resolution
- Leave application, approval and rejection
- Hostel dashboard and individual student reports
- Input validation and basic error handling
- Built-in demo data for presentation

## Technologies
- Python 3.x
- Standard Python libraries only
- Git/GitHub for version control

## Project Structure
- `main.py` - application controller and menus
- `student.py` - student operations
- `room.py` - room allocation operations
- `fee.py` - fee operations
- `complain.py` - complaint operations
- `leave.py` - leave operations
- `reports.py` - dashboard and reports
- `demo_data.py` - demonstration records
- `utils.py` - reusable console utilities
- `statement.md` - project statement

## Installation and Run
1. Install Python 3.x.
2. Clone/download the repository.
3. Open a terminal in the project directory.
4. Run:
   `python main.py`

## Demonstration
The program loads demo records when it starts. This allows the complete workflow to be demonstrated immediately.

Suggested flow:
1. Open Dashboard
2. View Students
3. View Room Details
4. View Fee Records
5. View Complaints
6. Resolve a complaint
7. View Leaves
8. Approve/reject a leave
9. Generate a Student Report
10. Add a new student and allocate a room

## Testing
Test invalid student IDs, duplicate IDs, invalid phone numbers, invalid fee amounts, full rooms, duplicate room allocation, complaint resolution, leave approval/rejection, and empty-record scenarios.

## Limitations
The current version uses in-memory data structures. Records reset when the application closes. A future version can add SQLite/database persistence and role-based authentication.

## Academic Alignment
The project demonstrates modular programming, functions, data structures, control flow, validation, CRUD-like operations, searching, and reporting in a real-world application.
