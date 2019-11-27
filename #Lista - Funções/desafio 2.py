def cripto(string):
    alfabeto = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    criptografada = ''
    for letra in string:
        cont = 1
        while cont < len(alfabeto):
            if alfabeto[cont] == letra:
                criptografada += alfabeto[-cont]
            cont += 1
    print (criptografada)
    
mensagem = input('Digite uma palavra a ser criptografada: ')
cripto(mensagem)