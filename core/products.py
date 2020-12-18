import base

class TangibleProduct(base.BaseProduct):
    store = []

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
        self.id = next(self.id_iter)
        self.store.append(self)

    def allproducts(self):
        return self.store

    def get(self, id):
        # TODO: Inefficient, run at O(log n)
        for product in self.store:
            if product.id == id:
                return product

    def update(self, id, **kwargs):
        # TODO
        # perform update
        # open from the store using context manager
        # read from the datastore
        # save the fields
        self.updated = datetime.datetime.now().strftime("%Y-%m-%d")

    def delete(self, id):
        pass

    def is_valid_date(date_input: str):
        # TODO: pull out to helpers
        # The length of a date string is 10
        # Also, the user can break the system
        # by supplying a 10-string that can't be 
        # converted to integers item which would 
        # beat the first validation metric
        # we can avoid this by using abs() function 

        result = None

        if date_input is not None and len(date_input) == 10:
            try:
                int("".join(date_input.split('-')))
            except ValueError:
                res = False
            else:
                result = True

    def set_expiry_date(self, date_input: str):
        if not self.is_valid_date(date_input):
            raise base.ExpiryDateInputError

        year, month, day = map(int, date_input.split('-'))
        self.expires = datetime.datetime(year, month, day)

    def __repr__(self):
        return f'<{self.id}, {self.name} - {self.__class__.__name__}>'


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
    