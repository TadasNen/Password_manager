import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from password_generator import password_generation
from encyption import *

from sqlalchemy.util import deprecations

deprecations.SILENCE_UBER_WARNING = True

engine = create_engine("sqlite:///password_manager.db")
Base = declarative_base()


class Password_Manager(Base):
    __tablename__ = "Saved passwords"
    id = Column(Integer, primary_key=True)
    website = Column(String)
    username = Column(String)
    enc_password = Column(String)
    input_date = Column(DateTime, default=datetime.date.today())

    def __init__(self, website, username, enc_password):
        self.website = website
        self.username = username
        self.enc_password = enc_password


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def create_sql_entry() -> None:
    """
    Function takes user input of data that is to be added to sql database and creates new entrt
    :return: None. Creates new entry in sql database
    """
    while True:
        input_website = input("Website password is associated with: ")
        input_username = input("Username used: ")
        password_query = input("Do you want to generate new password? [Y/N]: ")
        if password_query.lower() == "n":
            input_password = input("Please state your associated password: ")
            encrypted_password = fernet_encryption(input_password)
            session.add(Password_Manager(input_website, input_username, encrypted_password))
            session.commit()
            break
        elif password_query.lower() == "y":
            input_password = password_generation()
            encrypted_password = fernet_encryption(input_password)
            session.add(Password_Manager(input_website, input_username, encrypted_password))
            session.commit()
            break
        else:
            print("\nPlease select correct value - Y or N\n")


def view_sql() -> None:
    """
    Function prints out all entries containing sql database except for entry creation date
    :return: None. Function prints out results
    """
    view_data = session.query(Password_Manager).all()
    for el in view_data:
        decrypted_password = fernet_decryption(el.enc_password)
        print(f"{el.id}. Association: {el.website}; Login details: {el.username}; Password: {decrypted_password}")


def delete_sql_entry() -> None:
    """
    Function deletes selected entry in sql database based on users input of ID
    :return: None. Function deletes entry in sql database
    """
    while True:
        try:
            entry_id = int(input("Select password ID corresponding to which entry should be deleted: "))
            delete_entry_id = session.query(Password_Manager).get(entry_id)
            if delete_entry_id:
                session.delete(delete_entry_id)
                session.commit()
                break
            else:
                print("\nEntry ID does not exist\n")
        except ValueError:
            print("\nID must be a digit\n")


def filter_sql() -> None:
    """
    Looped menu of functions described above. Based on user entry, function calls other functions
    :return: None
    """
    while True:
        option_filter = input("Please select according to which column you want to filter:\n"
                              "1. Entry ID\n"
                              "2. Associated website\n"
                              "3. Login details\n"
                              "q - quit\n"
                              "Your option: ")
        if option_filter == "1":
            collumn_filter = Password_Manager.id
        elif option_filter == "2":
            collumn_filter = Password_Manager.website
        elif option_filter == "3":
            collumn_filter = Password_Manager.username
        elif option_filter == "q":
            break
        else:
            print("\nPlease select valid option\n")
        if option_filter == "1" or option_filter == "2" or option_filter == "3":
            input_filter = input("Search for: ")
            filter_entry = session.query(Password_Manager).filter(collumn_filter.ilike(f"%{input_filter}%")).all()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Your search results: ")
            for el in filter_entry:
                decrypted_password = fernet_decryption(el.enc_password)
                print(f"{el.id}. "
                      f"Association: {el.website}; "
                      f"Login details: {el.username}; "
                      f"Password {decrypted_password}")
            break
