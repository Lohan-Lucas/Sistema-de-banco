from abc import ABC, abstractclassmethod, abstractproperty
from time import sleep
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
        self._limite = 500
        self._LIMITES_SAQUE = 3
        self._qntd_saques = 0
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @property
    def limite(self):
        return self._limite
    
    @property
    def limiteSaque(self):
        return self._LIMITES_SAQUE
    
    @property
    def qntdSaque(self):
        return self._qntd_saques

    def sacar(self, valor):
        if self.qntdSaque == self.limiteSaque:
                    print("PROCESSANDO...")
                    sleep(2.5)
                    print('''
                        ------------------------------------
                         Limite de Saques diarios atingido
                        ------------------------------------
                    ''')
        elif self.saldo == 0:
                    print("PROCESSANDO...")
                    sleep(2.5)
                    print(''' 
                        ------------------------------------
                            Sua conta esta sem saldo
                        ------------------------------------
                    ''')
        else:
            while True:
                if valor <=0:
                    print("PROCESSANDO...")
                    sleep(2)
                    print('''
                    ------------------------------------
                         Digite um valor valido 
                    ------------------------------------
                    ''')
                elif valor > self.saldo:
                    print("PROCESSANDO...")
                    sleep(2.5)
                    print(f'''
                    ------------------------------------
                                Saque falho
                    ------------------------------------
                            SEU SALDO EH: R${self.saldo:.2f}
                    ------------------------------------
                    ''')
                    break
                elif valor > self.limite:
                    print("PROCESSANDO...")
                    sleep(2.5)
                    print(f'''
                    ------------------------------------
                                Saque falho
                    ------------------------------------
                        LIMITE POR SAQUE: R${self.limite:.2f}
                    ------------------------------------
                    ''')
                    break
                elif self.limite >= valor <= self.saldo:
                    self.saldo -= valor
                    self.qntdSaque += 1
                    print("PROCESSANDO...")
                    sleep(2.5)
                    print('''
                    ------------------------------------
                        Saque Concluido com Sucesso
                    ------------------------------------
                    ''')
                    break

    def depositar(self, valor):
        while True:
            if valor > 0:
                self.saldo += valor 
                print("PROCESSANDO...")
                sleep(2.5)
                print('''
                ------------------------------------
                   Deposito Concluido com Sucesso
                ------------------------------------
                ''')
                break
            else:
                print("PROCESSANDO...")
                sleep(2.5)
                print('''
                ------------------------------------
                      Digite um valor valido
                ------------------------------------
                ''')

    def __str__(self):
        return f"""
            Agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Sacar(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Depositar(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    menu = '''
    =========== MENU ============
    [d]\tDEPOSITAR
    [s]\tSACAR
    [e]\tEXTRATO
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSAIR
    ==============================

    => '''
    return input(textwrap.dedent(menu))

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("!!! Cliente nao encontrado !!!")
        return
    
    valor = float(input("Informe o valor do deposito: R$"))
    transacao = Depositar(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("!!! Cliente nao encontrado !!!")
        return
    
    valor = float(input("Informe o valor do saque: R$"))
    transacao = Sacar(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def criar_cliente(clientes):
    cpf = input("Informe o CPF(somente numeros): ")
    usuario = filtrar_cliente(cpf, clientes)

    if usuario:
         print('''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  Ja existe um usuario com esse CPF.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
''')
         return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd/mm/aaaa): ")
    endereco = input("Informe o endereco(logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    
    clientes.append(cliente)
    print('''
------------------------------
  Usuario criado com sucesso
------------------------------
''')
    
def criar_conta(clientes, numero, contas):
    cpf = input("Informe o CPF do usuario: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       cliente nao encontrado.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
''')    
        return
        
    conta = Conta.nova_conta(cliente=cliente, numero=numero)
    contas.append(conta)
    cliente.contas.append(contas)


    print('''
------------------------------
   Conta criada com sucesso
------------------------------
''')
        
def listar_contas(contas):
    for conta in contas:
        print('=' *100)
        print(textwrap.dedent(str(conta)))
   
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("!!! Cliente nao possui conta !!!")
        return
    else:
        return cliente.contas[0]

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("!!! Cliente nao encontrado !!!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("=============EXTRATO=============")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Nao foram realizadas transacoes"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR${conta.saldo:.2f}")
    print("=================================")

def main():
    clientes = []
    contas = []

    while True:
        opc = menu()

        if opc == 'd':
            depositar(clientes)
        
        elif opc == 's':
            sacar(clientes)
        
        elif opc == "e":
            exibir_extrato(clientes)
        
        elif opc == "nu":
            criar_cliente(clientes)

        elif opc == 'nc':
            numero = len(contas) + 1
            conta = criar_conta(clientes, numero, contas)

            if conta:
                contas.append(conta)

        elif opc == "lc":
            listar_contas(contas)
             
        elif opc == 'q':
            print('''
            -=-=-=-=-=-=-=-=-=-=-=-=-=
                   VOLTE SEMPRE
            -=-=-=-=-=-=-=-=-=-=-=-=-=
            ''')
            break       

main()