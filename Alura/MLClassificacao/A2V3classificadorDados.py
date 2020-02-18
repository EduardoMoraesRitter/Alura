from A2V1dados2 import carregar_acessos
x, y = carregar_acessos()
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(x,y)

resultado = modelo.predict(x)

diferencas = resultado - y
acertos = [ d for d in diferencas if d == 0 ]
total_acertos = len(acertos)
total_elementos = len(x)
taxa_acerto = 100.0 *  total_acertos / total_elementos

print(total_acertos)
print(total_elementos)

print(taxa_acerto)