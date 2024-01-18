av = 5

candy = int(input("Quantos doces vc quer? "))

i = 1
while i <= candy:

    if i >= av:
        print("Fora de estoque")
        break

    print("Candy")
    i += 1

print("Bye")