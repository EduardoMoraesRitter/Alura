porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]
dados=[porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]
marcacoes = [1,1,1,-1,-1,-1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

print("modelo: ")
print(modelo)

misterioso = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [0,0,1]
testes = [misterioso,misterioso2,misterioso3]
marcacoes_teste = [-1,1,-1]

resultado = modelo.predict(testes)

#quais diferencas atraves do teste
diferencas = resultado - marcacoes_teste

#quanto acertos eu tive
acertos = [d for d in diferencas if d == 0 ]

# pares = [n for n in range(10) if n % 2 == 0]

total_acertos = len(acertos)
total_elementos = len(testes)
print("total_acertos: " , total_acertos, " / total_elementos: " , total_elementos)

taxa_acertos = 100.0 * total_acertos / total_elementos
print(taxa_acertos)


