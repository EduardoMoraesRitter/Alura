#tanto classificacao ou regressao

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

filmes = pd.read_csv("dados/avaliacoes_usuario_limpo.csv", encoding = 'utf-8')

colunas  = filmes[filmes.columns[1:16]]
labels = filmes[filmes.columns[16:]]

treino_colunas, teste_colunas, treino_labels, teste_labels = train_test_split(colunas, labels)

treino_colunas = np.array(treino_colunas).reshape(len(treino_colunas),15)
teste_colunas = np.array(teste_colunas).reshape(len(teste_colunas),15)
treino_labels = treino_labels.values.ravel()
teste_labels = teste_labels.values.ravel()

#print(teste_labels)

modelo = tree.DecisionTreeClassifier(max_depth=20)
modelo.fit(treino_colunas, treino_labels)

print("DecisionTreeClassifier")
print("score: ",modelo.score(treino_colunas,treino_labels))
print("score: ",modelo.score(teste_colunas,teste_labels))
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


