#declara a variável saldo
saldo = 0 

#cria uma lista para armazenar os depósitos
depositos = []

#cria uma lista para armazenar os saques
saques = [] 

#declara o saldo diário do usuário
saldo_diario = 0

#declara a variável que armazena a quantidade de saques realizados
saques_diarios = 0

limite_diario = 1500

limite_saque = 500

while True:
    print('\nMENU:')
    print('1. Depósito')
    print('2. Saque')
    print('3. Extrato')
    print('4. Sair')

    opcao = int(input('Escolha uma opção (1-4): '))

    if opcao == 1: #Depósito
        valor_deposito = float(input('Digite o valor do depósito: '))
        if valor_deposito > 0:
            saldo += valor_deposito

            #adiciona os valores de depósito à lista depositos
            depositos.append(valor_deposito)
            
            print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!')
        else:
            print('O valor do depósito deve ser positivo')

    elif opcao == 2: #Saque
        valor_saque = float(input('Digite o valor do saque: '))
        if saldo_diario + valor_saque > limite_diario:
            print(f'Limite diário de saque atingido. Máximo de R$ {limite_diario:.2f} por dia')

        elif valor_saque > 0 and saldo >= valor_saque <= limite_saque:
            saldo -= valor_saque
            saldo_diario += valor_saque

            saques.append(valor_saque)
            saques_diarios +=1

            print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso.')

        elif saldo < valor_saque:
            print('Saldo insuficiente.')
        
        elif valor_saque > limite_saque:
            print(f'Valor máximo por saque é de R$ {limite_saque:.2f}.')
    
    elif opcao == 3: #Extrato
        print('Extrato: ')
        if not depositos and not saques:
            print('Não foram realizadas movimentações.')
        
        else:
            for deposito in depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in saques:
                print(f'Saque: R$ {saque:.2f}')
        
        print(f'Saldo atual: R${saldo:.2f}')

    elif opcao == 4: #Sair
        print('Saindo...')
        break

    else:
        print('Opção inválida. Escolha novamente.')


