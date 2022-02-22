import pandas as pd
import matplotlib.pyplot as plt 

plt.style.use('bmh')
#workbook1 = "rotten_tomatoes_movies_2.xlsx"
df = pd.read_csv('C:/Users/alialkirzam/OneDrive - Liverpool John Moores University/Documents/GitHub/csws-week3-3/data.csv')
#print(df.head())

x=df['genres']
y=df['authors']

plt.xlabel('genres', fontsize=20)
plt.ylabel('authors', fontsize=15)
plt.bar(x, y)
