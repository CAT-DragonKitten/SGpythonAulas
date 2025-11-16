import random
maximo = int(input("COLOQUE Ate quanto ira o numero secreto:  "))
chances = int(input("quantas chances voce quer?  "))
NumSecreto = random.randint(1,maximo)
Numescolhido = int(input("escolha um numero de 1 a  " + str(maximo)+ ": " ))
while chances > 0: 
    chances -= 1
    if chances == 0:
        print ("perdeu")
    elif Numescolhido > NumSecreto:
        Numescolhido = int(input("escolha um numero denovo. tenha em mente que o numero e menor que este.  "))
    elif Numescolhido == NumSecreto:
        print ("acertou cara.")
        chances = 0
    else:
        Numescolhido = int(input("escolha um numero denovo. tenha em mente que o numero e maior que este.  "))

    
