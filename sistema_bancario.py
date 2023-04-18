# Criar funções de depósito, saque e extrato
# Depósito:
# todos os depósitos devem ser armazenados na variável saldo e registrados na variável extrato
#
# Saque:
# 3 por dia
# Max 500 reais por saque
# Mensagem de impossibilidade de saque por falta de saldo
# Todos os saques devem ser armazenados e exibidos na operação extrato
#
# Extrato:
#  Listar depósitos e saques, com o saldo atual da conta ao final no formato R$ XXX.XX

header = " BEM-VINDO AO BANCO "
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 1000.00
LIMITE = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print(header.center(30, "="))

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        print("Depósito")
        while True: 
            deposito = input("Qual o valor que será depositado? ")
            try:
                deposito = float(deposito)
                if (deposito > 0):
                    saldo += deposito
                    extrato += f"\nDEPÓSITO + R$ {deposito:.2f}"
                    print(f"Seu saldo agora é de R$ {saldo:.2f}")
                    break
                else:
                    print("O valor do depósito deve ser positivo!")
            except ValueError:
                if (deposito.lower() == "q"):
                    break
                else:
                    print("Insira um valor ou tecle q para voltar ao menu anterior!")
    
    elif opcao == "s":
        if (numero_saques >= LIMITE_SAQUES):
            print("Você já realizou todos os saques diários disponíveis!")
        else:
            print("Saque")
            print(f"Saques diários restantes: {LIMITE_SAQUES - numero_saques}")
            print(f"Valor máximo por saque: R$ {LIMITE}")
            while True:
                saque = input("Qual o valor do saque? R$ ")
                try:
                    saque = float(saque)
                    if (saque <= 0):
                        print("Não é possível sacar valor negativo!")
                    elif (saque > saldo):
                        print(f"Saque não permitido! Valor superior ao saldo disponível.")
                    elif (saque > LIMITE):
                        print(f"Saque não permitido! Valor máximo para saque: R$ {LIMITE}")
                    elif(numero_saques >= LIMITE_SAQUES):
                        print("Você já realizou todos os saques diários disponíveis!")
                    elif (saldo >= saque):
                        numero_saques += 1
                        saldo-= saque
                        extrato += f"\nSAQUE - R$ {saque:.2f}"
                        print("Saque realizado com sucesso!")
                        break
                except ValueError:
                    if (saque.lower() == "q"):
                        break                    
                    else:
                        print("Insira um valor ou tecle q para voltar ao menu anterior")

    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print()
        print(f" SALDO DISPONÍVEL: R$ {saldo} ".center(50, "="))
    
    elif opcao == "q":
        print(" O BANCO AGRADECE A SUA PREFERÊNCIA! ".center(50, "="))
        break
    
    else:
        print("OPERAÇÃO INVÁLIDA! Por favor selecione a operação desejada dentre as opções disponíveis.")
