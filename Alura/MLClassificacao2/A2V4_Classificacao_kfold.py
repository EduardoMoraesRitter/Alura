from collections import Counter
import pandas as pd

df = pd.read_csv('situacao_clientes.csv')
x_df = df[['recencia', 'frequencia', 'semanas_de_inscricao']]
y_df = df['situacao']

xdummies_df = pd.get_dummies(x_df)
ydummies_df = y_df
x_arr = xdummies_df.values
y_arr = ydummies_df.values

#com KFOLD nao tem mais teste e sim testo diversas vezes
por_treino = 0.8

#separa os dados
tamanho_treino = int(por_treino * len(y_arr))
#tamanho_validacao = int(len(y_arr) - tamanho_treino)

#0 ate 799
treino_dados = x_arr[0:tamanho_treino]
treino_marcacoes = y_arr[0:tamanho_treino]

#900 ate 999
valiacao_dados = x_arr[tamanho_treino:]
valiacao_marcacoes = y_arr[tamanho_treino:]

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
#from sklearn.cross_validation import cross_val_score  depreciado
from sklearn.model_selection import cross_val_score
modelo = OneVsRestClassifier(LinearSVC(random_state=0))
k=3
score = cross_val_score(modelo, treino_dados,treino_marcacoes, cv = k)
print("cada pedação:", score)

#tirar a media
import numpy as np
print("media do score: ", np.mean(score))