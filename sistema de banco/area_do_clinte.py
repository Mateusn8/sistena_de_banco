from sistema_de_banco import Cliente, Banco,  Contapoupanca, ContaCorrente


banco = Banco()

nome1 = input('Digite o nome de usuario na conta: ')
idade1 = int(input('Digite sua idade: '))
agencia1 = int(input('agencia: '))
numeroconta1 = int(input('conta: '))

cliente1 = Cliente(nome1, idade1)

conta1 = ContaCorrente(agencia1, numeroconta1, 1200)

cliente1.inserirconta(conta1)

banco.inserircliente(cliente1)

senha = 4569
suasenha = int(input('senha: '))

if senha == suasenha:
    banco.autentificar(cliente1, conta1)
    print(conta1.detalhes())
    print(conta1.sacar(int(input('Digite o valor que degeja sacar: '))))
    print(conta1.deposito(int(input('Digite o valor que degeja depositar: '))))
    print(conta1.detalhes())
else:
    print('Cliente não autenticado')

nome2 = input('Digite o nome de usuario na conta: ')
idade2 = int(input('Digite sua idade: '))
agencia2 = int(input('agencia: '))
numeroconta2 = int(input('conta: '))

cliente2 = Cliente(nome2, idade2)

conta2 = Contapoupanca(agencia2, numeroconta2, 100)

cliente2.inserirconta(conta2)

banco.inserircliente(cliente2)

senha = 3698
suasenha = int(input('senha: '))


if senha == suasenha:
    banco.autentificar(cliente2, conta2)
    print(conta2.detalhes())
    print(conta2.sacar(int(input('Digite o valor que degeja sacar: '))))
    print(conta2.deposito(int(input('Digite o valor que degeja depositar: '))))
    print(conta2.detalhes())
else:
    print('Cliente não autenticado')

nome3 = input('Digite o nome de usuario na conta: ')
idade3 = int(input('Digite sua idade: '))
agencia3 = int(input('agencia: '))
numeroconta3 = int(input('conta: '))

cliente3 = Cliente(nome3, idade3)

conta3 = ContaCorrente(agencia3, numeroconta3, 500)

cliente3.inserirconta(conta3)

banco.inserircliente(cliente3)

senha = 6030
suasenha = int(input('senha: '))

if senha == suasenha:
    banco.autentificar(cliente3, conta3)
    print(conta3.detalhes())
    print(conta3.sacar(int(input('Digite o valor que degeja sacar: '))))
    print(conta3.deposito(int(input('Digite o valor que degeja depositar: '))))
    print(conta3.detalhes())
else:
    print('Cliente não autenticado')