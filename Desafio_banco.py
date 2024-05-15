menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

deposito = 0
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
movimentacao = 0
valor_saque = 0
saques = 0
valor_sacado = 0

extrato = ""


while True:

    opcao = input(menu)
    ###Depoisito
    if opcao == "1":
        deposito = input("Digite o valor a ser depositado na conta! ")
        saldo = saldo + float(deposito)
        movimentacao += 1
    ###Saque
    elif opcao == "2":

        valor_saque = float(input("Digite o Valor a ser sacado! "))
        if saldo >= valor_saque:
            if numero_saques <= 3:
                saldo -= valor_saque
                valor_sacado += valor_saque
                saques += 1
                print("Saque Realizado com Sucesso")
            else:
                print("Numéro de Saques Excedidos")
        else:
            print("Saldo Insuficiente para Saque")
    # Extrato
    elif opcao == "3":
        if movimentacao != 0:
            print("\n############### Extrato ##############")
            print(f"\nLimite de Saque da Conta: {LIMITE_SAQUES}")
            print("Número de Saques da conta: %s" % (saques))
            print("Valor Sacado R$ %s" % (valor_sacado))
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("\n######################################")
        else:
            print("Erro Conta Zerada, favor fazer depositos")
    # Sair
    elif opcao == "0":
        break
    else:
        print("Operação Inválida, por favor selecione novamente a operação Desejada! ")
