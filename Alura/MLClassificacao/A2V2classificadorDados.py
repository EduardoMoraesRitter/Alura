from A2V1dados2 import carregar_acessos

x, y = carregar_acessos()

#print(x,y)

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(x,y)

teste1 = [1,0,0]

print(modelo.predict([teste1]))