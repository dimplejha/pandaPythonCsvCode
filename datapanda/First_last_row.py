import pandas as pd
df = pd.read_csv('data.csv')

first = df.head(5)
last = df.tail(5)

print(df.columns)
print(first)
print(last)
