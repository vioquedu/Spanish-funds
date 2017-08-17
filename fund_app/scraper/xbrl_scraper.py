"""This file contain the scraper needed to fill 
the data model based on a XBRL file provided.
"""

# Import libraries
import pandas as pd
import lxml
from lxml import etree

class XBRLScraper(object):
    
    def __init__(self, xbrl_file):
        """Initialize the parser given a path to
        the XBRL file to be parsed.
        
        * Assign the path to an attribute
        * Get the file tree from file.
        * Get the root from the tree.
        """
        self.xbrl_file = xbrl_file
        self.tree = etree.parse(self.xbrl_file)
        self.root = self.tree.getroot()

    def get_metadata(self):
        """Extract XBRL metadata.
        """
        pass

    def get_date_info(self):
        """Extract date information from the
        XBRL file.
        """
        pass

    def get_firm_info(self):
        """Extract firm information from
        the XBRL file.
        """
        pass

    def get_fund_info(self):
        """Extract fund information from the 
        XBRL file.
        """
        pass

    def get_companies_info(self):
        """Extract companies information from the 
        XBRL file
        """
        pass
        

    def pipeline(self):
        """Execute the whole pipeline of parsing the file.
        """
        pass
