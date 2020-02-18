
import pandas as pd

classificacoes = pd.read_csv('email.csv')
textosPuros = classificacoes['email']
textosQuebrados = textosPuros.str.lower().str.split(' ')
dicionario = set()
for lista in textosQuebrados:
    dicionario.update(lista)


totalPalavras = len(dicionario)
tuplas = list(zip(dicionario, range(totalPalavras)))
palavrasIndices = {palavra:indice for palavra, indice in tuplas}


texto1 = "Se eu comprar cinco anos antecipados, eu ganho algum desconto?"
texto1Quebrados = texto1.lower().split(' ')
vetor = [0] * totalPalavras
print(vetor)
for palavra in texto1Quebrados:
    if palavra in palavrasIndices:
            posicao = palavrasIndices[palavra]
            vetor[posicao] += 1
            print(palavra, posicao)
    

print(vetor)



