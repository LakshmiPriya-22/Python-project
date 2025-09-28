import csv, os
from constants import CSV_FILE, DELETED_FILE, COLUMNS

def delete_student():
    print("\n--- UC4: Delete Student ---")
    roll = input("Enter Roll No: ").strip()
    found=False; rows=[]; deleted_row=None

    with open(CSV_FILE,"r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll_No"]==roll:
                print(f"Found {row['Name']} (Roll {row['Roll_No']})")
                confirm=input("Delete? (Y/N): ").strip().lower()
                if confirm=="y": deleted_row=row; found=True; continue
            rows.append(row)

    if found:
        with open(CSV_FILE,"w",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=COLUMNS)
            writer.writeheader()
            writer.writerows(rows)
        if deleted_row:
            file_exists=os.path.exists(DELETED_FILE)
            with open(DELETED_FILE,"a",newline="") as f:
                writer=csv.DictWriter(f,fieldnames=COLUMNS)
                if not file_exists: writer.writeheader()
                writer.writerow(deleted_row)
        print("Student deleted and moved to students_deleted.csv")
    else: print("Student not found or cancelled.")
