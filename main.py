from sql_database import *

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to password manager app")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

while True:
    menu_options = input("Please select what would you like to do:\n"
                         "1. Generate new password\n"
                         "2. Create entry to local database\n"
                         "3. View database entries\n"
                         "4. Delete entries\n"
                         "5. Search by category\n"
                         "q - Quit\n"
                         "Please select your option: ")
    if menu_options.lower() == 'q':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("\nProgram closed, see you next time!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    elif menu_options == '1':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print(password_generation())
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    elif menu_options == '2':
        create_sql_entry()
    elif menu_options == '3':
        view_sql()
    elif menu_options == '4':
        delete_sql_entry()
    elif menu_options == '5':
        filter_sql()
    else:
        print("Selected option is not valid, "
              "please try again using 1-5 digits or 'q' to quit")