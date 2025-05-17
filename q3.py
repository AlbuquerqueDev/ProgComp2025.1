import random

# Sorteia um número entre 1 e 100
numero_sorteado = random.randint(1, 100)

menor_numero = 1
maior_numero = 100
tentativas = 0
palpite = 0

while tentativas < 4:
    print("----------------------------")
    print("Tentativa: ", tentativas + 1)
    print("O intervalo agora está entre: ", menor_numero, "a", maior_numero)
    print("----------------------------")

    palpite = int(input("Diga um número:"))

    if palpite == numero_sorteado:
        print("Parabéns, você acertou!")
    if palpite < numero_sorteado:
        menor_numero = palpite + 1
        print()
        print("----------------------------")
        print("O número está entre:", menor_numero, "a", maior_numero)
        print("----------------------------")
    else:
        maior_numero = palpite - 1
        print("----------------------------")
        print("O número está entre:", menor_numero, "a", maior_numero)
        print("----------------------------")
    tentativas += 1

print("Você não acertou, o número era: ", numero_sorteado)
