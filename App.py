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

def delete_student():
    print("\n  Delete Student ")
    roll = input("Enter Roll No of student to delete: ").strip()

    found = False
    rows = []
    deleted_row = None

    
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll_No"] == roll:
                print(f" Found Student: {row['Name']} (Roll {row['Roll_No']})")
                confirm = input("Are you sure you want to delete this student? (Y/N): ")
                if confirm.lower() == "y":
                    deleted_row = row
                    found = True
                    continue  
            rows.append(row)

    if found:

        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writeheader()
            writer.writerows(rows)


        if deleted_row:
            file_exists = os.path.exists(DELETED_FILE)
            with open(DELETED_FILE, "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=COLUMNS)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(deleted_row)

        print(" Student deleted and moved to students_deleted.csv")
    else:
        print(" Student not found or deletion cancelled.")

def update_student():
    print("\n Update Student Records ")
    roll = input("Enter Roll No of student to update: ").strip()

    updated = False
    rows = []

    
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll_No"] == roll:
                print(f" Found Student: {row['Name']} (Roll {row['Roll_No']})")
                print("Current Attendance:", row["Attendance_%"])
                print("Current Marks:", row["Mid1_Marks"], row["Mid2_Marks"], row["Quiz_Marks"], row["Final_Marks"])

                print("\nWhat do you want to update?")
                print("1. Attendance")
                print("2. Marks")
                choice = input("Enter choice: ")

                if choice == "1":
                    new_att = input("Enter new Attendance %: ")
                    try:
                        new_att = float(new_att)
                        if 0 <= new_att <= 100:
                            print(f"Old Attendance: {row['Attendance_%']} → New: {new_att}")
                            row["Attendance_%"] = str(new_att)
                            updated = True
                        else:
                            print(" Attendance must be between 0-100.")
                    except:
                        print(" Invalid number.")

                elif choice == "2":
                    for exam in ["Mid1_Marks", "Mid2_Marks", "Quiz_Marks", "Final_Marks"]:
                        new_mark = input(f"Enter new {exam} (leave blank to keep {row[exam]}): ")
                        if new_mark.strip() != "":
                            try:
                                new_mark = float(new_mark)
                                if 0 <= new_mark <= 100:
                                    print(f"Old {exam}: {row[exam]} → New: {new_mark}")
                                    row[exam] = str(new_mark)
                                    updated = True
                                else:
                                    print(" Marks must be 0-100.")
                            except:
                                print(" Invalid number.")
                else:
                    print(" Invalid choice!")

            rows.append(row)

    
    if updated:
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writeheader()
            writer.writerows(rows)
        print(" Record updated successfully!")
    else:
        print(" No updates made (student not found or invalid input).")


def lookup_student():
    print("\n Lookup Student ")
    search = input("Enter Roll No or Name: ").strip()

    found = False
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        results = []
        for row in reader:
            
            if row["Roll_No"] == search:
                results = [row]
                found = True
                break
            elif search.lower() in row["Name"].lower():
                results.append(row)
                found = True

    if found:
        print("\n Search Results ")
        for r in results:
            print(r)
    else:
        print(" No student found with that Roll No or Name.")


def clerk_menu():
    while True:
        print("\n  Clerk Menu  ")
        print("1. Add New Student")
        print("2. Delete Student")
        print("3. Export Backup")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == "1":
            print(" Add Student Function")
            add_student()
        elif choice == "2":
            print(" Delete Student Function")
            delete_student()
        elif choice == "3":
            print(" Export Backup Function")
        elif choice == "4":
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
            lookup_student()
        elif choice == "2":
            print(" Update Records Function")
            update_student()  
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

       

