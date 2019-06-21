#CRIPTOGRAFA
valorString = (input("Digite um valor inteiro de 4 digítos: "))
if ((len(valorString)== 4) and (valorString.isdigit())):

    valorInt = [int(valorString[0]), int(valorString[1]), int(valorString[2]), int(valorString[3])]
    
    c = 0
    while c < 4:
        valorInt[c] = (valorInt[c] + 6) % 10
        c = c + 1
    
    aux = valorInt[0]
    valorInt[0] = valorInt[2]
    valorInt[2] = aux
    aux = valorInt[1]
    valorInt[1] = valorInt[3]
    valorInt[3] = aux
    
    print("Novo valor criptografado: %d%d%d%d"%(valorInt[0],valorInt[1],valorInt[2],valorInt[3]))
    
else:
    print("Erro. Por favor, digite apenas um valor de 4 dígitos.")


#DESCRIPTOGRAFAR
crip = input('Digite um valor de 4 dígitos criptografado: ')
if ((len(crip)== 4) and (crip.isdigit())):

    cripInt = [int(crip[0]),int(crip[1]),int(crip[2]),int(crip[3])]
    aux = crip[2]
    cripInt[2] = cripInt[0]
    cripInt[0] = aux
    aux = cripInt[3]
    cripInt[3] = cripInt[1]
    cripInt[1] = aux

    c = 0
    while c < 4:
        cripInt[c] = (int(cripInt[c]) % 10) - 6
        c = c + 1

    c = 0
    while c < 4:
        if (cripInt[c] <= 0):
            cripInt[c] = cripInt[c] % 10
        c = c + 1
    print('O número original é: %d%d%d%d'%(cripInt[0],cripInt[1],cripInt[2],cripInt[3]))
else:
    print("Erro. Por favor, digite apenas um valor de 4 dígitos.")