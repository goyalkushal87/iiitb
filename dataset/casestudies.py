# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:20:17 2019

@author: kushal
"""

import numpy as np
import pandas as pd
import utility as ut

   

 
def main():
  columnName = "permalink"  
  df =ut.utility.readFile("companies.txt", "\t","ISO-8859-1")
  duplicate = ut.utility.checkDuplicate(df, columnName)
  if(duplicate is not None):
      print(duplicate)
      # check specific column
      count =ut.utility.checkCount(duplicate,columnName)
      print(count)
  else :
      print(df)
     
  # remove unwanted chaarcter

if  __name__ =='__main__':
    main()    