#tanto classificacao ou regressao

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#na regressao ele pega a media
from sklearn.ensemble import RandomForestRegressor

filmes = pd.read_csv("dados/movies_multilinear_reg.csv", encoding = 'utf-8')

colunas  = filmes[filmes.columns[2:17]]
labels = filmes[filmes.columns[17:]]

treino_colunas, teste_colunas, treino_labels, teste_labels = train_test_split(colunas, labels)

treino_colunas = np.array(treino_colunas).reshape(len(treino_colunas),15)
teste_colunas = np.array(teste_colunas).reshape(len(teste_colunas),15)
treino_labels = np.array(treino_labels).reshape(len(treino_labels),1)
teste_labels = np.array(teste_labels).reshape(len(teste_labels),1)

print(treino_colunas.shape)
print(teste_colunas.shape)
print(treino_labels.shape)
print(teste_labels.shape)

#podemos limite numero de arvores n_estimators=20
modelo = RandomForestRegressor(max_features=5, n_estimators=20)

#ele exije que a coluna de regressao seja um array apenas
modelo.fit(treino_colunas, treino_labels.ravel())

print("RandomForestRegressor")
print("score: ",modelo.score(treino_colunas,treino_labels))
print("score: ",modelo.score(teste_colunas,teste_labels))

'''
print("acuracia: ", accuracy_score(teste_labels,modelo.predict(teste_colunas)))



#comparar com o modelo de regressao linear
from sklearn.linear_model import LogisticRegression

modeloLR = LogisticRegression(solver='lbfgs')
modeloLR.fit(treino_colunas, treino_labels)

print("LogisticRegression")
print("score: ",modeloLR.score(treino_colunas,treino_labels))
print("score: ",modeloLR.score(teste_colunas,teste_labels))
print("acuracia: ", accuracy_score(teste_labels,modeloLR.predict(teste_colunas)))

#testando os dados
zootopia = [0,0,0,0,0,0,0,1,1,1,1,0,1,110,27.74456356]
print("ZOTOPIA: ", modelo.predict([zootopia]))
'''