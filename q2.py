n1 = int(input("Digite sua nota da primeira unidade: "))
n2 = int(input("Digite sua nota da segunda unidade: "))


md = (2 * n1 + 3 * n2) / 5

if md >= 60:
    print("Aprovado!")
elif md >= 20:
    print("Prova final\n")
    naf = int(input("Digite a nota obtida na prova final: "))
    mfd = (md + naf) / 2
    if mfd >= 60:
        print("Aprovado!")
    else:
        print("Reprovado!")
else:
    print("Reprovado!")
