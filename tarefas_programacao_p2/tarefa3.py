


"""
    Neste caso um algoritmo guloso é suficiente para resolver o problema. 
    A ideia é começar com as maiores notas, utilizando o maior número possível delas.
"""


def troco(valor):
    #Opções de notas e moedas listadas em ordem decrescente
    opcoes_notas = [100, 50, 20, 10, 5, 2]
    opcoes_moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    #Iteração sobre cada opção de nota
    for nota in opcoes_notas:
        cont_nota = 0 
        #Subtrai a nota atual do valor enquanto for possível 
        while (valor - nota > 0):
            valor -= nota
            cont_nota += 1 #Conta o número de notas daquele tipo utilizadas
        print(f"{cont_nota} nota(s) de R$ {nota:.2f}")
    #Iteração sobre cada opção de moeda
    for moeda in opcoes_moedas:
        cont_moeda = 0
        #Subtrai a moeda atual do valor enquanto for possível 
        while (valor - moeda > 0):
            valor -= moeda
            cont_moeda += 1 #Conta o número de moedas daquele tipo utilizadas
        print(f"{cont_moeda} moeda(s) de R$ {moeda:.2f}")


valor = float(input())
troco(valor)