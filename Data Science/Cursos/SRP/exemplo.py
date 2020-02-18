from math import sqrt

#elevado
pow(3, 2)

#raiz quadrada
sqrt(pow(3-3, 2) + pow(3.5-4,2))

#evitar dicisao por zero e mudar a esca para percentual
1/(1+sqrt(pow(3-3, 2) + pow(3.5-4,2)))



from math import sqrt

#comparando dois
def euclidi(u1, u2):
    si = {}
    for item in avaliacoes[u1]:
        if item in avaliacoes[u2]: si[item] = 1

    if len(si) == 0: return 0

    soma = sum([pow(avaliacoes[u1][i] - avaliacoes[u2][i], 2)
                for i in avaliacoes[u1] if i in avaliacoes[u2]])

    return 1/(1+sqrt(soma))




>>> from recomendacao import euclidi
>>> euclidi('Leonardo', 'Ana')

euclidi('Ana', 'Claudia')
0.38742588672279304

#simularidade compada com todos ou encontramos usuarios parecidos
def getsimilares(usuario):
    similar = [(euclidi(usuario, outro), outro)
               for outro in avaliacoes if outro != usuario]
    similar.sort()#ordena 
    similar.reverse()#do maior para o menor
    return similar

#predizer a nota que usuario daria
def getrecomendacoes(usuario):
    totais={}
    somaSimilaridade={}
    for outro in avaliacoes:
        if outro == usuario: continue
        similaridade = euclidi(usuario, outro)#lista de similaridade

        if similaridade == 0: continue

        for item in avaliacoes[outro]:
            if item not in avaliacoes[usuario]:
                totais.setdefault(item, 0)
                totais[item] += avaliacoes[outro][item] * similaridade
                somaSimilaridade.setdefault(item, 0)
                somaSimilaridade[item] += similaridade
    rankings=[(total / somaSimilaridade[i], i) for i, total in totais.itens()]
    rankings.sort() 
    rankings.reverse()
    return rankings

######
from recomendacao import getrecomendacoes
getrecomendacoes('Leonardo')

#baseada em usuario - olho os usuario que fizeram avaliação em comum
#versus
#baseda em itens -




