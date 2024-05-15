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

def depositar(saldo, valor,/):
    extrato_deposito = ""
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

def sacar(*, saldo, valor, limite):
    qntd_saques = 0
    extrato_saque = ""

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
    extrato = f'''
    -=-=-=-=-=-=-=-=-=-=-=-=-=
    Depositos feitos:
    -=-=-=-=-=-=-=-=-=-=-=-=-=
    {extrato_d}
    -=-=-=-=-=-=-=-=-=-=-=-=-=
    Saques feitos:
    -=-=-=-=-=-=-=-=-=-=-=-=-=
    {extrato_s}
    -=-=-=-=-=-=-=-=-=-=-=-=-=
    Saldo: R${saldo:.2f}
    -=-=-=-=-=-=-=-=-=-=-=-=-=
    '''            
    return extrato

def criar_usuario(usuario):
    print

def filtrar_usuario(cpf, usuario):
    print()

def main():
    saldo = 0 
    limite = 500
    LIMITES_SAQUE = 3
    usuarios = []
    contas = []
    

    while True:
        opc = menu()

        if opc == 'd':
            valor = float(input("Valor do deposito: R$"))

            saldo, extrato_deposito = depositar(saldo, valor)
        
        elif opc == 's':
            if qntd_saques == LIMITES_SAQUE:
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
                break
            else:
                valor = float(input("Valor do saque: R$"))
                saldo, extrato_saque, qntd_saques = sacar(saldo=saldo, valor=valor, limite=limite)
        elif opc == "e":
            if extrato_deposito == "" and extrato_saque == "":
                extrato = "A conta nao foi movimentada"
            else:
                print("PROCESSANDO...")
                sleep(2.5)
                exibir_extrato(saldo, extrato_d=extrato_deposito, extrato_s=extrato_saque)
        elif opc == 'q':
            print('''
            -=-=-=-=-=-=-=-=-=-=-=-=-=
                VOLTE SEMPRE
            -=-=-=-=-=-=-=-=-=-=-=-=-=
            ''')
            break                
                

main()



























               
    
            
        