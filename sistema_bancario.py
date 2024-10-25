home = """
[d] Depositar
[s] Sacar
[e] Extrato
[z] Sair

"""

saldo = 0
limite = 500
saques_hoje = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    opcao = input(home)

    # Operação de Depósito
    if opcao == 'd':
        valor = float(input("Valor do Depósito: R$"))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido! Depósitos devem ser maiores que zero.")
        
    # Operação de Saque
    elif opcao == 's':
        if saques_hoje >= LIMITE_SAQUES:
            print("O limite de saques diários foi atingido!") 
        else:
            valor = float(input("Valor a ser sacado: R$"))
            if valor > saldo:
                print("Saldo insuficiente!")
            elif valor > limite:
                print("O valor ultrapassa o limite diário de saque!")
            elif valor > 0:
                saldo -= valor
                extrato += f'Saque: R${valor:.2f}\n'
                saques_hoje += 1
                print("Saque realizado com sucesso!")
            else:
                print("Valor inválido! Saques devem ser maiores que zero.")

    # Operação de Extrato
    elif opcao == 'e':
        print("\n=====> EXTRATO <===== \n")
        print(extrato if extrato else "Nenhuma movimentação registrada!")
        print(f'\nSaldo atual: R${saldo:.2f}\n')
    
    # Sair
    elif opcao == 'z':
        print("Agradecemos a preferência, volte sempre!")
        break
    
    # Opção inválida
    else:
        print("Opção inexistente! Selecione uma operação válida.")