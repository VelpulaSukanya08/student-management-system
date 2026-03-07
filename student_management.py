students = []

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully")

    elif choice == "2":
        print("Student List:")
        for s in students:
            print(s)

    elif choice == "3":
        name = input("Enter student name to delete: ")

        if name in students:
            students.remove(name)
            print("Student deleted successfully")
        else:
            print("Student not found")

    elif choice == "4":
        name = input("Enter student name to search: ")

        if name in students:
            print("Student found")
        else:
            print("Student not found")

    elif choice == "5":
        print("Program exited")
        break

    else:
        print("Invalid choice")