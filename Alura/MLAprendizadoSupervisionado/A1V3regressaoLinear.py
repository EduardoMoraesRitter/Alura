#atuqlizar o pip igual o npm
#python -m pip install --upgrade pip
import pandas as pd
#python -mpip install matplotlib
import matplotlib.pyplot as plt
#pip install -U scikit-learn
from sklearn.model_selection import train_test_split
#biblioteca de manipulacao de matrix
import numpy as np
#importar modelo
from sklearn.linear_model import LinearRegression

movies = pd.read_csv("dados/regressao_linear_alura.csv")
'''
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
'''
#gerar um dataframe
investimentoDF = movies['Investimento']
bilheteriaDF = movies['Bilheteria']
#print(investimentoDF)

#dividir os dado em teste e treino
#investimentoTreino, investimentoTeste, bilheteriaTreino, bilheteriaTeste = train_test_split(investimentoDF, bilheteriaDF)
investimentoTreino, investimentoTeste, bilheteriaTreino, bilheteriaTeste = train_test_split(investimentoDF, bilheteriaDF, test_size=0.1)
print("investimentoTreino:", len(investimentoTreino), 
    "investimentoTeste:", len(investimentoTeste),
    "bilheteriaTreino:", len(bilheteriaTreino),
    "bilheteriaTeste:", len(bilheteriaTeste),
    )

#criar um arrary - verto coluna
investimentoTreino = np.array(investimentoTreino).reshape(len(investimentoTreino), 1)
investimentoTeste = np.array(investimentoTeste).reshape(len(investimentoTeste), 1)
bilheteriaTreino = np.array(bilheteriaTreino).reshape(len(bilheteriaTreino), 1)
bilheteriaTeste = np.array(bilheteriaTeste).reshape(len(bilheteriaTeste), 1)
print(type(investimentoTreino))

#criar o modelo
modelo = LinearRegression()

#treianr modelo
modelo.fit(investimentoTreino, bilheteriaTreino)

#intepta o eixo Y o qual quero adivinhar
print(modelo.intercept_)

#coeficiente angular decobiri o X 
print(modelo.coef_)

#testar o modelo passando o X que o valor q tenho e preciso descobrir o Y
#preciso passar um array com uma coluna
predicao = modelo.predict([[27.74456356]])
print("quantas pessoas vai ter:", predicao)

#validar a conta y = Mx + B
print(modelo.coef_*27.74456356+modelo.intercept_)

#medida de pontuacao de acertos e previsao
print(modelo.score(investimentoTreino, bilheteriaTreino))
print(modelo.score(investimentoTeste, bilheteriaTeste))