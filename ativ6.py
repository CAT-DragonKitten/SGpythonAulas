LiamNota1 = float(input("digite sua nota   "))
LiamNota2 = float(input("digite sua nota   "))
LiamNota3 = float(input("digite sua nota   "))
if ((LiamNota1 + LiamNota2 + LiamNota3) / 3) == 10.0:
    print ("A de novo... Passou, com merito...")
elif ((LiamNota1 + LiamNota2 + LiamNota3) / 3) >= 9.0:
    print ("CONSEGUIU UM A!? Passou!")
elif ((LiamNota1 + LiamNota2 + LiamNota3)) / 3 >= 8.0:
    print ("B... meh nota meia boca...notas ruins, mas eu fui aprovado")
elif ((LiamNota1 + LiamNota2 + LiamNota3)) / 3 >= 7.0:
    print ("C... passei raspando... aprovddo como um desempregado")
elif ((LiamNota1 + LiamNota2 + LiamNota3)) / 3 >= 6.0:
    print ("D... passei na sorte... aprovei na sorte")
elif ((LiamNota1 + LiamNota2 + LiamNota3)) / 3 >= 5.0:
    print ("F... virar youtuber... aprovado de forma horrenda")
else:
    print ("F... reprovei..... vou pedir esmola")
