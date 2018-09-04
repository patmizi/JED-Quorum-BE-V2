from chalicelib.lib.exceptions import NotFoundException
from . import DatabaseSession


class MySqlStore:
    def update_object(self, entity, _id, params):
        with DatabaseSession() as session:
            data = session.query(entity).filter(entity.id == _id).first()

            print("UPDATE_OBJECT")
            print(data)
            print("ID")
            print(_id)
            print("PARAMS")
            print(params)

            if not data:
                raise NotFoundException()

            for k, v in params.items():
                if not hasattr(data, k):
                    raise ValueError("Entity {} doesn't have the property `{}`".format(entity.__class__.__name__, k))
                setattr(data, k, v)

            session.commit()
            return data

    def normalize(self, o):
        pass
