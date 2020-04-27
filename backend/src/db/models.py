import datetime
import enum

from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime, Boolean, desc, Enum, ForeignKey, asc, func, Float
from sqlalchemy.orm import relationship, backref
from common.server.flaskutils import print_flush
from common.db.tools import to_dict, serialize, serialize_foreign, serialize_foreign_recursive
from common.db.base import Base
from common.utils.security import verify_password, hash_password

from config.settings import SETTINGS


class Account(Base):
    __tablename__ = 'account'

    uniqid = Column(String(36), primary_key=True)
    password = Column(String(89), nullable=True)
    email = Column(String(120), nullable=True)
    name = Column(String(50), unique=True)
    created_at = Column(DateTime, unique=False, default=datetime.datetime.utcnow)

    def __init__(self, name):
        self.uniqid = str(uuid4())
        self.name = name
        self.password = None
        self.email = None
        self.created_at = datetime.datetime.utcnow()

    def set_password(self, password):
        self.password = hash_password(password)

    def check_password(self, password):
        return verify_password(self.password, password)

    def get_data(self):
        return {'uniqid': self.uniqid,
                'name': self.name,
                'permission': self.permission,
                'email': self.email}

    def __repr__(self):
        return '<Account %r (%s)>' % (self.name, self.uniqid)
