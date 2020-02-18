from A2V1dados2 import carregar_acessos
x, y = carregar_acessos()

print(x)

print(y)

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

#lembrando q X sao os dado ou coluna e o Y sao as marcaçoes ou classes

#separa 90% para treino
treino_x = x[:80]
treino_y = y[:80]

#separando 10% para teste
teste_x = x[-20:]
teste_y = y[-20:]

modelo.fit(treino_x,treino_y)

resultado = modelo.predict(teste_x)

diferencas = resultado - teste_y
acertos = [ d for d in diferencas if d == 0 ]
total_acertos = len(acertos)
total_elementos = len(teste_x)
taxa_acerto = 100.0 *  total_acertos / total_elementos

print(total_acertos)
print(total_elementos)

print(taxa_acerto)