from time import sleep
import textwrap

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


def depositar(saldo, valor, extrato_deposito,/):
    while True:
        if valor > 0:
            saldo += valor 
            extrato_deposito += f"Deposito no valor de R${valor:.2f}\n"
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
    return saldo, extrato_deposito


def sacar(*, saldo, limite, limites_saques, qntd_saques, extrato_saque):
    if qntd_saques == limites_saques:
                print("PROCESSANDO...")
                sleep(2.5)
                print('''
                    ------------------------------------
                     Limite de Saques diarios atingido
                    ------------------------------------
                ''')
    elif saldo == 0:
                print("PROCESSANDO...")
                sleep(2.5)
                print(''' 
                    ------------------------------------
                        Sua conta esta sem saldo
                    ------------------------------------
                ''')
    else:
        valor = float(input("Valor do saque: R$"))
        while True:
            if valor <=0:
                print("PROCESSANDO...")
                sleep(2)
                print('''
                ------------------------------------
                    Digite um valor valido 
                ------------------------------------
                ''')
            elif valor > saldo:
                print("PROCESSANDO...")
                sleep(2.5)
                print(f'''
                ------------------------------------
                            Saque falho
                ------------------------------------
                        SEU SALDO EH: R${saldo:.2f}
                ------------------------------------
                ''')
                break
            elif valor > limite:
                print("PROCESSANDO...")
                sleep(2.5)
                print(f'''
                ------------------------------------
                            Saque falho
                ------------------------------------
                    LIMITE POR SAQUE: R${limite:.2f}
                ------------------------------------
                ''')
                break
            elif limite >= valor <= saldo:
                saldo -= valor
                extrato_saque += f"Saque feito no valor de R${valor:.2f}\n"
                qntd_saques += 1
                print("PROCESSANDO...")
                sleep(2.5)
                print('''
                ------------------------------------
                    Saque Concluido com Sucesso
                ------------------------------------
                ''')
                break
    return saldo, extrato_saque, qntd_saques


def exibir_extrato(saldo, /, *, extrato_d, extrato_s): 
    if extrato_d == "" and extrato_s == "":
        extrato = "\nA conta nao foi movimentada"
    else:
        extrato = f'''
-=-=-=-=-=-=-=-=-=-=-=-=-=
  Depositos feitos:
-=-=-=-=-=-=-=-=-=-=-=-=-=
\n{extrato_d}
-=-=-=-=-=-=-=-=-=-=-=-=-=
  Saques feitos:
-=-=-=-=-=-=-=-=-=-=-=-=-=
\n{extrato_s}
-=-=-=-=-=-=-=-=-=-=-=-=-=
  Saldo: R${saldo:.2f}
-=-=-=-=-=-=-=-=-=-=-=-=-=
    '''            
    print(extrato)


def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

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

    usuarios.append({'nome':nome,
                     'data_nascimento':data_nascimento,
                     'endereco':endereco,
                     'cpf':cpf 
                     })
    print('''
------------------------------
  Usuario criado com sucesso
------------------------------
''')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print('''
------------------------------
   Conta criada com sucesso
------------------------------
''')
         return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    print('''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       Usuario nao encontrado.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
''')

def listar_contas(contas):
    for conta in contas:
          linha = f'''
                Agencia:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}      
    '''
    print('=' *100)
    print(textwrap.dedent(linha))

def main():
    saldo = 0 
    limite = 500
    LIMITES_SAQUE = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    extrato_d = ""
    extrato_s = ""
    qntd_saques = 0

    while True:
        opc = menu()

        if opc == 'd':
            valor = float(input("Valor do deposito: R$"))
            saldo, extrato_d = depositar(saldo, valor, extrato_d)
        
        elif opc == 's':
            saldo, extrato_s, qntd_saques = sacar(
                 saldo=saldo,
                 limite=limite,
                 qntd_saques=qntd_saques,
                 limites_saques=LIMITES_SAQUE,
                 extrato_saque=extrato_s
            )
        
        elif opc == "e":
            print("PROCESSANDO...")
            sleep(2.5)
            exibir_extrato(saldo, extrato_d=extrato_d, extrato_s=extrato_s)
        
        elif opc == "nu":
            criar_usuario(usuarios)

        elif opc == 'nc':
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

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



























               
    
            
        