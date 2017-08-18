"""This file contain the scraper needed to fill 
the data model based on a XBRL file provided.
"""

# Import libraries
import pandas as pd
import untangle

# App imports
from settings import session_scope
from data_model import Fund, Firm

class XBRLScraper(object):
    
    def __init__(self, xbrl_file, fund_nif, firm_name):
        """Initialize the parser given a path to
        the XBRL file to be parsed.
        
        * Assign the path to an attribute
        * Get the file tree from file.
        * Get the root from the tree.
        """
        self.xbrl_file = xbrl_file
        self.root = untangle.parse(self.xbrl_file)
        self.fund_nif = fund_nif
        self.firm_name = firm_name

    def get_database_data(self):
        """Search for information in database.
        """
        with session_scope() as s:
            # Get firm
            self.firm = s.query(Firm).filter(Firm.name==self.firm_name).one()
            # Get fund
            self.fund = s.query(Fund).filter(Fund.nif==self.fund_nif).one()

    def get_date_info(self):
        """Extract date information from the
        XBRL file.
        """
        pass

    def get_companies_info(self):
        """Extract companies information from the 
        XBRL file
        
        * Get shares in listed companies
        """
        companies = (self.root.xbrli_xbrl
                     .iic_fim_InformeFIM
                     .iic_fim_DatosFondoCompartimentoFIM
                     .iic_fim_InversionesFinancierasFIM
                     .iic_com_InversionesFinancierasValorEstimado
                     .iic_com_InversionesFinancierasInterior
                     .iic_com_InversionesFinancierasRVCotizada
        )

        companies_list = []
        submissions_list = []
        for c in companies:
            isin = c.iic_com_CodigoISIN.cdata
            eop_pct, bop_pct, eop_value, bop_value = None, None, None, None
            # Loop over values

            for p in c.iic_com_InversionesFinancierasImporte:
                # Get percentages
                pct = p.iic_com_InversionesFinancierasPorcentaje
                contextPct = pct.get_attribute('contextRef')
                if contextPct.endswith('ia'):
                    eop_pct = pct.cdata
                elif contextPct.endswith('ipy'):
                    bop_pct = pct.cdata

                # Get absolute values
                val = p.iic_com_InversionesFinancierasValor
                contextVal = val.get_attribute('contextRef')
                if contextVal.endswith('ia'):
                    eop_val = val.cdata
                elif contextVal.endswith('ipy'):
                    bop_val = val.cdata
                
            submission_dict = {
                'company_isin': isin
                ,'fund_submission_id': self.fund_isin
                ,'eop_value': eop_val
                ,'eop_pct': eop_pct
                ,'bop_value': bop_val
                ,'bop_pct': bop_pct
            }

            company_dict = {
                'isin': isin
                ,'name': c.iic_com_InversionesFinancierasDescripcion.cdata.split("|")[1]
            }
            
            companies_list.append(company_dict)
            submissions_list.append(submission_dict)
            
        return companies_list, submissions_list

    def pipeline(self):
        """Execute the whole pipeline of parsing the file.

        1. Information received:
          * Fund nif.
          * Firm name.
        2. Get information from database about the fund.
        3. Parse date information from the fund.
        4. Parse companies information from the xbrl.

        Steps:
        
        1. Get Fund and Firm information from database.
        2. Build and create Fund Submission.
        3. Create new companies.
        4. Add fund portfolio (CompanySubmission)
        """
        pass
