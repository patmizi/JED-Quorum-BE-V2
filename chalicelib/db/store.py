from chalicelib.lib.exceptions import NotFoundException
from . import DatabaseSession


class MySqlStore:
    def update_object(self, entity, _id, primary_key, params):
        with DatabaseSession() as session:
            data = session.query(entity).filter(entity.id == _id).first()

            if not data:
                raise NotFoundException()

            for k, v in params.items():
                print(k)
                if not hasattr(data, k):
                    raise ValueError("Entity {} doesn't have the property `{}`".format(entity.__class__.__name__, k))
                print('k: ', k)
                print('v: ', v)
                print('data: ', data.address)
                setattr(data, k, v)

            session.commit()
            return data

    def normalize(self, o):
        pass
