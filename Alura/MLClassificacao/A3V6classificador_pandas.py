#pip install pandas 

import pandas as pd

#data frame, nao é um array
df = pd.read_csv('busca.csv')

#print(df)

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

#print(x_df, y_df)

#tranforma minha linha categorizadas em colunas(ou em boliano)
xdummies_df = pd.get_dummies(x_df)
#nao precisa mais é bom
#ydummies = pd.get_dummies(y)[1]
ydummies_df = y_df

#print(xdummies_df, ydummies_df)

#tranformar em array
x_arr = xdummies_df.values
y_arr = ydummies_df.values

print(x_arr, y_arr)