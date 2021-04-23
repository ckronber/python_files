import pandas as pd

#
#df = pd.read_csv('imdb.csv')
#print(df.head())
#print(df.info())
#df.rename(columns = {'name': 'movie_title'},inplace = True)
#df.columns = ['ID','Title','Category','Year Released','Rating']
#print(df)


df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df['clinic_north'] #select 1 column of information
print(type(clinic_north))

clinic_north_south = df[['clinic_north','clinic_south']] #select 2 columns of information
print(type(clinic_north_south))

march = df.iloc[2] #select the march row

april_may_june = df[-3:]  #dataframe starting with row 3 to the end of the rows
print(april_may_june)

january = df[df.month == 'January'] # different way of selecting a column
print(january)

march_april = df[(df.month == 'March') | (df.month == 'April')]
print(march_april)

january_february_march = df[df.month.isin(['January','February','March'])]
print(january_february_march)

df2 = df.loc[[1, 3, 5]]
print(df2)
df3 = df2.reset_index()
df2.reset_index(inplace = True,drop = True)
print(df2)
print(df3)