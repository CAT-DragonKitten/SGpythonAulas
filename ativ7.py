NumSecreto = 2
Numescolhido = int(input( "escolha um numero de 1 a 10,  "))
while Numescolhido != NumSecreto:
    if Numescolhido < NumSecreto:
        print ("e maior.")
        Numescolhido = int(input("escolha outro Numero  "))
    elif Numescolhido > NumSecreto:
        print ("e menor.")
        Numescolhido = int(input("escolha outro Numero  "))
if NumSecreto == Numescolhido:
    print ("acertou mizeravi")
