import textwrap

def menu():
    menu = '''
    ============ MENU ============
    [d] \tDEPOSITAR
    [s] \tSACAR
    [e] \tEXTRATO
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q] \tSAIR
    ==============================

    => '''
    return input(textwrap.dedent(menu))


menu()
