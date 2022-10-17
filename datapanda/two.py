import pandas as pd
df = pd.read_csv('data.csv')


result = df.drop([''],
                 axis=1, inplace=True)
print(result)

print(df.columns)
