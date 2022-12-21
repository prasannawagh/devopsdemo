import pandas as pd
import sys
import os

data = pd.Series([1,2,3])

file_path = sys.path.append(os.environ['WORKSPACE']) + "/config/mapping/map1.csv"
df = pd.read_csv(file_path,sep=',')

print(df)
print('Hello World')
print (data)
