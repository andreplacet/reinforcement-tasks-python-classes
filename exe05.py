# Exercicio 05


class ContaCorrente:
    def __init__(self, nome, conta, saldo=0):
        self.conta = '000' + str(conta)
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return nome

    def alterar_nome(self):
        try:
            new_name = str(input('Digite o novo nome: '))
            self.nome = new_name
            print('Nome atualizado com sucesso!')
        except:
            print('Falha ao alterar o nome, tente novamente!')

    def saque(self):
        if self.saldo > 0:
            saque = float(input(f'Saldo dísponivel: R$ {self.saldo:.2f}'
                                f'\nQual valor deseja sacar? '))
            if saque > self.saldo:
                print('Não foi possivel realizar o saque, valor acima do saldo disponivel!')
            else:
                self.saldo -= saque
                print(f'Saque concluido!\n'
                      f'Saldo disponivel R${self.saldo:.2f}')
        else:
            print('Saldo não disponivel para saque!')

    def deposito(self):
        print(f'Saldo disponivel R$ {self.saldo:.2f}')
        try:
            new_saldo = float(input('Informe o valor do deposito: '))
            self.saldo += float(new_saldo)
            print(f'Deposito no valor de R${new_saldo:.2f} efetuado com sucesso!')
        except:
            print('Não foi possivel realizar o deposito, tente novamente!')


contas = []

while True:
    print(f'{"BANCO ACME INC":^50}')
    print(f'{"="}' * 50)
    print('Bem vindo a interface de de gerenciamento do banco\nAcme INC\n'
          'Em que podemos ajuda-lo hoje?')
    escolha = int(input('1 - Criar Conta  '
                        '2 - Fazer depósito\n'
                        '3 - Fazer Saque  '
                        '4 - Alterar dados da conta\n'
                        '0 - Sair\n'
                        '--> '))
    if escolha not in (0, 1, 2, 3, 4):
        pass
    else:
        if escolha == 1:
            nome = str(input('Nome: ')).capitalize()
            conta = str(input('Número da conta: '))
            novo_cliente = ContaCorrente(nome=nome, conta=conta)
            contas.append(novo_cliente)
        elif escolha == 2:
            nome = str(input('Nome do correntista: ')).capitalize()
            for item in contas:
                if nome == item.nome:
                    item.deposito()
                else:
                    print('Conta nao encontrada!')
        elif escolha == 3:
            try:
                nome = str(input('Nome do correntista: ')).capitalize()
                for item in contas:
                    if nome == item.nome:
                        item.saque()
                    else:
                        print('Conta não econtrada')
            except:
                print('Não foi possivel efetuar o saque!!')
        elif escolha == 4:
            try:
                nome = str(input('Nome do correntista: ')).capitalize()
                for item in contas:
                    if nome == item.nome:
                        item.alterar_nome()
                    else:
                        print('Conta não econtrada!')
            except:
                print('Não foi possivel alterar os dados')
        elif escolha == 0:
            print('Obrigado por usar os nosso serviços !!')
            break
