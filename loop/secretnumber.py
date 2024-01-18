secret_number = 777

print(
    """
    +===================================+
    | Bem vindo ao meu jogo, trouxa!    |
    | Insira um número inteiro          |
    | e adivinhar o número que tenho    |
    | escolhidos para você.             |
    | Então, qual é o número secreto?   |
    +===================================+
    """)

a = int(input("Digite um número secreto: "))

while a != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    a = int(input("Insira novamente, trouxa: "))

print("Muito bem, trouxa! Você está livre agora.")