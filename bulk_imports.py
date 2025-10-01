import csv
from constants import CSV_FILE, IMPORT_ERRORS_FILE, COLUMNS

def bulk_import(file_path):
    valid=[]; invalid=[]; existing=set()
    with open(CSV_FILE,"r") as f:
        reader=csv.DictReader(f)
        for r in reader: existing.add(r["Roll_No"])

    with open(file_path,"r") as f:
        reader=csv.DictReader(f)
        for idx,row in enumerate(reader,start=2):
            try:
                if row["Roll_No"] in existing: raise ValueError("Duplicate Roll_No")
                row["Attendance_%"]=float(row["Attendance_%"])
                for col in ["Mid1_Marks","Mid2_Marks","Quiz_Marks","Final_Marks"]:
                    row[col]=float(row[col])
                valid.append(row)
            except Exception as e:
                row["Error"]=str(e); row["Line"]=idx
                invalid.append(row)

    with open(CSV_FILE,"a",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=COLUMNS)
        writer.writerows(valid)

    if invalid:
        with open(IMPORT_ERRORS_FILE,"w",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=list(COLUMNS)+["Line","Error"])
            writer.writeheader()
            writer.writerows(invalid)

    print(f"Imported {len(valid)} rows, {len(invalid)} errors.")
