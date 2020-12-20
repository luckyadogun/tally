import inspect
import datetime

from . import base

class ProductError(Exception): pass
class InvalidProductIDError(ProductError): pass
class NoInstanceAccessError(ProductError): pass

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
        if not key in cls.store:
            raise InvalidProductIDError
        return cls.store.get(key)

    @classmethod
    def update(self, id, **kwargs):
        # TODO: Perform update here
        self.updated = datetime.datetime.now().strftime("%Y-%m-%d")

    def delete(self, id_):
        pass

    @staticmethod
    def is_valid_date(date_input: str):
        # TODO: Turn to a decorator if another method needs it
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
        obj = super().__getattribute__(instance)
        if inspect.ismethod(obj):
            raise NoInstanceAccessError("instances can't access class method")
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
    