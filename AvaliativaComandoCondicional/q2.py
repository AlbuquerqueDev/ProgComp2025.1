n1 = int(input("Digite sua nota da primeira unidade: "))
n2 = int(input("Digite sua nota da segunda unidade: "))


# Calcula a media
md = (2 * n1 + 3 * n2) / 5

# Se a média for maior ou igual a 60... Aprovado
if md >= 60:
    print("Aprovado!")
# caso não se for maior ou igual a 20... Prova final!
elif md >= 20:
    print("Prova final\n")
    naf = int(input("Digite a nota obtida na prova final: "))
    mfd = (md + naf) / 2

    # Se a nota da prova final for maior ou igual a 60... Aprovado!
    if mfd >= 60:
        print("Aprovado!")
    # Caso não... Reprovado.
    else:
        print("Reprovado!")
else:
    print("Reprovado!")
