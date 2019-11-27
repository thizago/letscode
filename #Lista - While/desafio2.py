contador = 1
numero = 1
soma = 0
while contador <= 10:
    soma = soma + numero
    numero = 1/( numero * contador)
    contador +=1
    print (contador, numero, soma)
