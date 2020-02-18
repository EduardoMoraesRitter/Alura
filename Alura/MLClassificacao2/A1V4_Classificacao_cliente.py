from collections import Counter
import pandas as pd

df = pd.read_csv('situacao_clientes.csv')
x_df = df[['recencia', 'frequencia', 'semanas_de_inscricao']]
y_df = df['situacao']

xdummies_df = pd.get_dummies(x_df)
ydummies_df = y_df
x_arr = xdummies_df.values
y_arr = ydummies_df.values

#porcentagens de teste treino e validação
por_treino = 0.8
por_teste = 0.1
por_validacao = 0.1

#separa os dados
tamanho_treino = int(por_treino * len(y_arr))
tamanho_teste = int(por_teste * len(y_arr))
tamanho_validacao = int(len(y_arr) - tamanho_treino - tamanho_teste)

#0 ate 799
treino_dados = x_arr[0:tamanho_treino]
treino_marcacoes = y_arr[0:tamanho_treino]

#800 ate 899
fim_teste = (tamanho_treino + tamanho_teste)
teste_dados = x_arr[tamanho_teste:fim_teste]
teste_marcacoes = y_arr[tamanho_teste:fim_teste]

#900 ate 999
valiacao_dados = x_arr[fim_teste:]
valiacao_marcacoes = y_arr[fim_teste:]

def fit_predict(modelo, nome, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)
    resultado_arr = modelo.predict(teste_dados)
    acertos = (resultado_arr == teste_marcacoes)
    total_acertos = sum(acertos)
    toral_elementos = len(teste_dados)
    taxa_acerto = 100.0 * total_acertos / toral_elementos
    print("taxa de acerto do {0}: {1} ".format(nome, taxa_acerto))
    return taxa_acerto

#usar um algoritimo quando tenho mult class
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
#modelo = OneVsRestClassifier(LinearSVC(random_state=0))
#modelo.fit(treino_dados, treino_marcacoes)
#print(modelo.predict(teste_dados))
#print(teste_marcacoes)
modeloOneVsRest = OneVsRestClassifier(LinearSVC(random_state=0))
resultadoOneVsRest = fit_predict(modeloOneVsRest, 'OneVsRest', treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)


#roda o algorimo
from sklearn.naive_bayes import MultinomialNB
modeloMultinomialNB = MultinomialNB()
resultadoMultinomialNB = fit_predict(modeloMultinomialNB, 'MultinomialNB', treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

#roda o algoritimo
from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoostClassifier = AdaBoostClassifier()
resultadoAdaBoostClassifier = fit_predict(modeloAdaBoostClassifier, 'AdaBoostClassifier', treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

if resultadoMultinomialNB > resultadoAdaBoostClassifier:
    vencedor = modeloMultinomialNB
else:
    vencedor = modeloAdaBoostClassifier

resultadorvencedor = vencedor.predict(valiacao_dados)

#mosta o vencedor
acertos = (resultadorvencedor == valiacao_marcacoes)
total_acertos = sum(acertos)
toral_elementos = len(valiacao_dados)
taxa_acerto = 100.0 * total_acertos / toral_elementos
print("taxa de acerto do vencedor: {0} ".format(taxa_acerto))

#algoritimo basico
acerto_base = max(Counter(valiacao_marcacoes).values())
taxa_acerto_base = 100.0 * acerto_base/len(valiacao_marcacoes) 
print("taxa de acerto base: %f" % taxa_acerto_base)
print("total de validacao: %i" % len(valiacao_marcacoes))

