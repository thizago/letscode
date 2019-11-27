while True:
    idade = int(input('Digite a sua idade: '))
    if 0 <= idade <= 150:
        break
    print ('Esse campo só aceita números entre 0 e 150.')

while True:
    salario = int(input('Digite o seu salário: '))
    if salario >= 0:
        break
    print ('Esse campo só aceita numeros positivos.')
while True:
    sexo = input('Digite seu sexo (M, F, Outro)')
    if sexo == 'M' or sexo == 'F' or sexo == 'Outro':
        break
    print ('Esse campo só aceita M, F ou Outro.')
print ('Você tem', idade , 'anos, ganha', salario , 'e se identifica com o sexo ', sexo )

 

