n = int(input("Digite um número de até 4 algarismos: "))


if n <= 10000:
    # Pega a o dígito unitário do número
    unidade = n % 10
    # Pega o digito da dezena do número
    dezena = (n // 10) % 10
    # Pega o dígito da centena do número
    centena = (n // 100) % 10
    # Pega o dígito da milhar do número
    milhar = (n // 1000) % 10

    # Soma os algarismos
    soma = unidade + dezena + centena + milhar

    print("A soma dos algarismos é igual a:", soma)

else:
    print("Número inválido!")
