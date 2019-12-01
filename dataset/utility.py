# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:56:46 2019

@author: kushal
"""

import numpy as np
import pandas as pd
import chardet
import re

class utility:
    # function to test if a file is in unicode
    def isItUnicode(filename):
        with open(filename, 'rb') as f:
            encodingInfo = chardet.detect(f.read())
            if "UTF" not in encodingInfo['encoding']: 
                    print("This isn't Unicode! It's", encodingInfo['encoding'])
            else: 
                print("Yep, it's Unicode.")
    
    def readFile(location, separator, encoding):
        df = pd.read_csv(location, sep=separator,encoding = encoding)
        return df

    def checkDuplicate(dataframe, columnName):
        
        if any(dataframe.duplicated(subset=[columnName])):
            df = dataframe.loc[dataframe.duplicated(subset=[columnName])]
            return df 
        
        
    def checkCount(dataframe, columnName):
         if(dataframe is not None):
                count = dataframe[columnName].count()
                return count
    
 #   def removeUnwantedCharacer(dataframe)
    def strip_character(dataCol):
         r = re.compile(r'[^a-zA-Z !@#$%&*_+-=|\:";<>,./()[\]{}\']')
         return r.sub('', dataCol)
     
    def getDataframe(filelocation,UniqueID,separator,encoding):
            
            columnName = UniqueID #"permalink"  "companies.txt" "\t" "ISO-8859-1"
            df = utility.readFile(filelocation,separator,encoding)
            df[columnName] = df[columnName].astype(str).str.lower()
            df[columnName] = df[columnName].apply(utility.strip_character)
            return df
            
    def getuniquecountDiff(dataframe1,dataframe2,column1,column2):
        df1 = dataframe1[column1].unique() 
        df2 = dataframe2[column2].unique()
        count =len(set(df1) ^ set(df2))
        print("**************set 2********************************")
      
        print("Symmetric difference :", count )
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        