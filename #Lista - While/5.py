numero = int(input('Digite o nemuro a ser consultado os divisores: '))
inicial = numero
while numero > 0:
    if (inicial % numero) == 0:
        print (numero)
    numero -= 1