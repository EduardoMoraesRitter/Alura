from collections import Counter
from sklearn.model_selection import cross_val_score # essa é a ultima versao deprecida => from sklearn.cross_validation import cross_val_score
from sklearn.svm import LinearSVC

import pandas as pd
import numpy as np
import nltk #pip install nltk

#no terminal em corpora de linguagem depois stopwords e download, verifica so uma vez
#nltk.download('stopwords') 
stopwords = nltk.corpus.stopwords.words("portuguese")

#para ter a raiza das palavras
#nltk.download('rslp')
stemmer = nltk.stem.RSLPStemmer()
#stemmer.stem("amigos")

classificacoes = pd.read_csv('email.csv', encoding = 'utf-8')
textosPuros = classificacoes['email']

textosQuebrados = textosPuros.str.lower().str.split(' ')
dicionario = set()
for lista in textosQuebrados:
    validas = [stemmer.stem(palavra) for palavra in lista if palavra not in stopwords and len(palavra)>0]
    dicionario.update(validas)
print(dicionario)

totalPalavras = len(dicionario)
print(totalPalavras)
tuplas = list(zip(dicionario, range(totalPalavras)))
tradutor = {palavra:indice for palavra, indice in tuplas}

def vetorizar_texto(texto, tradutor):
    vetor = [0] * len(tradutor)
    for palavra in texto:
        if len(palavra)>0:
            raiz = stemmer.stem(palavra)
            if raiz in tradutor:
                posicao = tradutor[raiz]
                vetor[posicao] += 1
    return vetor

#print(vetorizar_texto(textosQuebrados[0], tradutor))
#print(vetorizar_texto(textosQuebrados[1], tradutor))
#print(vetorizar_texto(textosQuebrados[2], tradutor))

vetoresDeTexto = [vetorizar_texto(texto, tradutor) for texto in textosQuebrados]
print(vetoresDeTexto[0])

marcas = classificacoes['classificacao']

X = np.array(vetoresDeTexto)
Y = np.array(marcas.tolist())

porcentagem_treino = 0.8
tamanho_treino = int(porcentagem_treino * len(Y))
tamanho_validacao = len(Y) - tamanho_treino

treino_dados = X[0:tamanho_treino]
treino_marcacoes = Y[0:tamanho_treino]

validacao_dados = X[tamanho_treino:]
validacao_marcadores = Y[tamanho_treino:]

def fit_predict(nome, modelo, treino_dados, treino_marcacoes):
    k=10
    scores = cross_val_score(modelo, treino_dados, treino_marcacoes, cv=k)
    taxa_acerto = np.mean(scores)

    msg = 'Taxa de acerto do {0}: {1}'.format(nome, taxa_acerto)
    print(msg)
    return taxa_acerto


resultados = {}

from sklearn.multiclass import OneVsRestClassifier
modeloOneVsRest = OneVsRestClassifier(LinearSVC(random_state=0))
resultadoOneVsRest = fit_predict('OneVsRest', modeloOneVsRest, treino_dados, treino_marcacoes)
resultados[resultadoOneVsRest] = modeloOneVsRest

from sklearn.multiclass import OneVsOneClassifier
modeloOneVsOne = OneVsOneClassifier(LinearSVC(random_state=0))
resultadoOneVsOne = fit_predict('OneVsOne', modeloOneVsOne, treino_dados, treino_marcacoes)
resultados[resultadoOneVsOne] = modeloOneVsOne

from sklearn.naive_bayes import MultinomialNB
modeloMultinomialNB = MultinomialNB()
resultadoMultinomialNB = fit_predict('MultinomialNB', modeloMultinomialNB, treino_dados, treino_marcacoes)
resultados[resultadoMultinomialNB] = modeloMultinomialNB

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoostClassifier = AdaBoostClassifier(random_state=0)
resultadoAdaBoostClassifier = fit_predict('AdaBoostClassifier', modeloAdaBoostClassifier, treino_dados, treino_marcacoes)
resultados[resultadoAdaBoostClassifier] = modeloAdaBoostClassifier


#procurar na lista o resultado q for o maior
vencedor = resultados[max(resultados)]
print(vencedor)
vencedor.fit(treino_dados, treino_marcacoes)
resultadorvencedor = vencedor.predict(validacao_dados)

#mosta o vencedor
acertos = (resultadorvencedor == validacao_marcadores)
total_acertos = sum(acertos)
toral_elementos = len(validacao_dados)
taxa_acerto = 100.0 * total_acertos / toral_elementos

print("\n")
print("taxa de acerto do vencedor: {0} ".format(taxa_acerto))

#algoritimo basico
acerto_base = max(Counter(validacao_marcadores).values())
taxa_acerto_base = 100.0 * acerto_base/len(validacao_marcadores) 
print("taxa de acerto base: %f" % taxa_acerto_base)
print("total de validacao: %i" % len(validacao_marcadores))


