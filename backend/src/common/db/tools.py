import datetime
import enum
import json
import sqlalchemy

from sqlalchemy.ext.declarative import DeclarativeMeta
from common.db.base import Database
from common.server.flaskutils import print_flush

def to_dict(obj, ignore=None):
    if not ignore:
        ignore = []

    if str(type(obj)) == "<class 'sqlalchemy.util._collections.result'>":
        collection = {}
        for x in obj:
            collection.update(_to_dict(x, ignore, prefixe=True))
        return collection
    else:
        return _to_dict(obj, ignore)


def _to_dict(obj, ignore, prefixe=False):
    collection = {}
    for c in obj.__table__.columns:
        value = getattr(obj, c.name)
        if c.name not in ignore:
            if prefixe:
                collection.update({str(obj.__table__) + '__' + c.name: value})
            else:
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


def serialize_foreign_recursive(obj, level=1, flattened=False, flaten_key=None, ignored_keys=None):
    if level < 0:
        return str(obj)

    fields = {}
    for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
        value = obj.__getattribute__(field)
        if ignored_keys and field in ignored_keys:
            continue
        if str(type(value)) == "<class 'sqlalchemy.orm.dynamic.AppenderQuery'>":
            pass
        elif callable(value):
            pass
        elif isinstance(value.__class__, DeclarativeMeta):
            if flattened:
                fields.update(serialize_foreign_recursive(value, level - 1, flattened=flattened, flaten_key=field, ignored_keys=ignored_keys))
            else:
                fields[field] = serialize_foreign_recursive(value, level - 1, ignored_keys=ignored_keys)
        else:
            if flaten_key:
                fields[flaten_key + '__' + field] = value
            else:
                fields[field] = value

    return serialize(fields)


def new_alchemy_encoder():
    _visited_objs = []
    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    fields[field] = str(obj.__getattribute__(field))
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder

# no tested
def to_json(e):
    return json.dumps(e, cls=new_alchemy_encoder(), check_circular=False)

def update_id(db_obj, on_key):
    with Database(auto_commit=True) as db:
        scan = db.query(db_obj).all()

        for s in scan:
            xid = getattr(s, on_key)
            new_xid = xid.split('-')
            if len(new_xid) == 3:
                new_xid = new_xid[0] + ' ' + new_xid[1] + ' ' + new_xid[2]
                setattr(s, on_key, new_xid)
