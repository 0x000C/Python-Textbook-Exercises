# Write an expression that selects all even numbered rows in wwc.
import pandas as pd

print(pd.read_csv('wwc2019_q-f.csv').loc[2::2])