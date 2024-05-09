from time import sleep

menu = '''
==================
[d] DEPOSITAR
[s] SACAR
[e] EXTRATO
[q] SAIR
==================

=> '''

saldo = 0 
limite_por_saque = 500
extrato = ""
numeros_saque = 0 
LIMITES_SAQUE = 3
qntd_saques = 0
extrato_saque = ""
extrato_deposito = ""


while True:
    opc = input(menu).lower().strip()

    if opc == 'd':
        while True:
            valor_deposito = float(input("Valor do deposito: R$"))
            if valor_deposito > 0:
                saldo += valor_deposito  
                extrato_deposito += f"Deposito no valor de R${valor_deposito:.2f}\n"
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
        elif qntd_saques <= LIMITES_SAQUE:
            while True:
                valor_saque = float(input("Valor do saque: R$"))
                if valor_saque <=0:
                    print("PROCESSANDO...")
                    sleep(2)
                    print('''
                    ------------------------------------
                           Digite um valor valido 
                    ------------------------------------
                    ''')
                elif valor_saque > saldo:
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
                elif valor_saque > limite_por_saque:
                    print("PROCESSANDO...")
                    sleep(2.5)
                    print(f'''
                    ------------------------------------
                                Saque falho
                    ------------------------------------
                        LIMITE POR SAQUE: R${limite_por_saque:.2f}
                    ------------------------------------
                    ''')
                elif limite_por_saque >= valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato_saque += f"Saque feito no valor de R${valor_saque:.2f}\n"
                    qntd_saques += 1
                    print("PROCESSANDO...")
                    sleep(2.5)
                    print('''
                    ------------------------------------
                         Saque Concluido com Sucesso
                    ------------------------------------
                    ''')
                    break
    elif opc == "e":
        if extrato_deposito == "" and extrato_saque == "":
            extrato = "A conta nao foi movimentada"
        else:
            extrato = f'''
-=-=-=-=-=-=-=-=-=-=-=-=-=
Depositos feitos:
-=-=-=-=-=-=-=-=-=-=-=-=-=
{extrato_deposito}
-=-=-=-=-=-=-=-=-=-=-=-=-=
Saques feitos:
-=-=-=-=-=-=-=-=-=-=-=-=-=
{extrato_saque}
-=-=-=-=-=-=-=-=-=-=-=-=-=
Saldo: R${saldo:.2f}
-=-=-=-=-=-=-=-=-=-=-=-=-=
                '''            
        print("PROCESSANDO...")
        sleep(2.5)
        print(extrato)
    elif opc == 'q':
        print('''
        -=-=-=-=-=-=-=-=-=-=-=-=-=
              VOLTE SEMPRE
        -=-=-=-=-=-=-=-=-=-=-=-=-=
        ''')
        break                
                

               
    
            
        