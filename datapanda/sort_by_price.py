# Sort all cars by Price column

import pandas as pd
carsDf = pd.read_csv("data.csv")
carsDf = carsDf.sort_values(by=['price'])
print(carsDf)
