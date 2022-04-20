# Write a function that returns the sum of the goals scored by winners.
import pandas as pd

print(pd.read_csv('wwc2019_q-f.csv')['W Goals'].sum())