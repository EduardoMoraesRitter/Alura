#pip install pandas 

import pandas as pd
df = pd.read_csv('busca_modificado.csv')
x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

xdummies_df = pd.get_dummies(x_df)
ydummies_df = y_df

x_arr = xdummies_df.values
y_arr = ydummies_df.values

########################################### codigo do algoritimo

#dado de treinamento sao 90%
tamanho_treino = int(0.9 * len(y_arr))
treino_dados = x_arr[:tamanho_treino]
treino_marcacoes = y_arr[:tamanho_treino]

#dados de teste sao 10%
tamanho_teste = len(y_arr) - tamanho_treino #0.1 * len(y_arr)c
teste_dados = x_arr[-tamanho_teste:]
teste_marcacoes = y_arr[-tamanho_teste:]

#from pega um parte da biblioteca
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
#82% sao bom ou ruim?, esse pergunta é dificio! depende


#nao posso usar a toda a base para fazer essa comparação é injusto, pos isso uso a teste_marcacoes
#o mesmo conjunto de dados, para algoritimos fiferentes
from collections import Counter
acerto_base = max(Counter(teste_marcacoes).values())
taxa_acerto_base = 100.0 * acerto_base/len(teste_marcacoes)
print("taxa de acerto base: %f" % taxa_acerto_base)

