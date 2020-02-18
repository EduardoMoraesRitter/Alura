import csv
def carregar_acessos():

    x = []#lado direito
    y =[]#as classificaçoes lado esquerdo

    #abrir o arquivo
    arquivo = open('acesso.csv', 'r')

    #leitor de csv
    leitor = csv.reader(arquivo)
    next(leitor)

    #ler cada linha
    for home,como,contato,comprou in leitor:
        dado = [int(home),int(como),int(contato)]
        x.append(dado)
        y.append(int(comprou))

    return x, y

