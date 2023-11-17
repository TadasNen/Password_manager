import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from password_generator import password_generation

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

def create_sql_entry():
    while True:
        input_website = input("Website password is associated with: ")
        input_username = input("Username used: ")
        password_query = input("Do you want to generate new password? [Y/N]: ")
        if password_query.lower() == "n":
            input_password = input("Please state your associated password: ")
            session.add(Password_Manager(input_website, input_username, input_password))
            session.commit()
            break
        elif password_query.lower() == "y":
            input_password = password_generation()
            session.add(Password_Manager(input_website, input_username, input_password))
            session.commit()
            break
        else:
            print("\nPlease select correct value - Y or N\n")

def view_sql():
    view_data = session.query(Password_Manager).all()
    for el in view_data:
        print(f"{el.id}. Association: {el.website}; Login details: {el.username}; Password: {el.enc_password}")