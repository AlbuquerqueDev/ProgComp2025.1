# Variáveis para cada mês do ano
dias_jan = 31
dias_fev = 28
dias_mar = 31
dias_abr = 30
dias_mai = 31
dias_jun = 30
dias_jul = 31
dias_ago = 31
dias_set = 30
dias_out = 31
dias_nov = 30
dias_dez = 31

dia1 = int(input("Digite o dia da data inicial: "))
mes1 = int(input("Digite o mês da data inicial: "))

dia2 = int(input("Digite o dia da data final: "))
mes2 = int(input("Digite o mês da data final: "))

# Verifica se o mês está entre 1 e 12
if mes1 < 1 or mes1 > 12 or mes2 < 1 or mes2 > 12:
    print("Mês inválido!")
else:
    # Verifica se o dia é válido para o mês e atribui para uma variável max_dia
    if mes1 == 1:
        max_dia1 = dias_jan
    elif mes1 == 2:
        max_dia1 = dias_fev
    elif mes1 == 3:
        max_dia1 = dias_mar
    elif mes1 == 4:
        max_dia1 = dias_abr
    elif mes1 == 5:
        max_dia1 = dias_mai
    elif mes1 == 6:
        max_dia1 = dias_jun
    elif mes1 == 7:
        max_dia1 = dias_jul
    elif mes1 == 8:
        max_dia1 = dias_ago
    elif mes1 == 9:
        max_dia1 = dias_set
    elif mes1 == 10:
        max_dia1 = dias_out
    elif mes1 == 11:
        max_dia1 = dias_nov
    elif mes1 == 12:
        max_dia1 = dias_dez

    if mes2 == 1:
        max_dia2 = dias_jan
    elif mes2 == 2:
        max_dia2 = dias_fev
    elif mes2 == 3:
        max_dia2 = dias_mar
    elif mes2 == 4:
        max_dia2 = dias_abr
    elif mes2 == 5:
        max_dia2 = dias_mai
    elif mes2 == 6:
        max_dia2 = dias_jun
    elif mes2 == 7:
        max_dia2 = dias_jul
    elif mes2 == 8:
        max_dia2 = dias_ago
    elif mes2 == 9:
        max_dia2 = dias_set
    elif mes2 == 10:
        max_dia2 = dias_out
    elif mes2 == 11:
        max_dia2 = dias_nov
    elif mes2 == 12:
        max_dia2 = dias_dez

    # Validação dos dias
    if dia1 < 1 or dia1 > max_dia1 or dia2 < 1 or dia2 > max_dia2:
        print("Dia inválido!")
    else:
        # Verifica se a data final é posterior à inicial
        if mes2 < mes1 or (mes2 == mes1 and dia2 < dia1):
            print("A data final deve ser posterior à inicial.")
        else:
            # Soma os dias entre as duas datas
            dias_passados = 0
            mes = mes1
            while mes < mes2:
                # Se eu não usar esse while aqui o código fica estupidamente grande...
                if mes == 1:
                    dias_passados = dias_passados + dias_jan
                elif mes == 2:
                    dias_passados = dias_passados + dias_fev
                elif mes == 3:
                    dias_passados = dias_passados + dias_mar
                elif mes == 4:
                    dias_passados = dias_passados + dias_abr
                elif mes == 5:
                    dias_passados = dias_passados + dias_mai
                elif mes == 6:
                    dias_passados = dias_passados + dias_jun
                elif mes == 7:
                    dias_passados = dias_passados + dias_jul
                elif mes == 8:
                    dias_passados = dias_passados + dias_ago
                elif mes == 9:
                    dias_passados = dias_passados + dias_set
                elif mes == 10:
                    dias_passados = dias_passados + dias_out
                elif mes == 11:
                    dias_passados = dias_passados + dias_nov
                elif mes == 12:
                    dias_passados = dias_passados + dias_dez
                mes = mes + 1

            # Subtrai o dia inicial e soma o dia final
            dias_passados = dias_passados - dia1 + dia2
            print("Dias decorridos entre as datas:", dias_passados)
