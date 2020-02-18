#classificacao

import pandas as pd
from collections import Counter

movies = pd.read_csv("dados/avaliacoes_usuario_limpo.csv", encoding = 'utf-8')

print(Counter(movies['Gostou']))

from sklearn.model_selection import train_test_split

#pega todas as colunas caracteristicas
colunas  = movies[movies.columns[1:16]]
classes = movies[movies.columns[16:]]

treino_colunas, teste_colunas, treino_classe, teste_classe = train_test_split(colunas, classes, test_size=0.1)

print("treino gostaram", Counter(treino_classe['Gostou']))

import numpy as np

#transformar em arrarys
treino_colunas = np.array(treino_colunas).reshape(len(treino_colunas),15)
teste_colunas = np.array(teste_colunas).reshape(len(teste_colunas),15)
treino_classe = treino_classe.values.ravel()
teste_classe = teste_classe.values.ravel()

#importa a regressao logistica
from sklearn.linear_model import LogisticRegression
modelo = LogisticRegression(solver='lbfgs')
modelo.fit(treino_colunas, treino_classe)
previsao = modelo.predict(teste_colunas)

#medir a acuracia
from sklearn.metrics import accuracy_score
acuracia = accuracy_score(teste_classe,previsao)
print("acuracia: ", acuracia)

print("score: ",modelo.score(treino_colunas, treino_classe))

from sklearn.naive_bayes import GaussianNB #MultinomialNB
modeloNB = GaussianNB()#MultinomialNB()
modeloNB.fit(treino_colunas,treino_classe)
previsao_NB = modeloNB.predict(teste_colunas)

acuracia_NB = accuracy_score(teste_classe,previsao_NB)
print("acuracia_NB: ", acuracia)
print("score_ND: ",modeloNB.score(treino_colunas, treino_classe))


zotopia = [[0,0,0,0,0,0,0,1,1,1,1,0,1,110,27.74456356]]
print(modelo.predict(zotopia))


