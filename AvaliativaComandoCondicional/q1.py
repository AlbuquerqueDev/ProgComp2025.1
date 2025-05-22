n = int(input("Digite um número de até 4 algarismos: "))

if n <= 10000:
    unidade = n % 10
    dezena = (n // 10) % 10
    centena = (n // 100) % 10
    milhar = (n // 1000) % 10

    soma = unidade + dezena + centena + milhar

    print("A soma dos algarismos é igual a:", soma)

else:
    print("Número inválido!")
