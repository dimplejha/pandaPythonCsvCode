import pandas as pd
df = pd.read_csv("data.csv")
df = df[['company', 'price']][df.price == df['price'].max()]
print(df)
