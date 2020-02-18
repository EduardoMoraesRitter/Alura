# from A2V1dados import carregar_acessos

#dados, marcacoes = carregar_acessos()

#marcacoes

import csv
ifile  = open('acesso.csv', "r")
read = csv.reader(ifile)
for row in read :
    print (row) 