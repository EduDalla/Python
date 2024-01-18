lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number #acumula o número e volta para o começo somando
    lst_2.append(add) # e colocando na lista

print(lst_2)

# Resultado 1, 3, 6, 10, 15 (o 1º é 1 pq o add = 0)