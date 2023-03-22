#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from .base_model import BaseModel, Base


class User(BaseModel, Base):
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

