import pandas as pd
import csv
df = pd.read_csv("C:/Users/kirti/Dropbox/Python/C129/PRO-129-Datasets-main/final.csv")
print(df.shape)

del df["hyperlink"]
print(df.shape)
print(list(df))
df = df.rename({'pl_discmethod':"planet_discovery_method"})
df.to_csv('main.csv')