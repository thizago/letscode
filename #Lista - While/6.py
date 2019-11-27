print ('''Somatório

''')
soma = 0
while True:
    numero = float(input('Digite um número a ser somado (0 para sair)'))
    if numero == 0:
        break
    soma += numero
print (soma)

