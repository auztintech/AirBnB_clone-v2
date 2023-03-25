#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Table, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Model Representing an Amenity in the database"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity, viewonly=False)
