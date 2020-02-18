import pandas as pd

classificacoes = pd.read_csv('email.csv')
textosPuros = classificacoes['email']
textosQuebrados = textosPuros.str.lower().str.split(' ')
dicionario = set()
for lista in textosQuebrados:
    dicionario.update(lista)


totalPalavras = len(dicionario)
tuplas = list(zip(dicionario, range(totalPalavras)))
tradutor = {palavra:indice for palavra, indice in tuplas}
print(totalPalavras)

def vetorizar_texto(texto, tradutor):
    vetor = [0] * len(tradutor)
    for palavra in texto:
        if palavra in tradutor:
            vetor[tradutor[palavra]] += 1
    return vetor

#print(vetorizar_texto(textosQuebrados[0], tradutor))
#print(vetorizar_texto(textosQuebrados[1], tradutor))
#print(vetorizar_texto(textosQuebrados[2], tradutor))

vetoresDeTexto = [vetorizar_texto(texto, tradutor) for texto in textosQuebrados]
print(vetoresDeTexto)

