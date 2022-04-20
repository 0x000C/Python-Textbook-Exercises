# Write an expression that generates the DataFrame
import pandas as pd

print(pd.read_csv('wwc2019_q-f.csv').loc[1:2:])