import pandas as pd
df = pd.read_csv('busca2.csv')
#nao brincar com minhas caracteristicas
#home, busca = 70 %
#busca, logado = 10%
x_df = df[['busca']] #df[['home', 'busca', 'logado']]
y_df = df['comprou']
xdummies_df = pd.get_dummies(x_df)
ydummies_df = y_df
x_arr = xdummies_df.values
y_arr = ydummies_df.values

tamanho_treino = int(0.9 * len(y_arr))
treino_dados = x_arr[:tamanho_treino]
treino_marcacoes = y_arr[:tamanho_treino]

tamanho_teste = len(y_arr) - tamanho_treino
teste_dados = x_arr[-tamanho_teste:]
teste_marcacoes = y_arr[-tamanho_teste:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado_arr = modelo.predict(teste_dados)
acertos = (resultado_arr == teste_marcacoes)

total_acertos = sum(acertos)
toral_elementos = len(teste_dados)
taxa_acerto = 100.0 * total_acertos / toral_elementos

print("total_acertos: ", total_acertos)
print("toral_elementos: ",toral_elementos)
print("taxa_acerto: %f" %taxa_acerto)

from collections import Counter
y_obj = Counter(y_arr)
dic_y = y_obj.values()
acerto_maior = max(dic_y)
acerto_menos = min(dic_y)
taxa_acerto_base = 100.0 * acerto_maior/len(y_arr) 
print("taxa de acerto do algoritimo basico: %f" % taxa_acerto_base)

