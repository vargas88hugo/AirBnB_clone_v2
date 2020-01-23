#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)

    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """public getter method cities to return the list
            of City objects from storage linked to the current
            State"""
            from models import storage
            from models import City
            return [i for j, i in storage.all(City).items()
                    if i.state_id == self.id]
