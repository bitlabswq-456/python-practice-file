import pandas as pd
std=pd.read_csv("Pandas/Students.csv")
print(std['marks'].max())
print(std['marks'].min())
print(std['marks'].sum())
print(std['marks'].count())
