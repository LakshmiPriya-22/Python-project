import csv
from constants import CSV_FILE, COLUMNS

def add_student():
    print("\n--- UC1: Add New Student ---")
    while True:
        roll_no = input("Roll No: ").strip()
        if roll_no.isdigit(): roll_no = int(roll_no); break
        else: print("Roll No must be a number.")

    # Check duplicates
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["Roll_No"]) == roll_no:
                print("Student with this Roll_No already exists!"); return

    name = input("Name: ")
    branch = input("Branch: ")
    year = input("Year: ")
    gender = input("Gender: ")

    while True:
        age = input("Age: ").strip()
        if age.isdigit(): age = int(age); break
        else: print("Age must be a number.")

    while True:
        attendance = input("Attendance %: ").strip()
        try:
            attendance = float(attendance)
            if 0 <= attendance <= 100: break
            else: print("Attendance must be 0-100.")
        except: print("Enter valid number.")

    marks = []
    for exam in ["Mid1", "Mid2", "Quiz", "Final"]:
        while True:
            mark = input(f"{exam} Marks: ").strip()
            try:
                mark = float(mark)
                if 0 <= mark <= 100: marks.append(mark); break
                else: print("Marks must be 0-100.")
            except: print("Enter valid number.")

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll_no, name, branch, year, gender, age,
                         attendance, marks[0], marks[1], marks[2], marks[3]])
    print("Student added successfully!")
