import csv
from constants import CSV_FILE

def sort_students(by="Final_Marks", descending=True):
    with open(CSV_FILE,"r") as f:
        students=list(csv.DictReader(f))
    students.sort(key=lambda x: float(x.get(by,0)), reverse=descending)
    for s in students: print(s)

def filter_students(attendance_threshold=75):
    with open(CSV_FILE,"r") as f:
        students=[r for r in csv.DictReader(f) if float(r.get("Attendance_%",0))<attendance_threshold]
    for s in students: print(s)
