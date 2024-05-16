def lista(a,b,c):
    for item in range(a, b, c):
        soma = 0
        soma += item
    return soma, c


soma, passo = lista(1,10,2)

print(soma, passo)

