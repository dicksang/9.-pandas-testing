# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:50:26 2020

@author: Dick Sang
"""

import pandas as pd

fruit_sales = pd.DataFrame({'Apples':[35, 41],'Bananas':[21, 34]}, index = [])

see = pd.read_csv('orders.csv', index_col = 'order_id')

pd.