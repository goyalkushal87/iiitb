# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:56:46 2019

@author: kushal
"""

import numpy as np
import pandas as pd

class utility:
    
    
    def readFile(location, separator, encoding):
        df = pd.read_csv(location, sep=separator,encoding = encoding)
        return df

    def checkDuplicate(dataframe, columnName):
        
        if any(dataframe.duplicated(subset=[columnName])):
            df = dataframe.loc[dataframe.duplicated(subset=[columnName])]
            return df 
        
        
    def checkCount(dataframe, columnName):
        print(dataframe)
        return dataframe[columnName].count()