from tabulate import tabulate
# Q1
# Alunos:
# Pedro Vinicius Morais Silva de Albuquerque
# Maria Vitoria da Silva
#
# 1. Cadastrar CPF
# 2. Adcionar um endereço MAC a um CPF
# 3. Remover um endereço MAC de um CPF
# 4. Remover um CPF
# 5. Listar os CPF cadastrados
# 6. Listar os MACs vinculados a um CPF
# 7. Salvar o banco de dados em um arquvio (perguntar o nome do arquivo)
# 8. Ler o banco de dados de um arquivo (perguntar o nome do arquivo)

BANNER = r"""
 __       __   ______    ______         __       __  ________  __    __  __    __       
|  \     /  \ /      \  /      \       |  \     /  \|        \|  \  |  \|  \  |  \      
| $$\   /  $$|  $$$$$$\|  $$$$$$\      | $$\   /  $$| $$$$$$$$| $$\ | $$| $$  | $$      
| $$$\ /  $$$| $$__| $$| $$   \$$      | $$$\ /  $$$| $$__    | $$$\| $$| $$  | $$      
| $$$$\  $$$$| $$    $$| $$            | $$$$\  $$$$| $$  \   | $$$$\ $$| $$  | $$      
| $$\$$ $$ $$| $$$$$$$$| $$   __       | $$\$$ $$ $$| $$$$$   | $$\$$ $$| $$  | $$      
| $$ \$$$| $$| $$  | $$| $$__/  \      | $$ \$$$| $$| $$_____ | $$ \$$$$| $$__/ $$      
| $$  \$ | $$| $$  | $$ \$$    $$      | $$  \$ | $$| $$     \| $$  \$$$ \$$    $$      
 \$$      \$$ \$$   \$$  \$$$$$$        \$$      \$$ \$$$$$$$$ \$$   \$$  \$$$$$$       
                                                                                        
"""
banco = {}

def validar_cpf(cpf: str):
    if type(cpf) != str:
        return False
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf.isdecimal() == False:
        print("\nDigite apenas números!")
        return False
    if len(cpf) != 11:
        print("\nUm CPF precisa ter 11 dígitos!")
        return False
    
    soma = 0
    for pos in range (9):
        soma += int(cpf[pos]) * (10 - pos)
    dv1 = 11 - soma % 11
    if dv1 >= 10: 
        dv1 = 0
        
    if dv1 != int(cpf[9]):
        print("\nCPF inválido.")
        return False
    
    soma = 0
    for pos in range (10):
        soma += int(cpf[pos]) * (11 - pos)
    dv2 = 11 - soma % 11

    if dv2 >= 10: 
        dv2 = 0
    if dv2 != int(cpf[10]):
        print(f"\nCPF inválido.")
        return False
        
    return True

def continuar(opcao: str): 
    global inicio
    if opcao == "n":
        print("\nRetornando ao menu principal...")
        inicio = False
        return False
    elif opcao != "y":
        print("\nOpção inválida.")
        inicio = False
        return False
    return True


def cadastrar_cpf():
    global inicio
    while True:
        cpf = input("\nInforme um CPF (apenas números)> ")
        if not validar_cpf(cpf): #valida o cpf, se for inválido, reinicia o loop para adicionar um CPF válido
            continue
        if cpf in banco: #verifica se o cpf já existe no dicionário banco
            print("\nCPF já cadastrado no banco de dados!")
            continue
        else: #se o cpf não existir, adiciona ao dicionário com uma lista vazia
            banco[cpf] = []
            print("\nCPF Cadastrado com sucesso!")
            
        opcao = input("\nDeseja cadastrar outro CPF? [Y/n]> ").strip().lower() # da a opção de continuar
        if not continuar(opcao):
            return


def cadastrar_mac(): #vincula um endereço MAC a um cpf existente
    global inicio
    while True:
        cpf = input("\nInforme um CPF (apenas números)> ") #valida o cpf e continua o loop se for invalido
        if not validar_cpf(cpf):
            continue 
        if cpf not in banco: #verifica se o cpf esta cadastrado no banco
            print("\nCPF não encontrado, tente novamente...")
            continue
        mac = input("\nDigite o endereço MAC> ").strip()

        if mac in banco[cpf]: #verifica se o endereço MAC ja esta na lista do cpf
            print("\nMAC já cadastrado para esse CPF!")
        else: #adiciona o endereço mac a lista do cpf correspondente
            banco[cpf].append(mac.upper()) 
            print(f"\nO endereço MAC: {mac} foi cadastrado e vinculado ao CPF {cpf}")
            opcao = input("\nDeseja adicionar outro MAC? [Y/n]> ").strip().lower()
            if not continuar(opcao):
                return


def remover_mac():
    global inicio
    while True:
        cpf = input("\nInforme um CPF (apenas números)> ")
        if not validar_cpf(cpf):
            continue
        if cpf not in banco:
            print("\nCPF não encontrado, tente novamente...")
            continue
        mac = input("\nDigite o endereço MAC para remover> ").strip().upper()
        if mac in banco[cpf]:
            banco[cpf].remove(mac)
            print("\nEndereço MAC removido com sucesso!")
            opcao = (
                input("\nDeseja remover outro endereço MAC? [Y/n]> ").strip().lower()
            )
            if not continuar(opcao):
                return
        else:
            print("\nEndereço MAC não encontrado :(")
            return


def remover_cpf():
    global inicio
    while True:
        cpf = input("\nInforme o CPF para remover (apenas números)> ")
        if not validar_cpf(cpf):
            continue
        if cpf not in banco:
            print("\nCPF não encontrado, tente novamente...")
            continue
        if banco[cpf]:
            print("\nNão é possível remover CPFs com endereços MAC vinculados.")
            continue
        else:
            del banco[cpf]
            print("\nCPF removido com sucesso.")
            opcao = input("\nDeseja remover outro CPF? [Y/n]> ")
            if not continuar(opcao):
                return


def listar_cpfs():
    global inicio
    while True:
        if not banco:
            print("\nNenhum CPF cadastrado no banco.")
            return
        else:
            tabela = [[i + 1, cpf] for i, cpf in enumerate(banco.keys())]
            titulo = ["#", "CPF"]
            print(tabulate(tabela, headers=titulo, tablefmt="grid"))
            return


def listar_mac():
    global inicio
    while True:
        cpf = input("\nInforme um CPF (apenas números)> ")
        if not validar_cpf(cpf):
            continue
        if not banco:
            print("\nNenhum cpf cadastrado no banco de dados.")
            return
        if cpf not in banco:
            print("\nCPF não encontrado, tente novamente...")
            continue
        if not banco[cpf]:
            print("\nNenhum endereço MAC encontrado para esse CPF")
            return
        tabela = [[i + 1, mac] for i, mac in enumerate(banco[cpf])]
        titulo = ["#", "Endereço MAC"]
        print(f"\nEndereços MAC vinculados ao cpf> {cpf}")
        print("\n", tabulate(tabela, headers=titulo, tablefmt="grid"))
        return


def salvar_arquivo():
    nome = input("\nInforme o nome do arquivo .txt que será gerado> ").strip()

    if not nome.lower().endswith(".txt"):
        nome += ".txt"
    try:
        with open(nome, "w") as fd:
            for cpf, macs in banco.items():
                linha = f"{cpf}|{' - '.join(macs)}\n"
                fd.write(linha)
        print(f"\nArquivo de texto gerado com sucesso -> {nome}.")
    except Exception as e:
        print(f"\nErro durante o salvamento do arquivo> {e}")


def carregar_arquivo():
    nome = input("\nInforme o nome do arquivo de texto para ser lido> ").strip()

    try:
        with open(nome, "r") as fd:
            global banco
            banco = {}
            for linha in fd:
                cpf, macs_aux = linha.strip().split("|")
                if macs_aux:
                    macs = macs_aux.split(" - ")
                else:
                    macs = []
                banco[cpf] = macs
        print("\nArquivo carregado com sucesso.")
    except FileNotFoundError:
        print("\nArquivo não encontrado.")
        return
    except Exception as e:
        print(f"\nErro ao carregar o arquivo> {e}")


inicio = True

def menu():
    while True:
        try:
            global inicio
            if inicio:
                print(BANNER)
            print("\nMenu para cadastramento de MAC address")
            print("\nDigite o menu que deseja acessar:\n")
            print("   1 - Cadastrar CPF")
            print("   2 - Adicionar um endereço MAC a um CPF")
            print("   3 - Remover um endereço MAC de um CPF")
            print("   4 - Remover CPF")
            print("   5 - Listar CPFs cadastrados.")
            print("   6 - Listar MACs vinculados a um CPF")
            print("   7 - Salvar banco de dados")
            print("   8 - Ler um banco de dados")
            print("   0 - Fechar o programa\n")

            opcao = input("Escolha uma opção> ")

            match opcao:
                case "1":
                    cadastrar_cpf()
                case "2":
                    cadastrar_mac()
                case "3":
                    remover_mac()
                case "4":
                    remover_cpf()
                case "5":
                    listar_cpfs()
                case "6":
                    listar_mac()
                case "7":
                    salvar_arquivo()
                case "8":
                    carregar_arquivo()
                case "0":
                    print("\nFinalizando programa...")
                    break
                case _:
                    inicio = False
                    print("\nOpção inválida :(")
        except (KeyboardInterrupt, EOFError):
            print("\nAbortando... x_x")
            break


if __name__ == "__main__":
    menu()
