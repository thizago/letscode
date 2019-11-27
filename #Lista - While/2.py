numero_maximo = int(input('Digite até que número deseja a somatoria: '))
i = 1
soma = 0

while i <= numero_maximo:
    soma += i
    i += 1
    
print (':', soma)