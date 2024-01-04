usuarios = []
contas_correntes = []
numero_conta = 0
agencia = "0001"

def criar_usuario():
    return {'nome': input("Digite o nome do usuário: "), 'data_nascimento': input("Digite a data de nascimento (DD/MM/AAAA): "),
            'cpf': input("Digite o CPF: "), 'endereco': input("Digite o endereço: ")}

def criar_conta_corrente(usuario):
    global numero_conta
    numero_conta += 1
    return {'numero_conta': numero_conta, 'agencia': agencia, 'usuario': usuario, 'saldo': 0, 'depositos': [],
            'saques': [], 'saldo_diario': 0, 'saques_diarios': 0, 'limite_diario': 1500, 'limite_saque': 500}

def realizar_saque(conta, valor_saque):
    if conta['saldo_diario'] + valor_saque > conta['limite_diario']:
        return f'Limite diário de saque atingido. Máximo de R$ {conta["limite_diario"]:.2f} por dia'
    elif valor_saque > 0 and conta['saldo'] >= valor_saque <= conta['limite_saque']:
        conta['saldo'] -= valor_saque
        conta['saldo_diario'] += valor_saque
        conta['saques'].append(valor_saque)
        conta['saques_diarios'] += 1
        return f'Saque de R$ {valor_saque:.2f} realizado com sucesso.'
    elif conta['saldo'] < valor_saque:
        return 'Saldo insuficiente.'
    elif valor_saque > conta['limite_saque']:
        return f'Valor máximo por saque é de R$ {conta["limite_saque"]:.2f}.'

def realizar_deposito(conta, valor_deposito):
    if valor_deposito > 0:
        conta['saldo'] += valor_deposito
        conta['depositos'].append(valor_deposito)
        return f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!'
    else:
        return 'O valor do depósito deve ser positivo'

def exibir_extrato(conta):
    if not conta['depositos'] and not conta['saques']:
        return ['Não foram realizadas movimentações.']
    else:
        extrato = [f'Depósito: R$ {deposito:.2f}' for deposito in conta['depositos']]
        extrato.extend([f'Saque: R$ {saque:.2f}' for saque in conta['saques']])
        extrato.append(f'Saldo atual: R${conta["saldo"]:.2f}')
        return extrato

while True:
    print('\nMENU:')
    print('1. Criar Usuário')
    print('2. Criar Conta Corrente')
    print('3. Saque')
    print('4. Depósito')
    print('5. Extrato')
    print('6. Listar Usuários e Contas')
    print('7. Sair')

    opcao = int(input('Escolha uma opção (1-7): '))

    if opcao == 1:  # Criar Usuário
        novo_usuario = criar_usuario()
        if not any(user['cpf'] == novo_usuario['cpf'] for user in usuarios):
            usuarios.append(novo_usuario)
            print('Usuário criado com sucesso!')
        else:
            print('CPF já cadastrado. Cada usuário deve ter um CPF único.')

    elif opcao == 2:  # Criar Conta Corrente
        cpf_usuario = input("Digite o CPF do usuário para associar a conta corrente: ")
        usuario_associado = next((user for user in usuarios if user['cpf'] == cpf_usuario), None)
        if usuario_associado:
            nova_conta = criar_conta_corrente(usuario_associado)
            contas_correntes.append(nova_conta)
            print(f'Conta corrente criada com sucesso! Número da conta: {nova_conta["numero_conta"]}')
        else:
            print('Usuário não encontrado. Cadastre o usuário primeiro.')

    elif opcao == 3:  # Saque
        numero_conta = int(input("Digite o número da conta para realizar o saque: "))
        conta_saque = next((conta for conta in contas_correntes if conta['numero_conta'] == numero_conta), None)
        if conta_saque:
            valor_saque = float(input('Digite o valor do saque: '))
            print(realizar_saque(conta_saque, valor_saque))
        else:
            print('Conta corrente não encontrada.')

    elif opcao == 4:  # Depósito
        numero_conta = int(input("Digite o número da conta para realizar o depósito: "))
        conta_deposito = next((conta for conta in contas_correntes if conta['numero_conta'] == numero_conta), None)
        if conta_deposito:
            valor_deposito = float(input('Digite o valor do depósito: '))
            print(realizar_deposito(conta_deposito, valor_deposito))
        else:
            print('Conta corrente não encontrada.')

    elif opcao == 5:  # Extrato
        numero_conta = int(input("Digite o número da conta para visualizar o extrato: "))
        conta_extrato = next((conta for conta in contas_correntes if conta['numero_conta'] == numero_conta), None)
        if conta_extrato:
            print(*exibir_extrato(conta_extrato), sep='\n')
        else:
            print('Conta corrente não encontrada.')
            
    elif opcao == 6:  # Listar Usuários e Contas
        print('\nLista de Usuários e Contas:')
        for usuario in usuarios:
            print(f'\nUsuário: {usuario["nome"]}')
            contas_usuario = [conta["numero_conta"]for conta in contas_correntes if conta['usuario'] == usuario]
            if contas_usuario:
                for numero_conta in contas_usuario:
                    print(f'Conta corrente: {numero_conta}')
            else:
                print('Nenhuma conta associada a este usuário.')

    elif opcao == 7:  # Sair
        print('Saindo...')
        break

    else:
        print('Opção inválida. Escolha novamente.')
