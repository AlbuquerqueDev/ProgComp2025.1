import math

minutos = int(input("Digite o tempo em minutos: "))

hora = math.ceil(minutos / 60)

total = 0

if hora >= 12:
    total = 30

if hora <= 2:
    total = hora * 8
elif hora <= 4:
    total = (2 * 8) + ((hora - 2) * 5)
else:
    total = (2 * 8) + (2 * 5) + ((hora - 4) * 3)

print("Total a ser pago: ", total)
