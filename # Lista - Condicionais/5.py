idade = int(input('Digite sua idade: '))

if idade < 0 or idade > 150:
    print ('Idade invalida')

salario = float(input('Digite o seu Salário: '))

if salario < 0:
    print ('Valor invalido')

sexo = input('Digite seu sexo (M, F ou Outro): ')

if (sexo != 'M') and (sexo != 'F') and (sexo != 'Outro'):
    print ('Entrada invalida')
