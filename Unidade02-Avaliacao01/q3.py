# Pedro Vinicius Morais Silva de Albuquerque 20251014050038
# Maria Vitoria da Silva 20251014050001
import random


BANNER = r"""
 ______   _   _   _____   _____   _____
 |  _  \ | | | | |  ___| |_   _| |  _  |
 | | | | | | | | | |__     | |   | | | |
 | | | | | | | | |  __|    | |   | | | |
 | |/ /  | |_| | | |___    | |   \ \_/ /
 |___/    \___/  \____/    \_/    \___/
"""

# Dicionário com as mensagens finais.
# chave: quantidade de tentativas
# valores: mensagens das respectivas tentativas
mensagem_final = {
    1: "Impossível",
    2: "Ninja",
    3: "Impressionante",
    4: "Interessante",
    5: "Pode melhorar",
    6: "Foi por pouco",
}

palavras = (
    "ADAGA",
    "ADUBO",
    "AMIGO",
    "ANEXO",
    "ARAME",
    "ARARA",
    "ARROZ",
    "ASILO",
    "ASTRO",
    "BAILE",
    "BAIXA",
    "BALAO",
    "BALSA",
    "BARCO",
    "BARRO",
    "BEIJO",
    "BICHO",
    "BORDA",
    "BORRA",
    "BRAVO",
    "BREJO",
    "BURRO",
    "CAIXA",
    "CALDO",
    "CANJA",
    "CARRO",
    "CARTA",
    "CERVO",
    "CESTA",
    "CLIMA",
    "COBRA",
    "COLAR",
    "COQUE",
    "COURO",
    "CRAVO",
    "DARDO",
    "FAIXA",
    "FARDO",
    "FENDA",
    "FERRO",
    "FESTA",
    "FLUOR",
    "FORCA",
    "FORNO",
    "FORTE",
    "FUNDO",
    "GAITA",
    "GARRA",
    "GENIO",
    "GESSO",
    "GRADE",
    "GRANA",
    "GRAMA",
    "GURIA",
    "GREVE",
    "GRUTA",
    "HEROI",
    "HOTEL",
    "ICONE",
    "IMPAR",
    "IMUNE",
    "INDIO",
    "JUNTA",
    "LAPIS",
    "LARVA",
    "LAZER",
    "LENTO",
    "LESTE",
    "LIMPO",
    "LIVRO",
    "MACIO",
    "MAGRO",
    "MALHA",
    "MANSO",
    "MARCO",
    "METAL",
    "MORTE",
    "MORRO",
    "MURAL",
    "MOVEL",
    "NACAO",
    "NINHO",
    "NOBRE",
    "NORMA",
    "NORTE",
    "NUVEM",
    "PACTO",
    "PALHA",
    "PARDO",
    "PARTE",
    "PEDRA",
    "PEDAL",
    "PEIXE",
    "PRADO",
    "PISTA",
    "POMBO",
    "POETA",
    "PONTO",
    "PRATO",
    "PRECO",
    "PRESO",
    "PROSA",
    "PRUMO",
    "PULGA",
    "PULSO",
    "QUEPE",
    "RAIVA",
    "RISCO",
    "RITMO",
    "ROSTO",
    "ROUPA",
    "SABAO",
    "SALTO",
    "SENSO",
    "SINAL",
    "SITIO",
    "SONHO",
    "SOPRO",
    "SURDO",
    "TARDE",
    "TERNO",
    "TERMO",
    "TERRA",
    "TIGRE",
    "TINTA",
    "TOLDO",
    "TORRE",
    "TRAJE",
    "TREVO",
    "TROCO",
    "TRONO",
    "TURMA",
    "URUBU",
    "VALSA",
    "VENTO",
    "VERDE",
    "VISAO",
    "VINHO",
    "VIUVO",
    "ZEBRA",
)

PADRAO = "\033[00m"
AMARELO = "\033[93m"
VERDE = "\033[92m"
CINZA = "\033[97m"


def checagem(palpite: str, segredo: str) -> str:
    """
    Função que percorre as letras do palpite, e compara com o segredo
    fazendo uma varredura para cada cor,
    verde: letra está na posição certa;
    amarelo: está na palavra mas na posição errada;
    cinza: não está na palavra;
    """

    # checa se o segredo já foi descoberto, (está vazio)
    if not segredo:
        # caso sim, retorna o palpite só que em cinza
        return "".join(CINZA + letra + PADRAO for letra in palpite)

    # String que irá ser retornada no final da função
    # ao final das checagens, a string saída terá
    # o palpite do usuiário porém com as letras coloridas
    saida = ""

    # enumerador que percorre o indice da letra (i) e a propria letra (letra) do palpite
    for i, letra in enumerate(palpite):
        # Caso a letra está no mesmo indice que o segredo...
        if letra == segredo[i]:
            # então adciona a letra, dessa vez verde, na string saida
            saida += VERDE + letra + PADRAO
        elif letra in segredo:  # se não se, a letra está na palavra...
            # então adiciona essa letra na cor amarela
            saida += AMARELO + letra + PADRAO
        else:
            saida += CINZA + letra + PADRAO  # adciona a letra na cor cinza
    return saida  # retorna uma string com as letras nas cores certas


def pegar_palpite() -> str:
    """
    Função que pega um palpite válido do usuário
    o loop é encerrado quando o usuário digita um palpite válido.
    """
    while True:
        palpite = input(f"\nDigite um palpite palpite> ").upper()

        # se o palpite tiver 5 caracteres e forem letras.
        if len(palpite) == 5 and palpite.isalpha():
            return palpite  # retorna o palpite
        print("\nPalpite inválido. (Digite 5 letras)")


def exibir_termo(tentativas):
    """
    Função que exibe a "tela" do termo, de 7 linhas e cada tentativa é linha1 e linha2
    tentativas é uma tupla que contém (linha1, linha2)
    """
    print()
    for i in range(7):  # Loop que representa cada linha do jogo.
        """
            Verifica se já existe uma tentativa feita para esta posição i
            len(tentativas_coloridas) é o número de palpites que já foram dados
            Se o índice i for menor que isso, significa que temos um palpite real para mostrar nessa linha
        """
        if i < len(tentativas):
            # extrai a tupla para as variaveis linha1 e linha2
            linha1, linha2 = tentativas[i]
            # exibe as linhas com os palpites armazenados em linha1 e linha2
            print(linha1 + " | " + linha2)
        else:  # Caso não exista uma tentativa
            bloco = CINZA + "_" + PADRAO  # cria um bloco "_"
            linha_vazia = bloco * 5  # cria uma linha composta por 5 blocos "_ _ _ _ _"
            print(linha_vazia + " | " + linha_vazia)  # exibe a linha vazia


def rodar_termo():
    """
    Função que "roda" o dueto
    """

    segredos = [
        random.choice(palavras),
        random.choice(palavras),
    ]  # cria uma lista com 2 segredos

    segredos_copia = segredos.copy()

    # Enquanto um segredo for igual o outro, ache outro segredo.
    while segredos[1] == segredos[0]:
        segredos[1] = random.choice(palavras)

    tentativas = []  # variavel que armazena as tentativas do usuário, uma lista de tuplas
    if not tentativas:
        print(BANNER)
    exibir_termo(tentativas)

    # repetição principal do jogo, que roda 7 vezes, uma para cada palpite
    for n_tentativas in range(1, 8):
        palpite = pegar_palpite()

        # montando as duas colunas coloridas
        linha1 = checagem(palpite, segredos[0])
        linha2 = checagem(palpite, segredos[1])
        tentativas.append((linha1, linha2))

        # se o usuário acertar o palpite, torne o segredo para vazio
        if palpite == segredos[0]:
            segredos[0] = ""
        if palpite == segredos[1]:
            segredos[1] = ""

        exibir_termo(tentativas)

        # se os dois estiverem vazios, então o usuário acertou os 2.
        if segredos[0] == "" and segredos[1] == "":
            print("\nDueto!")
            if n_tentativas in mensagem_final:
                print(mensagem_final[n_tentativas])
            return

    print("\nQue pena! :(")
    print(f"\nOs segredos eram: {segredos_copia[0]} e {segredos_copia[1]}")


# iniciando a função principal
if __name__ == "__main__":
    try:
        rodar_termo()
    except KeyboardInterrupt:
        print("\nFinalizando o jogo...")
