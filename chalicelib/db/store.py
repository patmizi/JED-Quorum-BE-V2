from chalicelib.lib.exceptions import NotFoundException
from chalicelib.db.entities import Address
from chalicelib.lib.helpers import get_date_from_string
from . import DatabaseSession


class MySqlStore:
    def update_object(self, entity, _id, params):
        with DatabaseSession() as session:
            entity = session.query(entity).filter(entity.id == _id)
            data = entity.first()

            if not data:
                raise NotFoundException()

            for k, v in params.items():
                print(k)
                if not hasattr(data, k):
                    raise ValueError("Entity {} doesn't have the property `{}`".format(entity.__class__.__name__, k))

                if k == 'Date_Of_Birth':
                    v = get_date_from_string(v)
                if k == 'address':
                    address = Address(
                        AddressId=params['address'].get('AddressId', None),
                        Suburb=params['address'].get('Suburb', ""),
                        Country=params['address'].get('Country', ""),
                        State=params['address'].get('State', ""),
                        Postcode=params['address'].get('Postcode', ""),
                        Street=params['address'].get('Street', ""),
                        Unit=params['address'].get('Unit', "")
                    )
                    address = session.merge(address)
                    setattr(data, k, address)
                else:
                    setattr(data, k, v)

            session.commit()
            return data

    def normalize(self, o):
        pass
