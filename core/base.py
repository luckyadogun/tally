import datetime
from typing import List


class BaseError(TypeError): pass
class BaseInstantiationError(BaseError): pass
class EmptyImagesError(BaseError): pass
class ExpiryDateInputError(BaseError): pass



# TODO:
# Dynamic class naming should it change 

class BaseProduct:
    """
    Abstract Base Class

    NOTE: This class should not be instatiated.

    This class congregates the similar properties and behaviors
    across deriving classes.

    This class should be inherited by:

        - TangibleBaseProduct class: A sub-base class for tangible products
        - DigitalProduct class: A sub class for digital products

    """

    def __init__(self, name, desc=''):
        self.name = name
        self.desc = desc
        self.images = []
        self.main_image = ''

    def add_images(self, images: List):
        for img in images:
            self.images.append(img)

    def set_main_image(self, index: int):
        if len(self.images) == 0:
            raise EmptyImagesError
    
        self.main_image = self.images[index]
        print("Successful...")

    def __new__(cls, *args, **kwargs):
        if cls is BaseProduct:
            raise BaseInstantiationError(cls)
        return BaseProduct.__new__(cls, *args, **kwargs)


# class TangibleProduct(BaseProduct):
#     """
#         Abstract Class inheriting from BaseProduct class

#         This class should not be instatiated.
#     """
#     def __init__(self, name: str, weight: int, width: int, height: int, desc=''):
#         super().__init__(name, desc)
#         self.weight = weight
#         self.width = width
#         self.height = height
#         self.expires = None

#     def set_expiry_date(self, date_input: str):
#         try:
#             year, month, day = map(int, date_input.split('-'))
#             self.expires = datetime.datetime(year, month, day)
#         except Exception as e:
#             raise ExpiryDateInputError
        
#     def __new__(cls, *args, **kwargs):
#         if cls is TangibleProduct:
#             raise BaseInstantiationError(cls)
#         return TangibleProduct.__new__(cls, *args, **kwargs)



    
