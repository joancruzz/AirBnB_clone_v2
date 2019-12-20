#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import Base, BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities: relationship to cities table
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if type(models.storage) is models.engine.DBStorage:
        cities = relationship(
            'City', backref='state', cascade='all, delete-orphan'
        )
    else:
        @property
        def cities(self):
            """Get a list of cities associated with this state
            Return:
                returns a list of all City instances with a state_id matching
                the id of the current State
            """
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
