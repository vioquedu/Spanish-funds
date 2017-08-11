"""This file define the data model to be implemented
"""
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BASE = declarative_base()


class Firm(BASE):
    """Assets management firm table

    * id: PK, Integer
    * name: Name of the firm
    """

    __tablename__ = 'firms'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=True)

    def __str__(self):
        return "<Firm(id: {}; name: {})>".format(
            self.id
            ,self.name
            )

class Fund(BASE):
    """Investment fund

    * id: PK, integer.
    * name: Fund name.
    * firm: Assets management firm to which the firm belongs. FK.
    """
    __tablename__ = 'funds'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=True)
    firm_id = Column(Integer, ForeignKey('firms.id'), nullable=False)
    firm = relationship(Firm)

    def __str__(self):
        return "<Fund(id: {}; name: {}; firm_id {}>".format(
            self.id
            ,self.name
            ,self.firm_id
            )

class FundSubmission(BASE):
    """Fund submission to the CNMV every quarter.
    
    * id: PK, integer.
    * eop: Ending of period. Date.
    * bop: Begining of period. Date.
    * fund_id: Fund of the submission.
    """
    __tablename__ = 'fund_submission'

    id = Column(Integer, primary_key=True, autoincrement=True)
    eop = Column(Date, nullable=False)
    bop = Column(Date, nullable=False)
    fund_id = Column(Integer, ForeignKey('funds.id'), nullable=False)
    fund = relationship(Fund)

    def __str__(self):
        return "<FundSubmission(id: {}; eop: {:%Y-%m-%d}; bop: {:%Y-%m-%d}; fund_id: {}>".format(
            self.id
            ,self.eop
            ,self.bop
            ,self.fund_id
            )

class Company(BASE):
    """Company table.

    * id: PK, integer
    * name: Company name.
    * ISIN_code: Company ISIN code
    """
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    isin = Column(String(45), nullable=False)

    def __str__(self):
        return "<Company(id: {}; name: {}; isin: {}>".format(
            self.id
            ,self.name
            ,self.isin
            )

class CompanySubmission(BASE):
    """State of a company in a fund submission

    * id: PK, integer
    * fund_submission_id: Id of the fund submission
    * company_id: Id of the Company
    """
    __tablename__ = 'company_submission'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)
    fund_submission_id = Column(Integer, ForeignKey('fund_submission.id'), nullable=False)
    eop_value = Column(Numeric, nullable=True)
    eop_pct = Column(Numeric, nullable=True)
    bop_value = Column(Numeric, nullable=True)
    bop_pct = Column(Numeric, nullable=True)

    # Relationship
    company = relationship(Company)
    fund_submission = relationship(FundSubmission)

    def __str__(self):
        return "<CompanySubmission(id: {}; company_id: {}; fund_submission_id: {}>".format(
            self.id
            ,self.company_id
            ,self.fund_submission_id
            )
