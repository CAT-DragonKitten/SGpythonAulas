listaComNomes = ["Davi Barbosa","Davi Gerson","Diogo Verissimo","Leandro Vieira","Liam de Castro"]
print ("este sao os alunos da turma: "+ str(listaComNomes))
indice = int(input("coloque o indice:" ))
if indice < 0:
    print ("erro: indice nao encontrado")
elif indice > 5:
    print ("erro: indice nao encontrado")
else:
    print (listaComNomes[indice])
