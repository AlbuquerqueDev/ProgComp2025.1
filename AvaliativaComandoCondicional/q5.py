tempo = int(input("Digite o tempo em minutos: "))


total = 0


if tempo >= 720:
    total = 30
else:
    if tempo % 60 > 0:
        tempo = int(tempo / 60)
        tempo += 1
    else:
        tempo = int(tempo / 60)

    if tempo <= 2:
        total = tempo * 8
    elif tempo <= 4:
        total = (2 * 8) + ((tempo - 2) * 5)
    else:
        total = (2 * 8) + (2 * 5) + ((tempo - 4) * 3)

print("Total a ser pago: ", total)
