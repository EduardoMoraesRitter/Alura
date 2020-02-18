from collections import Counter

from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score #deprecisado from sklearn.cross_validation import cross_val_score

import numpy as np
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

treino_dados = x_arr[0:tamanho_treino]
treino_marcacoes = y_arr[0:tamanho_treino]

#o restande aparti do tamanho do treino
valiacao_dados = x_arr[tamanho_treino:]
valiacao_marcacoes = y_arr[tamanho_treino:]

#numero de cortes que faço na base e rodo -> cv
def fit_predict(nome, modelo, treino_dados, treino_marcacoes):
    scores = cross_val_score(modelo, treino_dados, treino_marcacoes, cv=10)
    taxa_acerto = np.mean(scores)

    msg = 'Taxa de acerto do {0}: {1}'.format(nome, taxa_acerto)
    print(msg)
    return taxa_acerto

resultados = {}

from sklearn.multiclass import OneVsRestClassifier
modeloOneVsRest = OneVsRestClassifier(LinearSVC(random_state=0))
resultadoOneVsRest = fit_predict('OneVsRest', modeloOneVsRest, treino_dados, treino_marcacoes)
resultados[resultadoOneVsRest] = modeloOneVsRest

from sklearn.multiclass import OneVsOneClassifier
modeloOneVsOne = OneVsOneClassifier(LinearSVC(random_state=0))
resultadoOneVsOne = fit_predict('OneVsOne', modeloOneVsOne, treino_dados, treino_marcacoes)
resultados[resultadoOneVsOne] = modeloOneVsOne

from sklearn.naive_bayes import MultinomialNB
modeloMultinomialNB = MultinomialNB()
resultadoMultinomialNB = fit_predict('MultinomialNB', modeloMultinomialNB, treino_dados, treino_marcacoes)
resultados[resultadoMultinomialNB] = modeloMultinomialNB

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoostClassifier = AdaBoostClassifier()
resultadoAdaBoostClassifier = fit_predict('AdaBoostClassifier', modeloAdaBoostClassifier, treino_dados, treino_marcacoes)
resultados[resultadoAdaBoostClassifier] = modeloAdaBoostClassifier

#procurar na lista o resultado q for o maior
vencedor = resultados[max(resultados)]
vencedor.fit(treino_dados, treino_marcacoes)
resultadorvencedor = vencedor.predict(valiacao_dados)

#mosta o vencedor
acertos = (resultadorvencedor == valiacao_marcacoes)
total_acertos = sum(acertos)
toral_elementos = len(valiacao_dados)
taxa_acerto = 100.0 * total_acertos / toral_elementos

print("\n")
print("taxa de acerto do vencedor: {0} ".format(taxa_acerto))

#algoritimo basico
acerto_base = max(Counter(valiacao_marcacoes).values())
taxa_acerto_base = 100.0 * acerto_base/len(valiacao_marcacoes) 
print("taxa de acerto base: %f" % taxa_acerto_base)
print("total de validacao: %i" % len(valiacao_marcacoes))
