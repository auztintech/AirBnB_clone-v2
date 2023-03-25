#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

storage_type = os.getenv("HBNB_TYPE_STORAGE")
if storage_type == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
