numero = float(input('Digite um número: '))

if numero == 0:
    print('Zero não é par nem impar')
elif (numero % 2) == 0:
    print (numero, 'é par.')
else:
    print (numero , 'é impar')