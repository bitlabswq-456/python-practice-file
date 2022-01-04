import pandas as pd
std=pd.read_csv("pandas/Students.csv")
data=std.head(5)
print(data)
data.to_csv("pandas/updatedfile.csv")
