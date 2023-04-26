#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    __tablename__ = 'places'

    city_id = Column(String(60, collation='latin1_swedish_ci'), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", cascade="all, delete", backref="place")

    place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60, collation='latin1_swedish_ci'), ForeignKey('amenities.id'), primary_key=True, nullable=False)
    )

    @property
    def reviews(self):
        from models import storage
        review_list = []
        for review in storage.all('Review').values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
    
    @property
    def amenities(self):
        """
        Getter attribute that returns the list of Amenity instances based on the attribute amenity_ids that contains
        all Amenity.id linked to the Place
        """
        from models import storage
        amenities = storage.all('Amenity').values()
        return [amenity for amenity in amenities if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, obj):
        """
        Setter attribute that handles append method for adding an Amenity.id to the attribute amenity_ids.
        This method should accept only Amenity object, otherwise, do nothing
        """
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
