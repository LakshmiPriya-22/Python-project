import csv
from constants import CSV_FILE, COLUMNS

def update_student():
    print("\n--- UC3: Update Student Records ---")
    roll = input("Enter Roll No: ").strip()
    updated = False
    rows = []

    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll_No"] == roll:
                print(f"Found Student: {row['Name']} (Roll {row['Roll_No']})")
                print("Attendance:", row["Attendance_%"])
                print("Marks:", row["Mid1_Marks"], row["Mid2_Marks"], row["Quiz_Marks"], row["Final_Marks"])
                print("1. Update Attendance\n2. Update Marks")
                choice = input("Choice: ").strip()
                if choice=="1":
                    new_att = input("New Attendance %: ").strip()
                    try:
                        new_att = float(new_att)
                        if 0<=new_att<=100: row["Attendance_%"]=str(new_att); updated=True
                        else: print("Attendance 0-100.")
                    except: print("Invalid number.")
                elif choice=="2":
                    for exam in ["Mid1_Marks","Mid2_Marks","Quiz_Marks","Final_Marks"]:
                        new_mark = input(f"{exam} (blank to keep {row[exam]}): ").strip()
                        if new_mark!="":
                            try:
                                new_mark=float(new_mark)
                                if 0<=new_mark<=100: row[exam]=str(new_mark); updated=True
                                else: print("Marks 0-100.")
                            except: print("Invalid number.")
            rows.append(row)

    if updated:
        with open(CSV_FILE,"w",newline="") as f:
            writer = csv.DictWriter(f,fieldnames=COLUMNS)
            writer.writeheader()
            writer.writerows(rows)
        print("Record updated!")
    else: print("No updates made.")
