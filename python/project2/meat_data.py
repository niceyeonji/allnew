import numpy as np
from pandas import DataFrame
import pandas as pd

filename = 'meat.csv'
dataframe = pd.read_csv(filename, index='')
print(dataframe)

result = dataframe.loc[['2015']]
print(type(result))
print(result)