import csv
from constants import CSV_FILE

def lookup_student():
    print("\n--- UC2: Lookup Student ---")
    search = input("Enter Roll No or Name: ").strip()
    found = False
    results = []

    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll_No"] == search: results = [row]; found = True; break
            elif search.lower() in row["Name"].lower(): results.append(row); found = True

    if found:
        print("\nSearch Results")
        for r in results: print(r)
    else: print("No student found.")
