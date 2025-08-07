# Pedro Vinicius Morais Silva de Albuquerque 20251014050038
# Maria Vitoria da Silva 20251014050001
import random


# BANNER = r"""
# ______   _   _   _____   _____   _____
# |  _  \ | | | | |  ___| |_   _| |  _  |
# | | | | | | | | | |__     | |   | | | |
# | | | | | | | | |  __|    | |   | | | |
# | |/ /  | |_| | | |___    | |   \ \_/ /
# |___/    \___/  \____/    \_/    \___/
# """
#

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

tentativas = []
segredo1 = random.choice(palavras)
segredo2 = random.choice(palavras)

inicio = True
# Impede que os segredos sejam iguais
while segredo2 == segredo1:
    segredo2 = random.choice(palavras)

PADRAO = "\033[00m"
AMARELO = "\033[93m"
VERDE = "\033[92m"
CINZA = "\033[97m"


def checagem(palpite, segredo):
    if not segredo:
        return [CINZA + letra + PADRAO for letra in palpite]

    saida = ["", "", "", "", ""]
    letras_segredo = list(segredo)

    # checa letras verdes
    for i in range(5):
        if palpite[i] == letras_segredo[i]:
            saida[i] = VERDE + palpite[i] + PADRAO
            letras_segredo[i] = None

    # checa letras amarelas
    for i in range(5):
        if saida[i] != "":
            letra_palpite = palpite[i]
            if letra_palpite in letras_segredo:
                saida[i] = AMARELO + letra_palpite + PADRAO
                letras_segredo[letras_segredo.index(letra_palpite)] = None
            else:
                saida[i] = CINZA + letra_palpite + PADRAO
    return saida


def exibir_termo(tentativas):
    print()
    for i in range(7):
        if i < len(tentativas):
            linha1, linha2 = tentativas[i]
            print("".join(linha1) + " | " + "".join(linha2))
        else:
            linha_vazia = CINZA + "_" + PADRAO
            linha_vazia_aux = "".join([linha_vazia] * 5)
            print(linha_vazia_aux + " | " + linha_vazia_aux)

    print("\n\nPara debug:")
    print(f"{AMARELO}texto em amarelo{PADRAO}")
    print(f"{VERDE}texto em verde{PADRAO}")
    print(f"{CINZA}texto em cinza{PADRAO}")
    print(f"Segredo 1: {segredo1}")
    print(f"Segredo 2: {segredo2}")


ganhou = False
for tentativa in range(1, 8):
    # print(BANNER)
    exibir_termo(tentativas)

    while True:
        palpite = input(f"Digite seu {tentativa}º palpite> ").strip().upper()
        if len(palpite) != 5:
            print("\nA palavra precisa ter 5 letras!")
        elif palpite not in palavras:
            print("\nPalavra inválida.")
        else:
            break

    linha1 = checagem(palpite, segredo1)
    linha2 = checagem(palpite, segredo2)
    tentativas.append((linha1, linha2))

    acertou1 = palpite == segredo1
    acertou2 = palpite == segredo2

    if acertou1 and acertou2:
        exibir_termo(tentativas)
        print("\nDueto!")

        if tentativa <= 6:
            print(mensagem_final[tentativa])
        ganhou = True
        break
    elif acertou1 or acertou2:
        if acertou1:
            segredo1 = ""
        if acertou2:
            segredo2 = ""
        if segredo1 == "" and segredo2 == "":
            exibir_termo(tentativas)
            print("\nDueto!")
            ganhou = True
            break
if not ganhou:
    print("\nQue pena! :(")
    print(f"As palavras eram: {segredo1} e {segredo2}")
