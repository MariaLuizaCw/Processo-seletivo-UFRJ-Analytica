""" A função abaixo retorna o número de vezes que uma certa palavra aparece em um arquivo txt """


def contadorDePalavras():
    #Abre o arquivo sem que ele perca os caracteres especiais
    arquivo = open("Texto.txt", 'r', encoding = 'utf8')
    #Divide o arquivo por linhas
    linhas = arquivo.read().split('\n')
    palavras = []
    quantidade_de_palavras = {} 
    for linha in linhas:
        #Divide o arquivo por palavras como todas letras minúsculas
        linha = linha.lower()
        palavras += linha.split(" ")
    for palavra in palavras:
        #Exclui o último caracter da string se ele não corresponde a uma letra
        ascii_ultima_letra = ord(palavra[-1]) 
        if ascii_ultima_letra < 97:
            palavra = palavra[0:-1]
        
        #Altera o valor da palavra no dicionário, somando 1
        if palavra in quantidade_de_palavras:
            quantidade_de_palavras[palavra] += 1
        #Adiciona a palavra no dicionário
        else:
            quantidade_de_palavras[palavra] = 1

    #imprime a palavra e o número de vezes que ela aparece
    for key, value in quantidade_de_palavras.items():
        print(f"{key}: {value}")


contadorDePalavras()