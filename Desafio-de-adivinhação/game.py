import random
numero_aleatorio = random.randint(1, 100)
palpite = input("Digite um número entre 1 e 100: ")
if int(palpite) == numero_aleatorio:
    print("Parabéns, você acertou!")
else:
    print("Que pena, você errou!")
acertou = False
while not acertou:
    palpite = input("Digite um número entre 1 e 100: ")
    if int(palpite) == numero_aleatorio:
        print("Parabéns, você acertou!")
        acertou = True
    else:
        print("Que pena, você errou! Tente novamente.")

