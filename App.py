import csv
import os
CSV_FILE = "students.csv"
DELETED_FILE = "students_deleted.csv"
IMPORT_ERRORS_FILE = "import_errors.csv"
COLUMNS = [
    "Roll_No", "Name", "Branch", "Year", "Gender", "Age",
    "Attendance_%", "Mid1_Marks", "Mid2_Marks", "Quiz_Marks", "Final_Marks"
]
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(COLUMNS)
        print(f"{CSV_FILE} created with headers.")

def role_menu():
    print("\n Login as ")
    print("1. Office Clerk")
    print("2. Faculty ")
    print("3. HOD ")
    print("4. Exit")
    choice = input("Enter choice: ")
    return choice
def add_student():
    print("\n Add New Student ")

    while True:
        roll_no = input("Roll No: ")
        if roll_no.isdigit():
            roll_no = int(roll_no)
            break
        else:
            print("Roll No must be a number.")

    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["Roll_No"]) == roll_no:
                print(" Student with this Roll_No already exists!")
                return
            
    name = input("Name: ")
    branch = input("Branch: ")
    year = input("Year: ")
    gender = input("Gender: ")
        
    while True:
        age = input("Age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Age must be a number.")
    while True:
        attendance = input("Attendance %: ")
        try:
            attendance = float(attendance)
            if 0 <= attendance <= 100:
                break
            else:
                print("Attendance must be 0-100.")
        except:
            print("Enter a valid number.")

    marks = []
    for exam in ["Mid1", "Mid2", "Quiz", "Final"]:
        while True:
            mark = input(f"{exam} Marks: ")
            try:
                mark = float(mark)
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be 0-100.")
            except:
                print("Enter a valid number.")
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            roll_no, name, branch, year, gender, age,
            attendance, marks[0], marks[1], marks[2], marks[3]
        ])

    print(" Student added successfully!")    
   

def clerk_menu():
    while True:
        print("\n  Clerk Menu  ")
        print("1. Add New Student")
        print("2. Delete Student")
        print("3. Export Backup")
        print("0. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            print(" Add Student Function")
            add_student()
        elif choice == "2":
            print(" Delete Student Function")
        elif choice == "3":
            print(" Export Backup Function")
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

def teacher_menu():
    while True:
        print("\n  Teacher Menu ")
        print("1. Lookup Student")
        print("2. Update Marks/Attendance")
        print("3. Generate PTM Report")
        print("4. Sort or Filter Students")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            print(" Lookup Student Function")
        elif choice == "2":
            print(" Update Records Function")
        elif choice == "3":
            print(" Generate Report Function")
        elif choice == "4":
            print(" Sort/Filter Function")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

def hod_menu():
    while True:
        print("\n HOD Menu ")
        print("1. Generate Summary Reports")
        print("2. Bulk Import from CSV")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            print(" Summary Report Function")
        elif choice == "2":
            print(" Bulk Import Function")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    init_csv()

    while True:
        choice = role_menu()

        if choice == "1":
            clerk_menu()
        elif choice == "2":
            teacher_menu()
        elif choice == "3":
            hod_menu()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

       

