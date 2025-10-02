from add_students import add_student
from lookup_students import lookup_student
from update_students import update_student
from delete_students import delete_student
from ptm_report import generate_ptm_report
from bulk_imports import bulk_import
from sort_filter import sort_students, filter_students

def role_menu():
    print("\nLogin as:\n1. Clerk\n2. Teacher\n3. HOD\n4. Exit")
    return input("Choice: ")

def clerk_menu():
    while True:
        print("\n1.Add Student\n2.Delete Student\n3.Export Backup\n4.Back")
        choice=input("Choice: ")
        if choice=="1": add_student()
        elif choice=="2": delete_student()
        elif choice=="3": print("Backup exported!")
        elif choice=="4": break

def teacher_menu():
    while True:
        print("\n1.Lookup Student\n2.Update Records\n3.PTM Report\n4.Sort/Filter\n5.Back")
        choice=input("Choice: ")
        if choice=="1": lookup_student()
        elif choice=="2": update_student()
        elif choice=="3": generate_ptm_report()
        elif choice=="4":
            print("1.Sort\n2.Filter"); ch=input("Choice: ")
            if ch=="1": sort_students()
            elif ch=="2": filter_students()
        elif choice=="5": break

def hod_menu():
    while True:
        print("\n1.Summary Reports\n2.Bulk Import CSV\n3.Back")
        choice=input("Choice: ")
        if choice=="1": generate_ptm_report()
        elif choice=="2": bulk_import(input("CSV path: "))
        elif choice=="3": break
