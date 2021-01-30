from peewee import *
import os, sys
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append('/Users/AdnanAhmad/Data/Development/PetProjects/LearningFastAPI/ContactAPI/')
from database import conn

class BaseModel(Model):
    class Meta:
        database = conn