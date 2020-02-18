#!-*- coding: utf8 -*-

import pandas as pd

classificacoes = pd.read_csv('email.csv')
textosPuros = classificacoes['email']
textosQuebrados = textosPuros.str.lower().str.split(' ')
dicionario = set()
for lista in textosQuebrados:
    dicionario.update(lista)
#dicionario sem indice - print(dicionario)
#print(list(dicionario)[2])
totalPalavras = len(dicionario)
#print(totalPalavras)
tuplas = list(zip(dicionario, range(totalPalavras)))
#print(tuplas)

#so um dicionario(python)pode consultar assim > print(tuplas['pode'])

#agora temos um dicionario com indice
palavrasIndices = {palavra:indice for palavra, indice in tuplas}
#print(palavrasIndices)
print(palavrasIndices['como'])




