print("Bem Vindo!\nConverta valores de kilometros para milhas e milhas para kilometros")

kilometers = int(input("Insira o valor do kilometro: "))
miles = int(input("Insira o valor da milha: "))

miles_to_kilometers = round(miles * 1.609)
kilometers_to_miles = round(kilometers // 1.609)

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")
