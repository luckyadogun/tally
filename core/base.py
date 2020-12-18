import datetime
import itertools
from typing import List
from abc import ABCMeta, abstractmethod


class BaseError(TypeError): pass
class BaseInstantiationError(BaseError): pass
class EmptyImagesError(BaseError): pass
class ExpiryDateInputError(BaseError): pass


class BaseProduct(metaclass=ABCMeta):
    id_iter = itertools.count()

    def __init__(self, name, desc=''):
        self.name = name
        self.desc = desc
        self.images = []
        self.main_image = ''
        self.created = datetime.datetime.now()

    @property
    def date_created(self):
        return self.created.strftime("%Y-%m-%d")

    @abstractmethod
    def allproducts(self):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def update(self, id, **kwargs):
        pass

    @abstractmethod
    def delete(self, id):
        pass

