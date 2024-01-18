c0 =  int(input("Digite o número: "))

etapas = 0
# pegue qualquer número inteiro diferente de zero e diferente de zero e nomeie-o como c0;
while c0 != 1: # se c0 ≠ 1 , volte ao ponto 2.
    etapas += 1 # contar o número de etapas
    if c0 % 2 == 0: # se for par, avalie um novo c0 como c0 ÷ 2;
        c0 //= 2
    else:
        c0 = (c0 * 3) + 1 # caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;

    print(c0) # contagem de cada c0 que passa pelo loop até o 1

print("etapas = ", etapas)

