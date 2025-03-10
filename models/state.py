#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """Instantiates a new State model"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        from models import storage
        related_cities = []

        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                related_cities.append(city)
        return related_cities
