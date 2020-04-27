import datetime
import enum

from common.utils.numerical import uniqid
from common.utils.security import hash_password, verify_password
from server.extensions import db


def cln_str(s):
    if s:
        return s.replace(
            "'",
            "").replace(
            '\\',
            '').replace(
            '%',
            '').replace(
                ';',
            '')
    return ''


class NumiiState(enum.Enum):
    BROKEN = "Broken"
    REPAIR = "On repair"
    SERVICE = "Working"


class TagType(enum.Enum):
    WARNING = "warning"
    HEAVY = "heavy"
    STOP = "stop"
    GA = "ga"
    GB = "gb"
    GC = "gc"
    PA = "pa"
    PB = "pb"
    PC = "pc"
    AP = "ap"
    REGRASP = "regrasp"
    BA = "ba"
    E = "e"
    F = "f"
    STEP = "step"
    CRANK = "crank"


class SessionGroup(db.Model):
    uniqid = db.Column(db.String(36), primary_key=True)
    group_id = db.Column(db.String(50), unique=False)
    group_index = db.Column(db.Integer, nullable=True, default=None)

    session_id = db.Column(db.String(36), db.ForeignKey('session.uniqid'))
    session = db.relationship('Session',
        backref=db.backref('session_groups', lazy='dynamic'))

    def __init__(self, session_id, group_index=0, group_id=None):
        self.uniqid = uniqid()
        self.session_id = session_id
        if not group_id:
            self.group_id = uniqid()
        else:
            self.group_id = group_id
        self.group_index = group_index


class Customer(db.Model):
    uniqid = db.Column(db.String(36), primary_key=True)
    password = db.Column(db.String(89), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, unique=False)

    def __init__(self, name):
        self.uniqid = uniqid()
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
                'email': self.email}

    def __repr__(self):
        return '<Customer %r (%s)>' % (self.name, self.uniqid)


class Numii(db.Model):
    uniqid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, unique=False)
    updated = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())
    state = db.Column(db.Enum(NumiiState))
    version = db.Column(db.String(50))
    branch = db.Column(db.String(50))
    commentary = db.Column(db.String(50))

    customer_id = db.Column(db.String(36), db.ForeignKey('customer.uniqid'))
    customer = db.relationship('Customer', backref=db.backref('numiis', lazy='dynamic'))

    def __init__(self, name, customer_obj):
        self.uniqid = uniqid()
        self.name = name
        self.created_at = datetime.datetime.utcnow()
        self.customer = customer_obj


class Plant(db.Model):

    uniqid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, unique=False)
    latitude = db.Column(db.Float, unique=False)
    longitude = db.Column(db.Float, unique=False)
    enabled = db.Column(db.Boolean, unique=False)

    customer_id = db.Column(db.String(36), db.ForeignKey('customer.uniqid'))
    customer = db.relationship('Customer',
                                backref=db.backref('plants',
                                                   lazy='dynamic'))

    __table_args__ = (db.UniqueConstraint('name', 'customer_id', name='uix_plant_name_customer_id'),)

    def __init__(self, name, latitude, longitude, customer_obj, enabled=True):
        self.uniqid = uniqid()
        self.name = name
        self.created_at = datetime.datetime.utcnow()
        self.latitude = latitude
        self.longitude = longitude
        self.enabled = enabled
        self.customer = customer_obj


class Line(db.Model):

    uniqid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50), unique=False)
    created_at = db.Column(db.DateTime, unique=False)
    enabled = db.Column(db.Boolean, unique=False)
    reference = db.Column(db.String(50), nullable=True, unique=False)

    plant_id = db.Column(db.String(36), db.ForeignKey('plant.uniqid', onupdate="CASCADE"))
    plant = db.relationship('Plant',
                            backref=db.backref('lines',
                                               lazy='dynamic'))
    __table_args__ = (db.UniqueConstraint('name', 'plant_id', name='uix_line_name_plant_id'),)

    def __init__(self, name, plant_obj, reference=None, enabled=True):
        self.uniqid = uniqid()
        self.name = name
        self.created_at = datetime.datetime.utcnow()
        self.enabled = enabled
        self.reference = reference
        self.plant = plant_obj


class Operator(db.Model):
    uniqid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50), unique=False)
    enable = db.Column(db.String(50), unique=True)

    def __init__(self, name, line_obj):
        self.uniqid = uniqid()


class Workstation(db.Model):

    uniqid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(50), unique=False)
    created_at = db.Column(db.DateTime, unique=False)
    enabled = db.Column(db.Boolean, unique=False)

    latitude = db.Column(db.Float, unique=False)
    longitude = db.Column(db.Float, unique=False)

    moy_last_month = db.Column(db.Integer, nullable=True, default=0)
    evolution_3_month = db.Column(db.Integer, unique=False)
    evolution_6_month = db.Column(db.Integer, unique=False)

    evolution_3_month_pts = db.Column(db.Integer, unique=False)
    evolution_6_month_pts = db.Column(db.Integer, unique=False)

    line_id = db.Column(db.String(36), db.ForeignKey('line.uniqid', onupdate="CASCADE"))
    line = db.relationship('Line',
                           backref=db.backref('workstations',
                                              lazy='dynamic'))
    __table_args__ = (db.UniqueConstraint('name', 'line_id', name='uix_workstation_name_line_id'),)

    def __init__(self, name, line_obj, enabled=True):
        self.uniqid = uniqid()
        self.name = name
        self.created_at = datetime.datetime.utcnow()
        self.enabled = enabled
        self.line = line_obj


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(36), unique=True)
#     hash = db.Column(db.String(124), unique=True)

#     def set_password(self, password):
#         self.hash = hash_password(password)

#     def check_password(self, password):
#         return verify_password(self.hash, password)

#     def __init__(self, name, password='kombos'):
#         self.name = name
#         self.set_password(password)

#     def __repr__(self):
#         return '<User %r (%d)>' % (self.name, self.id)

class Person(db.Model):

    uniqid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(36), unique=False)
    hash = db.Column(db.String(124), unique=False)
    created_at = db.Column(db.DateTime, unique=False)

    customer_id = db.Column(db.String(36), db.ForeignKey('customer.uniqid'))
    customer = db.relationship('Customer',
                           backref=db.backref('persons',
                                              lazy='dynamic'))
    __table_args__ = (db.UniqueConstraint('name', 'customer_id', name='uix_person_name_customer_id'),)

    def set_password(self, password):
        self.hash = hash_password(password)

    def check_password(self, password):
        return verify_password(self.hash, password)

    def __init__(self, name, password='kombos'):
        self.uniqid = uniqid()
        self.name = name
        self.set_password(password)
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        return '<Person %r (%s)>' % (self.name, self.uniqid)


class Tag(db.Model):

    uniqid = db.Column(db.String(36), primary_key=True)
    mtm = db.Column(db.Boolean)
    type = db.Column(db.Enum(TagType))
    at = db.Column(db.DateTime)
    by = db.Column(db.String(36))
    comment = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, unique=False)

    session_id = db.Column(db.String(36), db.ForeignKey('session.uniqid'))
    session = db.relationship('Session',
                              backref=db.backref('tags',
                                                 lazy='dynamic'))

    def __init__(self, type, by, comment, session_obj, mtm):
        self.uniqid = uniqid()
        self.type = type
        self.by = by
        self.at = datetime.datetime.utcnow() - datetime.timedelta(seconds=1)
        self.created_at = datetime.datetime.utcnow()
        self.comment = comment
        self.session = session_obj
        self.mtm = mtm

    def __repr__(self):
        return '<Tag %r (%r) (%r) (%r) (%r) (%r)>' % (
            self.type, self.by, self.at, self.session.uniqid, self.mtm, self.comment)

class PGTimestampedImage(db.Model):

    uniqid = db.Column(db.String(36), primary_key=True)
    created_at = db.Column(db.DateTime)
    timestamp = db.Column(db.BigInteger)
    session_id = db.Column(db.String(36), db.ForeignKey('session.uniqid'))
    data = db.Column(db.LargeBinary)

    def __init__(self, session, time, img_data):
        self.uniqid = uniqid()
        self.created_at = datetime.datetime.utcnow()
        self.timestamp = time
        self.session_id = session
        self.data = img_data


class Session(db.Model):

    uniqid = db.Column(db.String(36), primary_key=True)
    billed = db.Column(db.Boolean, unique=False, default=False)

    start_at = db.Column(db.DateTime)
    end_at = db.Column(db.DateTime, nullable=True, default=None)

    observator_id = db.Column(db.String(36), db.ForeignKey('person.uniqid'))
    observator = db.relationship('Person',
                                 foreign_keys=[observator_id],
                                 backref=db.backref('observator_sessions',
                                                    lazy='dynamic'))

    worker_id = db.Column(db.String(36), db.ForeignKey('person.uniqid'))
    worker = db.relationship('Person',
                             foreign_keys=[worker_id],
                             backref=db.backref('worker_sessions',
                                                lazy='dynamic'))

    workstation_id = db.Column(
        db.String(36),
        db.ForeignKey('workstation.uniqid'))
    workstation = db.relationship('Workstation',
                                  backref=db.backref('sessions',
                                                     lazy='dynamic'))

    indice = db.Column(db.Integer, nullable=True, default=None)
    score_joint = db.Column(db.String(3000))
    distance = db.Column(db.Float, nullable=True, default=None)
    latitude = db.Column(db.Float, nullable=True, default=None)
    longitude = db.Column(db.Float, nullable=True, default=None)
    noise = db.Column(db.Integer, nullable=True, default=None)
    counter = db.Column(db.String(3000))
    tag = db.Column(db.String(60))
    transform = db.Column(db.String(3000))

    size = db.Column(db.Float, nullable=True, default=None)
    weight = db.Column(db.Integer, nullable=True, default=None)
    gender = db.Column(db.String(36), nullable=True, default=None)
    age = db.Column(db.Integer, nullable=True, default=None)
    emotion = db.Column(db.String(36), nullable=True, default=None)

    threat = db.Column(db.String(3000))
    created_at = db.Column(db.DateTime, unique=False)
    extrapolated_date = db.Column(db.DateTime, unique=False)

    reference = db.Column(db.Boolean, default=False)

    tagged = db.Column(db.Boolean, unique=False, default=False)
    tagged_by_person = db.Column(db.String(36), db.ForeignKey('person.uniqid'))
    tagged_by = db.relationship('Person',
                                foreign_keys=[tagged_by_person],
                                backref=db.backref('taggedBy_sessions',
                                                   lazy='dynamic'))
    sensors = db.Column(db.String(1024))

    def __init__(self, uniqid, observator, worker, workstation, session_sensors, group=None, start_at=None):
        if not start_at:
            self.start_at = datetime.datetime.utcnow()
        else:
            self.start_at = start_at
        if not uniqid:
            self.uniqid = uniqid()
        self.uniqid = uniqid
        self.observator = observator
        self.worker = worker
        self.workstation = workstation
        self.created_at = datetime.datetime.utcnow()
        self.group = group
        self.sensors = session_sensors
    # def __repr__(self):
        # return '<Session %r (%d)>' % (self.uniqid, self.id)

    def __repr__(self):
        return '<Session %r (%s) at (%s)>' % (
            self.uniqid, self.worker, self.start_at)
