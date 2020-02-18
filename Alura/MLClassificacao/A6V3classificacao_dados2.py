import pandas as pd
df = pd.read_csv('busca.csv')
x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']
xdummies_df = pd.get_dummies(x_df)
ydummies_df = y_df
x_arr = xdummies_df.values
y_arr = ydummies_df.values

#porcentagens de teste treino e validação
por_treino = 0.8
por_teste = 0.1
por_validacao = 0.1

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

from sklearn.naive_bayes import MultinomialNB
fit_predict(MultinomialNB(), 'MultinomialNB', treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

from sklearn.ensemble import AdaBoostClassifier
fit_predict(AdaBoostClassifier(), 'AdaBoostClassifier', treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

from collections import Counter
y_obj = Counter(y_arr)
dic_y = y_obj.values()
acerto_maior = max(dic_y)
acerto_menos = min(dic_y)
taxa_acerto_base = 100.0 * acerto_maior/len(y_arr) 
print("taxa de acerto do algoritimo basico: %f" % taxa_acerto_base)

