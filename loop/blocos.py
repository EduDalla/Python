blocks = int(input("Insira o número de blocos: "))

altura = 0
while blocks > altura: # verifica se o número de blocos é maior que a altura
    altura += 1 # aumentar altura
    blocks -= altura # subtrai o valor de blocos pela altura

print("A altura da pirâmide:", altura)

# Código alternativo

# blocks = int(input("Insira o número de blocos: "))
#
# altura = 0
# while blocks > altura: # analiza se o número de blocos é maior que a altura
#     blocks -= altura # subtrai o valor de blocos pela altura
#     if altura == blocks: # se a altura for maior que blocos, o cógigo para
#         break
#     else: # caso o contrário adicione mais uma camada
#         altura += 1
#
# print("A altura da pirâmide:", altura)