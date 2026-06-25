from database import *

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        id = int(input("ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        dept = input("Department: ")
        add_student(id, name, age, dept)
        print("Student added!")

    elif choice == "2":
        view_students()

    elif choice == "3":
        id = int(input("Enter ID: "))
        student = search_student(id)
        print(student)

    elif choice == "4":
        id = int(input("ID: "))
        name = input("New Name: ")
        update_student(id, name)
        print("Updated!")

    elif choice == "5":
        id = int(input("ID: "))
        delete_student(id)
        print("Deleted!")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")