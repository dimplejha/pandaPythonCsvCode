import pandas as pd
df = pd.read_csv('data.csv')


file_name = "data.csv"
for chunk in pd.read_csv(file_name, chunksize=5):
    
    print(chunk)


    
