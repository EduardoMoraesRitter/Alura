#atuqlizar o pip igual o npm
#python -m pip install --upgrade pip
import pandas as pd
#python -mpip install matplotlib
import matplotlib.pyplot as plt

movies = pd.read_csv("dados/regressao_linear_alura.csv")

x = movies['Investimento']
y = movies['Bilheteria']

plt.scatter(x,y)
plt.show()

#pegar uma amostra
sample = movies.sample(n=200)
x = sample['Investimento']
y = sample['Bilheteria']

plt.scatter(x,y)
plt.show()