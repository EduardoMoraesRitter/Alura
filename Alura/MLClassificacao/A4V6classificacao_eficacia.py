#pip install pandas 

#o import pega toda a biblioteca
import pandas as pd

#data frame, nao é um array
df = pd.read_csv('busca_modificado.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

#tranforma minha linha categorizadas em colunas(ou em boliano)
xdummies_df = pd.get_dummies(x_df)
#nao precisa mais é bom
#ydummies = pd.get_dummies(y)[1]
ydummies_df = y_df

#tranformar em array
x_arr = xdummies_df.values
y_arr = ydummies_df.values

########################################### contador
from collections import Counter

#objeto com os valores
y_obj = Counter(y_arr)
#um dicionario
dic_y = y_obj.values() # so na versao antiga.intervalues()
#o maximo e o minimo
acerto_maior = max(dic_y)
acerto_menos = min(dic_y)

#filtra so os elemento q sao zero
#qual a eficacia do algoritimo
#acerto_um = list(y_arr).count('sim')#len(y_arr[y_arr=='sim']) #sum(y_arr)
#acerto_zero = len(y_arr[y_arr=='nao']) #len(y_arr) - acerto_um

#o maior é oq devo usar
taxa_acerto_base = 100.0 * acerto_maior/len(y_arr) #max(acerto_um, acerto_zero) / len(y_arr)

#print("taxa de acerto base: %d" % taxa_acerto_base) -- %d é pra inteiro
print("taxa de acerto base: %f" % taxa_acerto_base) #para numero flutuante

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

