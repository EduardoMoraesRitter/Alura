import pandas as pd
from collections import Counter
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.svm import LinearSVC
import nltk #pip install nltk

#nltk.download('stopwords') 
stopwords = nltk.corpus.stopwords.words("portuguese")
#nltk.download('rslp')
stemmer = nltk.stem.RSLPStemmer()
#nltk.download("punkt")

texto_dicionario = pd.read_csv('teste_dic.csv')['coluna']
#print(texto_dicionario)

texto_dicionario_raiz = [[stemmer.stem(palavra) for palavra in texto_dicionario if palavra not in stopwords and len(palavra)>1]]
#print(texto_dicionario_raiz)

dicionario = set()
for lista in texto_dicionario_raiz:
    dicionario.update(lista)
#print(dicionario)

totalPalavras = len(dicionario)
#print(totalPalavras)
tuplas = list(zip(dicionario, range(totalPalavras)))
#print(tuplas)
tradutor = {palavra:indice for palavra, indice in tuplas}
#print(tradutor)

def vetorizar_texto(texto, tradutor):
    vetor = [0] * len(tradutor)
    for palavra in texto:
        if len(palavra)>0:
            raiz = stemmer.stem(palavra)
            if raiz in tradutor:
                posicao = tradutor[raiz]
                vetor[posicao] += 1
                #print("posicao: ", posicao)

    return vetor

#print(vetorizar_texto("eu quero pizza", tradutor))

classificacoes = pd.read_csv('textos.csv')
textosPuros = classificacoes['exemplos']
frasesMinusculo = textosPuros.str.lower()

textosQuebrados = [nltk.tokenize.word_tokenize(frase) for frase in frasesMinusculo]
#print(textosQuebrados)

vetoresDeTexto = [vetorizar_texto(texto, tradutor) for texto in textosQuebrados]
#print(vetoresDeTexto)

marcas = classificacoes['classificacao']

X = np.array(vetoresDeTexto)
Y = np.array(marcas.tolist())
print(X, Y)

porcentagem_treino = 0.8
tamanho_treino = int(porcentagem_treino * len(Y))
tamanho_validacao = len(Y) - tamanho_treino

treino_dados = X[0:tamanho_treino]
treino_marcacoes = Y[0:tamanho_treino]

validacao_dados = X[tamanho_treino:]
validacao_marcadores = Y[tamanho_treino:]

def fit_predict(nome, modelo, treino_dados, treino_marcacoes):
    scores = cross_val_score(modelo, treino_dados, treino_marcacoes, cv=4)
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

"""
from sklearn.naive_bayes import MultinomialNB
modeloMultinomialNB = MultinomialNB()
resultadoMultinomialNB = fit_predict('MultinomialNB', modeloMultinomialNB, treino_dados, treino_marcacoes)
resultados[resultadoMultinomialNB] = modeloMultinomialNB

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoostClassifier = AdaBoostClassifier()
resultadoAdaBoostClassifier = fit_predict('AdaBoostClassifier', modeloAdaBoostClassifier, treino_dados, treino_marcacoes)
resultados[resultadoAdaBoostClassifier] = modeloAdaBoostClassifier
"""


#procurar na lista o resultado q for o maior
vencedor = resultados[max(resultados)]
print(vencedor)
vencedor.fit(treino_dados, treino_marcacoes)
resultadorvencedor = vencedor.predict(validacao_dados)

textoExemplo = vetorizar_texto( nltk.tokenize.word_tokenize("pizza eu querer oi"), tradutor)
print("CLASSIFICAO: ", vencedor.predict([textoExemplo]))

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