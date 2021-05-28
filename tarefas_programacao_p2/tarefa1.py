

#A função recursiva mediaDeInteiros foi cria para resolver esta tarefa



def mediaDeInteiros(InteirosRecebidos):
    entrada = input()
    #Verifica se a entrada é um inteiro
    if entrada.isdigit():
        #Adiciona a entrada à lista de inteiros já recebidos
        InteirosRecebidos.append(int(entrada))
        #chamada da recursiva função com a lista atualizada
        return mediaDeInteiros(InteirosRecebidos)
    #Verifica se a entrada é a string f
    elif entrada == "f":
        #retorna a média se não estiver vazia
        return 0 if len(InteirosRecebidos) == 0 else sum(InteirosRecebidos)/len(InteirosRecebidos)
    #Verifica uma entrada inválida
    else:
        #chamada da recursiva função sem atualizar a lista
        return mediaDeInteiros(InteirosRecebidos)


#A função começa com uma lista vazia
print(mediaDeInteiros([]));