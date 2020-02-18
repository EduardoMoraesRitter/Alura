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

movies = pd.read_csv("dados/movies_multilinear_reg.csv")

#gerar um dataframe
investimentoDF = movies[movies.columns[2:17]]
bilheteriaDF = movies[movies.columns[17:]]
#print(investimentoDF)

#dividir os dado em teste e treino
#investimentoTreino, investimentoTeste, bilheteriaTreino, bilheteriaTeste = train_test_split(investimentoDF, bilheteriaDF)
investimentoTreino, investimentoTeste, bilheteriaTreino, bilheteriaTeste = train_test_split(investimentoDF, bilheteriaDF, test_size=0.3)
print("investimentoTreino:", len(investimentoTreino), 
    "investimentoTeste:", len(investimentoTeste),
    "bilheteriaTreino:", len(bilheteriaTreino),
    "bilheteriaTeste:", len(bilheteriaTeste),
    )

#criar o modelo
modelo = LinearRegression()

#treianr modelo
modelo.fit(investimentoTreino, bilheteriaTreino)

#testar o modelo passando o X que o valor q tenho e preciso descobrir o Y
#predicao = modelo.predict([[0,0,0,0,0,0,0,0,1,1,1,0,1,145.5170642,3.451632127]])
predicao = modelo.predict([[0,1,1,0,0,1,0,0,0,0,0,0,0,148.265861,5.599493131]])
print("bilheteria prevista:", predicao)

#medida de pontuacao de acertos e previsao
print(modelo.score(investimentoTreino, bilheteriaTreino))
print(modelo.score(investimentoTeste, bilheteriaTeste))