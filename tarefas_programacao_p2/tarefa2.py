"""     
    A função posicaoCavalo analisa se o movimento do cavalo, em um tabuleior 8x8, é válido.
    Vamos interpretar a posição no tabuleiro como uma coordenada do tipo (x, y). 
    Por exemplo, a posição d4 equivale à coordenada (4, 4), pois "d" é a quarta letra do alfabeto. 
    Assim, podemos afirmar que um movimento válido é aquele cujo módulo da difereça entre a posição inicial
    e a posição final é (1, 2) ou (2, 1).

"""


def posicaoCavalo(inicial, final):

    conversor_de_letras = {"a": 1, "b": 2, "c": 3, "d":4, "e":5, "f": 6, "g": 7, "h": 8}
    #Diferença entre as coordenadas em x
    diffx = abs(conversor_de_letras[inicial[0]] - conversor_de_letras[final[0]])

    #Diferença entre as coordenadas em y
    diffy =  abs(int(inicial[1]) -  int(final[1]))

    #Coordenada que representa a diferença em módulo
    diff_coordenadas = (diffx, diffy)

    if diff_coordenadas == (1, 2) or diff_coordenadas == (2, 1):
        return "VÁLIDO"
    else:
        return "INVÁLIDO"



inicial = input()
final = input()

print(posicaoCavalo(inicial, final))

    