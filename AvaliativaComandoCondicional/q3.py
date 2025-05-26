import random

# Sorteia um número entre 1 e 100
numero_sorteado = random.randint(1, 100)

menor_numero = 1
maior_numero = 100
tentativas = 1

print("----------------------------")
print("Tentativa: ", tentativas)
print("O intervalo agora está entre: ", menor_numero, "a", maior_numero)
print("----------------------------")

palpite = int(input("Diga um número: "))

acerto = 0

if palpite == numero_sorteado:
    print("Parabéns, você acertou!")
    acerto = 1
if palpite < numero_sorteado:
    menor_numero = palpite + 1
else:
    maior_numero = palpite - 1

tentativas += 1

## tentativa 2

if acerto == 0:
    print("-------------------------")
    print("Tentativa: ", tentativas)
    print("O intervalo agora está entre: ", menor_numero, "a", maior_numero)
    print("-------------------------")

    palpite = int(input("Diga um número: "))

    if palpite == numero_sorteado:
        print("Parabéns, você acertou!")
        acerto = 1
    if palpite < numero_sorteado:
        menor_numero = palpite + 1
    else:
        maior_numero = palpite - 1

tentativas += 1

## tentativa 3

if acerto == 0:
    print("--------------------------")
    print("Tentativa: ", tentativas)
    print("O intervalo agora está entre: ", menor_numero, "a", maior_numero)
    print("--------------------------")

    palpite = int(input("Diga um número: "))

    if palpite == numero_sorteado:
        print("Parabéns, você acertou!")
        acerto = 1
    if palpite < numero_sorteado:
        menor_numero = palpite + 1
    else:
        maior_numero = palpite - 1

tentativas += 1

## tentativa 4

if acerto == 0:
    print("------------------------")
    print("Tentativa: ", tentativas)
    print("O intervalo agora está entre: ", menor_numero, "a", maior_numero)
    print("------------------------")

    palpite = int(input("Diga um número: "))

    if palpite == numero_sorteado:
        print("Parabéns, você acertou!")
        acerto = 1
        tentativas += 1
    if palpite < numero_sorteado:
        menor_numero = palpite + 1
    else:
        maior_numero = palpite - 1

print("Fim de jogo, você não acertou! O número sorteado era", numero_sorteado)
