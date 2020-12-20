import inspect
import datetime

from . import base

class TangibleProductError(Exception): pass
class InvalidIDError(TangibleProductError): pass
class NoInstanceAccessError(TangibleProductError): pass

class TangibleProduct(base.BaseProduct):
    store = {}

    def __init__(
            self, 
            name: str, 
            weight: int, 
            width: int, 
            height: int, 
            desc='',
        ):
        super().__init__(name, desc)
        self.weight = weight
        self.width = width
        self.height = height
        self.expires = None
        self.updated = None
        self.id = next(self.id_iter) + 1
        TangibleProduct.store[self.id] = self

    @classmethod
    def allproducts(cls):
        return cls.store

    @classmethod
    def get(cls, key):
        return cls.store.get(key)

    # def get(self, id):
    #     if id in self.store[id]:
    #         return TangibleProduct.store.get(id)
    #     else:
    #         raise InvalidProductIDException("TangibleProduct with ID: {id} doesn't exist!")

    @classmethod
    def update(self, id, **kwargs):
        # TODO
        # perform update
        # open from the store using context manager
        # read from the datastore
        # save the fields
        self.updated = datetime.datetime.now().strftime("%Y-%m-%d")

    def delete(self, id_):
        pass

    @staticmethod
    def is_valid_date(date_input: str):
        # TODO: 
        # I assume this will be used in other parts
        # of the codebase, so I suggest it be turned into
        # a decorator. If another decorator is needed
        # within the code, we could use a decorators.py module
        if date_input is not None and len(date_input) == 10:
            result = True if "".join(date_input.split('-')).isnumeric() else False
            return result

    def set_expiry_date(self, date_input: str):
        if not self.is_valid_date(date_input):
            raise base.ExpiryDateInputError

        year, month, day = map(int, date_input.split('-'))
        self.expires = datetime.datetime(year, month, day)

    def __repr__(self):
        return f'<{self.id}, {self.name} - {self.__class__.__name__}>'

    def __getattribute__(self, instance):
        # instances cannot access class methods
        obj = super().__getattribute__(instance)
        if inspect.ismethod(obj):
            raise NoInstanceAccessError("instance can't access class method")
        return obj
        


# class DigitalProduct(BaseProduct):
#     def __init__(
#             self, 
#             name: str, 
#             requirements: str,
#             version: float,
#             desc='',
#         ):
#         super().__init__(name, desc)
#         self.requirements = requirements
#         self.version = version
    