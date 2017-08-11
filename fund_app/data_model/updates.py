"""This file contains updates methods in the data model.
"""

from data_model.tables import (Firm, Fund)
from settings import session_scope

class UpdateMethod(object):
    """General class used to update SQLAlchemy objects.
    """
    sqlalchemy_class = None

    def __init__(self, dict_params={}, elements_list=[]):
        self.dict_params = dict_params
        self.elements_list = elements_list


    def update_element(self):
        """Update element from table
        """
        obj = self.sqlalchemy_class
        with session_scope() as s:
            instance = s.query(obj).filter(obj.id==self.dict_params['id']).one()
            for key in self.dict_params:
                setattr(instance, key, self.dict_params[key])

    def update_elements_list(self):
        """Update elements in table
        """
        obj = self.sqlalchemy_class
        with session_scope() as s:
            for i in self.elements_list:
                instance = s.query(obj).filter(obj.id==i['id']).one()
                for key in i:
                    setattr(instance, key, i[key])

class UpdateFirm(UpdateMethod):
    """UpdateFirm method
    """
    sqlalchemy_class = Firm


class UpdateFund(UpdateMethod):
    """Update Fund class
    """
    sqlalchemy_class = Fund


