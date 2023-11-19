from sql_database import *

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to password manager app")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

generate_key()

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
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Program closed, see you next time!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break
    elif menu_options == '1':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\nYour new password is {password_generation()}\n")
    elif menu_options == '2':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        create_sql_entry()
        print("\nNew entry successfully created\n")
    elif menu_options == '3':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Information in current database:")
        view_sql()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif menu_options == '4':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        delete_sql_entry()
        print("Entry successfully deleted")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif menu_options == '5':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        filter_sql()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("Selected option is not valid, "
              "please try again using 1-5 digits or 'q' to quit")
