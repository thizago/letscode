soma = 0
resposta = ''
while resposta != 'S'  and resposta != 'N':
    resposta = (input('Telefonou para a vítima? (S/N): '))
    if resposta == 'S':
        soma += 1
resposta = ''
while resposta != 'S' and resposta != 'N':
    resposta = (input('Esteve no local do crime? (S/N): '))
    if resposta == 'S':
        soma += 1
resposta = ''
while resposta != 'S' and resposta != 'N':
    resposta = (input('Mora perto da vítima? (S/N): '))
    if resposta == 'S':
        soma += 1    
resposta = ''
while resposta != 'S' and resposta != 'N':
    resposta = (input('Devia para a vítima? (S/N): '))
    if resposta == 'S':
        soma += 1    
resposta = ''
while resposta != 'S' and resposta != 'N':
    resposta = (input('Já trabalhou com a vítima? (S/N): '))
    if resposta == 'S':
        soma += 1    
resposta = ''

if soma == 5:
    print ('Assassino!')
elif soma >= 3:
    print ('Cumplice!')
elif soma >= 2:
    print ('Suspeito!')
else:
    print ('Liberado!')

    


'''
a. Telefonou para a vítima?
b. Esteve no local do crime?
c. Mora perto da vítima?
d. Devia para a vítima?
e. Já trabalhou com a vítima?
'''