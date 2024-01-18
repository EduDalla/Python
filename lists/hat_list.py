hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.

 # Etapa 1: escreva uma linha de código que solicita ao usuário
# que substitua o número do meio por um número inteiro inserido pelo usuário.
x = int(input("Digite o número inteiro para substituir no número do meio: "))
hat_list[2] = x

# Etapa 2: escreva uma linha de código que remova o último elemento da lista.
del hat_list[4]
 # Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual

print (hat_list) 