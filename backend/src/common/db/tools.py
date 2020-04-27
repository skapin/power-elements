import datetime
import enum


def to_dict(obj, ignore=None):
    if not ignore:
        ignore = []
    collection = {}
    for c in obj.__table__.columns:
        value = getattr(obj, c.name)
        if c.name not in ignore:
            collection.update({c.name: value})
    return collection


def serialize(obj, ignore=None):
    if not ignore:
        ignore = []

    for x in obj:
        if x in ignore:
            continue
        if isinstance(obj[x], datetime.datetime):
            obj[x] = str(obj[x])
        if isinstance(obj[x], enum.Enum):
            obj[x] = obj[x].value
    return obj


def serialize_foreign(obj, k, ignore=None):
    f_obj = getattr(obj, k, [])
    f_obj = to_dict(f_obj, ignore)
    o = {}
    for x in f_obj:
        o[k + '__' + x] = f_obj[x]
    return o
