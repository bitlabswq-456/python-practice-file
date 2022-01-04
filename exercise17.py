#find whose marks greater than 50
import pandas as pd 
std=pd.read_csv("pandas/Students.csv") 
print(std[std['marks']>50])
