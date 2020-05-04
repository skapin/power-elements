import datetime

from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from common.db.base import Base
from common.utils.security import verify_password, hash_password


class Account(Base):
    __tablename__ = 'account'

    uniqid = Column(String(36), primary_key=True)
    password = Column(String(89), nullable=True)
    name = Column(String(50), unique=True)
    created_at = Column(DateTime,
                        unique=False,
                        default=datetime.datetime.utcnow)

    def __init__(self, name, password):
        self.uniqid = str(uuid4())
        self.name = name
        self.password = password
        self.created_at = datetime.datetime.utcnow()

    def set_password(self, password):
        self.password = hash_password(password)

    def check_password(self, password):
        return verify_password(self.password, password)

    def get_data(self):
        return {'uniqid': self.uniqid,
                'name': self.name}

    def __repr__(self):
        return '<Account %r (%s)>' % (self.name, self.uniqid)


class Question(Base):
    __tablename__ = 'question'

    uniqid = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, unique=False, default=datetime.datetime.utcnow)

    def __init__(self, name):
        self.uniqid = str(uuid4())
        self.name = name
        self.created_at = datetime.datetime.utcnow()

    def get_data(self):
        return {'uniqid': self.uniqid,
                'name': self.name}

    def __repr__(self):
        return '<Question %r (%s)>' % (self.name, self.uniqid)


class Response(Base):
    __tablename__ = 'response'

    uniqid = Column(String(36), primary_key=True)
    value = Column(Integer)
    created_at = Column(DateTime,
                        unique=False,
                        default=datetime.datetime.utcnow)

    question_id = Column(String(36),
                         ForeignKey('question.uniqid', onupdate="CASCADE"))
    question = relationship('Question',
                            backref=backref('responses', lazy='dynamic'))

    account_id = Column(String(36),
                        ForeignKey('account.uniqid', onupdate="CASCADE"))
    account = relationship('Account',
                           backref=backref('responses', lazy='dynamic'))

    def __init__(self, value, question_obj, account_obj):
        self.uniqid = str(uuid4())
        self.value = value
        self.question = question_obj
        self.account = account_obj
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        return '<Response %r (%r) (%s)>' % (self.value, self.created_at, self.uniqid)
