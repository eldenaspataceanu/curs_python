from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
# import json

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(255))
    address = Column(VARCHAR(255))
    postcode = Column(VARCHAR(255))
    location = Column(VARCHAR(255))
    date_of_birth = Column(VARCHAR(255))
    professional_activities = Column(VARCHAR(255))
    telefone = Column(VARCHAR(255))
    constituency = Column(VARCHAR(255))
    political_party = Column(VARCHAR(255))
    email = Column(VARCHAR(255), unique=True)
    image_path = Column(VARCHAR(255))



# with open('output.json', 'r') as f:
#     data = json.load(f)
#
# print(data[0]['details']['Adresse'])
