# Count total cars per company

import pandas as pd

df = pd.read_csv("data.csv")
result = df["company"].value_counts()
print(result)
