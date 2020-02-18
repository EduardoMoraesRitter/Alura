import csv
def carregar_acessos():

    dados = []#lado direito
    marcacoes =[]#as classificaçoes lado esquerdo

    #abrir o arquivo
    arquivo = open('acesso.csv', 'r')

    #leitor de csv
    leitor = csv.reader(arquivo)

    #ler cada linha
    for acessou_home,acessou_como_funciona,acessou_contato,comprou in leitor:
        dados.append([acessou_home,acessou_como_funciona,acessou_contato])
        marcacoes.append(comprou)

    return dados, marcacoes

