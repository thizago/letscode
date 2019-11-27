numero_maximo = int(input('Digite até que número deseja o fatorial: '))
i = 1
fatorial = 1

while i <= numero_maximo:
   fatorial *= i
   i += 1
    
print (numero_maximo,'n!:', fatorial)