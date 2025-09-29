import csv
from constants import CSV_FILE

def generate_ptm_report(branch=None, year=None):
    students=[]
    with open(CSV_FILE,"r") as f:
        reader=csv.DictReader(f)
        for row in reader:
            if (branch is None or row["Branch"]==branch) and (year is None or row["Year"]==year):
                students.append(row)
    if not students: print("No students found"); return

    total=len(students)
    final=[float(s["Final_Marks"]) for s in students]
    avg=sum(final)/total
    high=max(final); low=min(final)

    grades={"A":0,"B":0,"C":0,"D":0}
    for m in final:
        if m>=90: grades["A"]+=1
        elif m>=75: grades["B"]+=1
        elif m>=50: grades["C"]+=1
        else: grades["D"]+=1

    print(f"\nPTM Report ({branch}-{year})")
    print(f"Total: {total}, Avg: {avg:.2f}, High: {high}, Low: {low}")
    print("Grades:",grades)
