import textwrap

AGENCIA = "0001"
usuarios = []
contas = []
numero_conta_sequencial = 1

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Usuário
[n] Nova Conta
[q] Sair

=> """

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário já cadastrado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def cadastrar_conta_bancaria(usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    
    if usuario:
        global numero_conta_sequencial
        contas.append({"agencia": AGENCIA, "numero_conta": numero_conta_sequencial, "usuario": usuario})
        print(f"Conta criada com sucesso! Agência: {AGENCIA} Conta: {numero_conta_sequencial}")
        numero_conta_sequencial += 1
    else:
        print("Usuário não encontrado! Cadastro da conta não realizado.")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$"))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$"))
        saldo, extrato, numero_saques = saque(
            saldo=saldo, valor=valor, extrato=extrato, limite=limite, 
            numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        cadastrar_usuario(usuarios)

    elif opcao == "n":
        cadastrar_conta_bancaria(usuarios, contas)

    elif opcao == "q":
        print("Agradecemos a preferência, volte sempre!\n")
        break

    else:
        print("Opção inexistente! Selecione uma operação válida.\n")