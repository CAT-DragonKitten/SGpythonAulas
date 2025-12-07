ListaDePerg = ["quem foi que desenvolveu a bomba nuclear?", "qual foi o bombardeiro ultilizado no bombardeio de Hiroshima e Nagasaki?", "O que foi e a VDV?"]
ListaDeResp = ["robert openheimmer", "B-29 'enola gay'", "servico de praquedismo do exercio russo"]
acertos = 0
for indice in range(3):
    print (ListaDePerg[indice])
    resposta = input("sua resposta: ")
    if resposta == ListaDeResp[indice]:
        acertos += 1 
        print ("acertou.")
    elif resposta == "":
        print ("nem tentou...")
    else:
        print ("errou.")
print ("voce acertou: " + str(acertos))
