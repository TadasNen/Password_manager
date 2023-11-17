import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
session = Session

