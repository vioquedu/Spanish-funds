"""This file contains create methods in the data model.
"""


from .tables import (Firm, Fund)
from ..settings import session_scope

class CreateMethod(object):
    """General class used to create classes.
    """
    sqlalchemy_class = None

    def __init__(self, dict_params={}, elements_list=[]):
        self.dict_params = dict_params
        self.element_list = elements_list

    def create_element(self):
        """Insert element in table.
        """
        obj = self.sqlalchemy_class(**self.dict_params)
        with session_scope() as s:
            s.add(obj)

    def create_elements_list(self):
        """Insert list of elements in table.
        """
        with session_scope() as s:
            for e in self.element_list:
                obj = self.sqlalchemy_class(**e)
                s.add(obj)
                

class CreateFirm(CreateMethod):
    """Create Firm
    """
    sqlalchemy_class = Firm
    
class CreateFund(CreateMethod):
    """Create Fund
    """
    sqlalchemy_class = Fund
