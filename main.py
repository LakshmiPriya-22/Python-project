from constants import init_csv
from users import role_menu, clerk_menu, teacher_menu, hod_menu

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
