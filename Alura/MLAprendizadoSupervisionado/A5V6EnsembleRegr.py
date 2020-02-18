#tanto classificacao ou regressao

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
#https://scikit-learn.org/stable/modules/model_evaluation.html
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor

filmes = pd.read_csv("dados/movies_multilinear_reg.csv", encoding = 'utf-8')

colunas  = filmes[filmes.columns[2:17]]
labels = filmes[filmes.columns[17:]]

treino_colunas, teste_colunas, treino_labels, teste_labels = train_test_split(colunas, labels)

treino_colunas = np.array(treino_colunas).reshape(len(treino_colunas),15)
teste_colunas = np.array(teste_colunas).reshape(len(teste_colunas),15)
treino_labels = treino_labels.values.ravel()
teste_labels = teste_labels.values.ravel()

print(treino_colunas.shape)
print(teste_colunas.shape)
print(treino_labels.shape)
print(teste_labels.shape)

############################################################

#podemos limite numero de arvores n_estimators=20
modelo = AdaBoostRegressor()
modelo.fit(treino_colunas, treino_labels)

print("AdaBoostRegressor")
print("score treino: ",modelo.score(treino_colunas,treino_labels))
print("score teste: ",modelo.score(teste_colunas,teste_labels))
print("acuracia: ", accuracy_score(teste_labels,modelo.predict(teste_colunas)))
#print("acuracia: ", accuracy_score([int(x) for x in treino_labels], [int(x) for x in modelo.predict(treino_colunas)] ))

modeloLR = GradientBoostingRegressor()
modeloLR.fit(treino_colunas, treino_labels)

print("GradientBoostingRegressor")
print("score treino: ",modeloLR.score(treino_colunas,treino_labels))
print("score teste: ",modeloLR.score(teste_colunas,teste_labels))
#o parametro pode ser tanto numpy.ndarray quanto list 
# porem so pode ser numero inteiro e nao float
# o conversor np.around(teste_labels, 0) e np.around(modeloLR.predict(teste_colunas), 0) nao funciona
#print("acuracia: ", accuracy_score([int(x) for x in teste_labels], [int(x) for x in modeloLR.predict(teste_colunas)] ))

#nao existe essa acuracia em regressao
print(r2_score(teste_labels, modeloLR.predict(teste_colunas)))

'''
#testando os dados
zootopia = [0,0,0,0,0,0,0,1,1,1,1,0,1,110,27.74456356]
print("ZOTOPIA: ", modelo.predict([zootopia]))
'''
