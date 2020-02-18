#!-*- coding: utf8 -*-
#para trabalhar com acentos


texto1 = "Se eu comprar cinco anos antecipados, eu ganho algum desconto?"
texto2 = "O exercício 15 do curso de Java 1 está com a resposta errada. Pode conferir pf?"
texto3 = "Existe algum curso para cuidar do marketing da minha empresa?"

import pandas as pd

classificacoes = pd.read_csv('email.csv')
#print(classificacoes)

textosPuros = classificacoes['email']
#print(textosPuros)

#textosQuebrados = textosPuros.str.split(' ')
#print(textosQuebrados)

#criar um dicionario
#dicionario = []
#for lista in textosQuebrados:
#    dicionario.extend(lista)
#print(dicionario)

#em conjunto de calavras que existe maiusculo e minusculo no corriano nao existe 
# em caso de email ser spam ou emoção eu preciso distinguir para facilitar 
textosQuebrados = textosPuros.str.lower().str.split(' ')

#criar um conjunto de palavras 
dicionario = set()
for lista in textosQuebrados:
    dicionario.update(lista)
print(dicionario)



