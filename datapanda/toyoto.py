import pandas as pd
df = pd.read_csv("data.csv")

car_Manufacturers = df.groupby('company')
print(car_Manufacturers.get_group('toyota'))
