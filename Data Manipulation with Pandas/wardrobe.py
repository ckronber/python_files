import pandas as pd
import csv


#dataframe 1
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name':['t-shirt','t-shirt','skirt','skirt'],
  'Color':['blue','green','red','black']
})

print(df1)


# dataframe 2
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3,'San Francisco', 90],
  [4,'Sacramento', 115]
  # Fill in rows 3 and 4
],
  columns=[
    #add column names here
    'Store ID','Location','Number of Employees'
  ])

print(df2)

