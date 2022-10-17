

import pandas as pd
df = pd.read_csv('data.csv')


empty = []
for chunk in pd.read_csv("data.csv", chunksize=5):
    chunk["location"] = "pune"
    chunk["color"] = "black"
    chunk["run"] = "thousand"
    chunk.drop(["company"], axis=1, inplace=True)
    convert = chunk.values.tolist()
    for i in convert:
        empty.append(i)

print(empty)

columns = ["index", "body-style", "wheel-base", "length", "engine-type", "num-of-cylinders", "horsepower", "average-mileage", "price", "location", "color", "run"
           ]
df = pd.DataFrame(empty, columns=columns)

df.to_csv('file8.csv')
print(df)
