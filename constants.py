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
        import csv
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(COLUMNS)
        print(f"{CSV_FILE} created with headers.")
