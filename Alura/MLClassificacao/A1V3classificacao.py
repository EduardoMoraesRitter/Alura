#caracteristicas gordinho, perninha curta, au au
porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]
#criar um matrix com caracteristicas

dados=[porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]
#macar e classificar, 1 é porco e -1 é cachorro
marcacoes = [1,1,1,-1,-1,-1]
#misterioso, oque ele é
misterioso = [1,1,1]
misterioso2 = [1,0,0]

#imposta o pacote basico de classificaçao
from sklearn.naive_bayes import MultinomialNB

#criar o modelo
modelo = MultinomialNB()
#treinar modelo(se adequar ou se encachar)
modelo.fit(dados, marcacoes)

#testar o modelo, preveja
#print(modelo.predict(misterioso2)) 
#nas versoes futuras nao aceita um elemento

#todo de uma vez
teste = [misterioso,misterioso2]
print(modelo.predict(teste))




## R
# library(bnlearn)
# library(gRain)
# 
# data(learning.test)
#  bn <- naive.bayes(learning.test, "A")
#  fit <- bn.fit(bn, learning.test)
# #

#dclassify em NODEJS
#npm install bayes em NODEJS


