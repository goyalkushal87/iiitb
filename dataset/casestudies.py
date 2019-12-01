# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:20:17 2019

@author: kushal
"""

import numpy as np
import pandas as pd
import utility as ut

   

 
def main():
  # dataframe companies  
  dataframe_companies = ut.utility.getDataframe("companies.txt","permalink", "\t","ISO-8859-1")  
  companies_count = ut.utility.checkCount(ut.utility.checkDuplicate(dataframe_companies,"permalink"),"permalink")
  print(companies_count)
  print("***********unique********************")
  print(dataframe_companies.permalink.nunique())
  print("***********nunique********************")
  # dataframe Funding round details: 
  dataframe_funding = ut.utility.getDataframe("rounds2.csv","company_permalink", ",","ISO-8859-1")
  funding_count = ut.utility.checkCount(ut.utility.checkDuplicate(dataframe_funding,"funding_round_permalink"),"funding_round_permalink")
  print(funding_count)
  print("***********unique********************")
  print(dataframe_funding.funding_round_permalink.nunique())
  print("***********nunique********************")
  
  
  #get unique count difference between dataframe
  #Are there any companies in the rounds2 file which are not  present in companies ?
  diff_companies = ut.utility.getuniquecountDiff(dataframe_companies,dataframe_funding,"permalink","company_permalink")
  print("Are there any companies in the rounds2 file which are not  present in companies ? ", diff_companies)
  
  # dataframe merging 
  master_frame = pd.merge(dataframe_companies, dataframe_funding, how ='inner', left_on ='permalink',right_on="company_permalink") 
  print(master_frame.count())
  
  
if  __name__ =='__main__':
    main()    