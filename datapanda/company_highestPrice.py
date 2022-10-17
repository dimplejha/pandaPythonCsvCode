

import pandas as pd
df = pd.read_csv("data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['price'].max()
print(priceDf)
