import json

from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import date, datetime

from chalicelib.lib.helpers import serialize_date, iso_date


def recursive_alchemy_encoder():
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
                    if field == 'id':  # id should not be returned because it is a synonym
                        continue
                    if isinstance(obj.__getattribute__(field), datetime):
                        fields[field] = iso_date(obj.__getattribute__(field))
                    elif isinstance(obj.__getattribute__(field), date):
                        fields[field] = serialize_date(obj.__getattribute__(field))
                    else:
                        fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder
