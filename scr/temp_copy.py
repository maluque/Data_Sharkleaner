
## SHARKLEANER pipeline

### 1. Set working directory, load modules and set global ipynb properties

```python
# Check working directory
!pwd

python

# List files in the current directory
!ls

python

# Change directory to 'scr'
!cd scr

python

# List files in the 'scr' directory
!ls

python

import os
os.chdir("/Users/Marina/AMAYA_UBUNTU/PY_PROJECTS/IRONHACK/PROJECTS/Data_Sharkleaner/scr")
current_directory = os.getcwd()
# print(current_directory)

python

import pandas as pd
import numpy as np
import re

np.random.seed(42)
pd.set_option('display.max_columns', None)  # Show all columns

# To display plots in Jupyter
%matplotlib inline

python

import warnings
warnings.filterwarnings('ignore')  # Ignore warnings

python

import pylab as plt
import seaborn as sns
import fuzzywuzzy as fzw

IMPORT MY OWN FUNCTIONS (mlg) FROM "scr/dataanalysis1.py"

When I make modifications in the functions, I need to detach the module and load it again!

python

import dataanalysis_fun1 as mlg
# del mlg
# import dataanalysis_fun1 as mlg

python

import importlib
import dataanalysis_fun1  # Import the module
importlib.reload(dataanalysis_fun1)  # Reload the module

2. Load raw data frame

The original database has 27,723 rows and 24 columns.

python

sharks_raw = pd.read_csv('../data/attacks.csv', encoding="latin1")
sharks = sharks_raw.copy()
display(sharks.shape)

3. Clean data
3.1 Column names

    Rename columns if necessary. You manually replaced the column name "se" with "sex."

python

sharks = mlg.colnnam_clean(sharks)
sharks.rename(columns={"se": "sex"}, inplace=True)

3.2 NA's per row

Use the mlg.na_absperc function to count the percentage of NA's per column. Rows with more than 40% NA values are removed.

python

sharks2 = sharks.copy()
plt.figure(figsize=(10, 6))
mlg.na_absperc(sharks2.T)["perc_NA"].hist(bins=50, color='#e74c3c', edgecolor='white')
NA_sum_row = mlg.na_absperc(sharks2.T)
NA40_index = NA_sum_row["perc_NA"] > 40
NA40_index = NA40_index[NA40_index == True]
sharks2.drop(index=NA40_index.index, inplace=True)
sharks2.reset_index(drop=True, inplace=True)
mlg.na_heatmap(sharks)

3.3 Duplicated rows

Check for duplicated rows in the dataframe. The dataframe has no duplicated rows.

python

sharks3 = sharks2.copy()
display(any(sharks3.duplicated()))
print(f'The dataframe has {display(sharks3.duplicated().sum())} duplicated rows')

3.4 Drop uninformative and redundant columns

Columns such as "unnamed_22" and "unnamed_23" are dropped as they only contain NA's. The original ID key columns are dropped as well. Additional columns will be added to reach a total of 24 columns as requested in the exercise.

python

colnams_new = ['date', 'year', 'type', 'country', 'area', 'location', 'activity', 'name', 'sex', 'age', 'injury', 'fatal_y_n', 'time', 'specie', 'investigator_or_source', 'pdf', 'href_formula', 'href']
sharks3 = sharks3[colnams_new]
sharks3.head()

3.5 Correct "date" column

    Remove leading and trailing spaces from the "date" column.
    Correct misspelling errors and unnecessary words.
    Identify and drop uncertain records.

python

sharks5 = sharks4.copy()

# Remove leading and trailing spaces (Using apply + lambda combo)
sharks5['date'] = sharks5['date'].apply(lambda a: a.strip())

# Correct misspelling errors and unnecessary words
messy_terms = ["Reported", "Reportd", "Mid", "Circa", "circa", "Ca."]
for i in messy_terms:
    sharks5["date"] = sharks5["date"].str.replace(i, "")

# Identify uncertain records
uncertainty_terms = ["Before", "before", " or ", "A.D", "B.C", "No date", "\\?", "\\/"]
for i in uncertainty_terms:
    sharks5["date"] = np.where(sharks5["date"].str.contains(i), "uncertain", sharks5["date"])

# Drop uncertain values
BB = len(sharks5)
sharks5 = sharks5[sharks5["date"] != "uncertain"]
AA = len(sharks5)
print(f''' {BB-AA} rows dropped ''')
sharks5.reset_index(drop=True, inplace=True)
sharks5[["date"]].sample(230).T

Extract relevant information from the "date" column.

python

import datefinder as datf

sharks5_date = sharks5[["date"]]
month_list = []
year_list = []

for i in sharks5_date["date"]:
    thedate = list(datf.find_dates(i))
    years = [date.year for date in thedate]
    month = [date.month for date in thedate]
    year_list.append(years)
    month_list.append(month)

print(type(year_list[0]))
sharks5_date["year"] = year_list
sharks5_date["month"] = month_list
sharks5_date[["year"]].T
