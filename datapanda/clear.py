#one
import pandas as pd

df = pd.read_csv("data.csv")
result = df.isnull()
print(result)
new_df = df.dropna()

print(new_df.to_string())
