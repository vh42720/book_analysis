"""
### 01 - Cleaning the datasets

This notebook outlines the cleaning process for the publishers data set which
contains Amazon ebook daily sales records from 2015. The data is taken from
Corgis project. Fortunately, the data is clearly label and preprocessed.
The main objectives would be removing redundant columns and reformatting
some names.

Data:
1. [publishers](https://corgis-edu.github.io/corgis/csv/publishers/)
    * Ebook sales data from Amazon for 27k titles in 2015

After cleaning, the data is renamed to book_sales for easy reference.
"""

import matplotlib.pyplot as plt
import pandas as pd

from ebook_analysis.config.config import *

# parameters
data_path = data_path
sales = pd.read_csv(f'{data_path}\\publishers.csv')

# cleaning steps
# replace dot and space in columns name.
sales.columns = sales.columns.str.replace(r'[\.\s]', '_')

# Remove the word statistic in column name
sales.columns = sales.columns.str.replace('statistics_', '')

# remove multiple revenues and gross sales columns
sales = sales.drop(sales.columns[2:6], axis=1)
sales = sales.drop('sales_rank', axis=1)

# list of repeated companies name
harper = ['HarperCollins Christian Publishing',
          'HarperCollins Publishers',
          'HarperCollins Publishing']
randomhouse = ['Random House LLC',
               'Random House Mondadori']

# rename sold_by all sub names for companies into one
sales['sold_by'] = sales['sold_by'].replace(harper, 'HarperCollins')
sales['sold_by'] = sales['sold_by'].replace(randomhouse, 'Random House')

# save the cleaned data with new name
sales.to_csv(f'{data_path}\\ebook_sales.csv')

# print out the cleaned data set info
print(sales.info())
