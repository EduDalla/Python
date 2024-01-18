year = int(input("Digite um ano: "))

ano_comum = 0
ano_bissexto = 0

if year < 1582:
    print("Não dentro do período do calendário gregoriano")
else:
    if (year % 4) != 0:
        print("Comum")

    elif (year % 100) != 0:
        print("Bissexto")

    elif (year % 400) != 0:
        print("Comum")

    else:
        print("bissexto")