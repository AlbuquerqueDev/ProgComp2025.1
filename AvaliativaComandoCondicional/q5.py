tempo = int(input("Digite o tempo em minutos: "))

total = 0

# Se o tempo for maior que 12 horas, cobre a taxa fixa de 30 Reais
if tempo >= 720:
    total = 30
else:
    # Converte o tempo para hora arredondando a casa decimal para cima caso exista resto na conversão
    if tempo % 60 > 0:
        tempo = int(tempo / 60)
        tempo += 1
    else:
        tempo = int(tempo / 60)

    # checagem para os outros preços
    if tempo <= 2:
        total = tempo * 8
    elif tempo <= 4:
        # (tempo - 2) é para subtrair a primeira cobrança acima.
        total = (2 * 8) + ((tempo - 2) * 5)
    else:
        total = (2 * 8) + (2 * 5) + ((tempo - 4) * 3)

print("Total a ser pago: ", total)
