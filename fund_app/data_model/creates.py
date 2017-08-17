"""This file contains create methods in the data model.
"""


from data_model.tables import (Firm, Fund)
from settings import session_scope

class CreateMethod(object):
    """General class used to create classes.
    """
    sqlalchemy_class = None
    mandatory_content = []

    def __init__(self, dict_params={}, elements_list=[]):
        self.dict_params = dict_params
        self.element_list = elements_list

    def check_dict_content(self):
        assert set(self.mandatory_content).issubset(set(self.dict_params.keys()))

    def check_list_content(self):
        for e in self.element_list:
            assert set(self.mandatory_content).issubset(set(e.keys()))

    def create_element(self):
        """Insert element in table.
        """
        self.check_dict_content()
        obj = self.sqlalchemy_class(**self.dict_params)
        with session_scope() as s:
            s.add(obj)

    def create_elements_list(self):
        """Insert list of elements in table.
        """
        self.check_list_content()
        with session_scope() as s:
            for e in self.element_list:
                obj = self.sqlalchemy_class(**e)
                s.add(obj)
                

class CreateFirm(CreateMethod):
    """Create Firm
    """
    sqlalchemy_class = Firm
    mandatory_content = ['name']

class CreateFund(CreateMethod):
    """Create Fund
    """
    sqlalchemy_class = Fund
    mandatory_content = ['name', 'firm_id', 'isin_code']
