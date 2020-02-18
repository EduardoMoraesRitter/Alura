#tanto classificacao ou regressao

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split

filmes = pd.read_csv("dados/movies_multilinear_reg.csv", encoding = 'utf-8')

colunas  = filmes[filmes.columns[2:17]]
labels = filmes[filmes.columns[17:]]

treino_colunas, teste_colunas, treino_labels, teste_labels = train_test_split(colunas, labels, test_size=0.1)

treino_colunas = np.array(treino_colunas).reshape(len(treino_colunas),15)
teste_colunas = np.array(teste_colunas).reshape(len(teste_colunas),15)
treino_labels = treino_labels.values.ravel()
teste_labels = teste_labels.values.ravel()

#print(teste_labels)

modelo = tree.DecisionTreeRegressor()
modelo.fit(treino_colunas, treino_labels)

print(modelo.score(treino_colunas,treino_labels))
print(modelo.score(teste_colunas,teste_labels))

#comparar com o modelo de regressao linear
from sklearn.linear_model import LinearRegression

modeloLR = LinearRegression()
modeloLR.fit(treino_colunas, treino_labels)

print(modeloLR.score(treino_colunas,treino_labels))
print(modeloLR.score(teste_colunas,teste_labels))
