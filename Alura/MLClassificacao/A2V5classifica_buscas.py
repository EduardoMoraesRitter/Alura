import csv

def carregar_busca():

    x = []
    y = []

    arquivo = open('busca.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home,busca,logado,comprou in leitor:
        dado = [int(home), busca, int(logado)]
        x.append(dado)
        y.append(int(comprou))
    
    return x,y

#print(carregar_busca())
#from A2V5classificador_busca import carregar_busca
x,y = carregar_busca()
print(x[0])
print(y[0])
