nota_1 = float(input('Digite a nota 1: '))
nota_2 = float(input('Digite a nota 2: '))
nota_3 = float(input('Digite a nota 3: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media > 6:
    print ('Passou!')
else:
    print('Bombou')
