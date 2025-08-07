# Pedro Vinicius Morais Silva de Albuquerque 20251014050038
# Maria Vitoria da Silva 20251014050001
def contar_palindromos():
    contador = 0
    for n in range(10, 100001):
        if palindromo(n):
            contador += 1
    return contador


def eh_palindromo(numero):
    numero_original = numero
    numero_palindromo = 0
    while numero > 0:
        digito = numero % 10
        numero_palindromo = (numero_palindromo * 10) + digito
        numero //= 10

    if numero_original == numero_palindromo:
        return True


quantidade = contar_palindromos()
print(f"Existem {quantidade} números palindromos entre 10 e 100000.")
