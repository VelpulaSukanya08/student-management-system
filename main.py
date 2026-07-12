import json
import os
import csv

FILE_NAME = "students.json"

# -------------------- Load Students --------------------
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# -------------------- Save Students --------------------
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# -------------------- Grade --------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

students = load_students()

# -------------------- Add Student --------------------
def add_student():

    print("\n========== ADD STUDENT ==========")

    # Auto Generate Roll Number
    if len(students) == 0:
        roll = "1"
    else:
        last_roll = int(students[-1]["roll"])
        roll = str(last_roll + 1)

    print("Generated Roll Number :", roll)

    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    course = input("Enter Course : ")
    marks = float(input("Enter Marks : "))

    grade = calculate_grade(marks)

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    save_students(students)

    print("Student Added Successfully!")

# -------------------- View Students --------------------
def view_students():

    print("\n========== STUDENT LIST ==========")

    if len(students) == 0:
        print("No Students Found!")
        return

    for student in students:
        print("-" * 40)
        print("Roll Number :", student["roll"])
        print("Name        :", student["name"])
        print("Age         :", student["age"])
        print("Course      :", student["course"])
        print("Marks       :", student["marks"])
        print("Grade       :", student["grade"])

# -------------------- Search Student --------------------
def search_student():

    roll = input("\nEnter Roll Number : ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found")
            print("---------------------------")
            print("Roll Number :", student["roll"])
            print("Name        :", student["name"])
            print("Age         :", student["age"])
            print("Course      :", student["course"])
            print("Marks       :", student["marks"])
            print("Grade       :", student["grade"])
            return

    print("Student Not Found!")
# -------------------- Update Student --------------------
def update_student():

    roll = input("\nEnter Roll Number to Update : ")

    for student in students:

        if student["roll"] == roll:

            print("\nLeave blank if you don't want to change a field.")

            name = input(f"Name ({student['name']}) : ")
            age = input(f"Age ({student['age']}) : ")
            course = input(f"Course ({student['course']}) : ")
            marks = input(f"Marks ({student['marks']}) : ")

            if name:
                student["name"] = name

            if age:
                student["age"] = int(age)

            if course:
                student["course"] = course

            if marks:
                student["marks"] = float(marks)
                student["grade"] = calculate_grade(float(marks))

            save_students(students)

            print("✅ Student Updated Successfully!")
            return

    print("❌ Student Not Found!")
    # -------------------- Delete Student --------------------
def delete_student():

    roll = input("\nEnter Roll Number to Delete : ")

    for student in students:

        if student["roll"] == roll:

            students.remove(student)
            save_students(students)

            print("✅ Student Deleted Successfully!")
            return

    print("❌ Student Not Found!")
    # -------------------- Statistics --------------------
def show_statistics():

    if len(students) == 0:
        print("\nNo Students Available!")
        return

    total = len(students)
    highest = max(students, key=lambda x: x["marks"])
    lowest = min(students, key=lambda x: x["marks"])

    average = sum(student["marks"] for student in students) / total

    print("\n========== STUDENT STATISTICS ==========")
    print("Total Students :", total)
    print("Average Marks  :", round(average, 2))
    print("Highest Marks  :", highest["marks"], "-", highest["name"])
    print("Lowest Marks   :", lowest["marks"], "-", lowest["name"])
    # -------------------- Sort Students --------------------
def sort_students():

    if len(students) == 0:
        print("\nNo Students Available!")
        return

    sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)

    print("\n========== STUDENT RANK LIST ==========")

    rank = 1

    for student in sorted_students:

        print("-" * 40)
        print("Rank        :", rank)
        print("Roll Number :", student["roll"])
        print("Name        :", student["name"])
        print("Course      :", student["course"])
        print("Marks       :", student["marks"])
        print("Grade       :", student["grade"])

        rank += 1
# -------------------- Export to CSV --------------------
def export_to_csv():

    if len(students) == 0:
        print("\nNo Students Available!")
        return

    with open("students.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Roll Number", "Name", "Age", "Course", "Marks", "Grade"])

        for student in students:

            writer.writerow([
                student["roll"],
                student["name"],
                student["age"],
                student["course"],
                student["marks"],
                student["grade"]
            ])

    print("\nStudents exported successfully to students.csv")        

# -------------------- Main Menu --------------------
while True:

    print("\n")
    print("=" * 45)
    print("   STUDENT MANAGEMENT SYSTEM PRO")
    print("=" * 45)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Statistics")
    print("7. Sort Students")
    print("8. Export to CSV")
    print("9. Exit")

    choice = input("Enter Your Choice : ")

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
        show_statistics()
    elif choice == "7":
        sort_students()
    elif choice == "8":
        export_to_csv()
    elif choice == "9":
        print("Thank You!")      
        break    

    else:
        print("Invalid Choice!")