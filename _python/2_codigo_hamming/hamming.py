
opcoes = int(input('Olá!\n\t Aperte 1 para gerar um código de Hamming\n\t Aperte 2 para encontrar o erro no código de Hamming\n\t Digite sua escolha: \n'))

if(opcoes == 1):  
    print('Digite os números: ')
    x = input()

    data = list(x)
    data.reverse()
    a, b, c, d, e = 0,0,0,0,[]

    while ((len(x) + d + 1) > (pow(2, d))):
        d = d + 1

    for i in range(0, (d + len(data))):
        p = (2 ** a)

        if(p == (i + 1)):
            e.append(0)
            a = a + 1

        else:
            e.append(int(data[c]))
            c = c + 1

    for paridades in range(0,(len(e))):
        pe = (2 ** b)

        if(pe == (paridades + 1)):
            iniciar = pe - 1
            i = iniciar
            toXor = []

            while(i < len(e)):
                block = e[i:i + pe]
                toXor.extend(block)
                i += 2 * pe

            for z in range(1, len(toXor)):
                e[iniciar] = e[iniciar] ^ toXor[z]
            b += 1

    e.reverse()
    print('Seu código de Hamming gerado: ', end = "")
    print(int(''.join(map(str, e))))

elif(opcoes == 2): 
    print('Digite o código de Hamming que foi gerado: ')

    x = input()
    data = list(x)
    data.reverse()
    a, b, c, d, error, e, paridadesArray, e_copy = 0,0,0,0,0,[],[],[]

    for k in range(0,len(data)):
        p = (2 ** c)
        e.append(int(data[k]))
        e_copy.append(data[k])

        if(p == ( k + 1 )):
            c = c + 1
            
    for paridades in range(0,(len(e))):
        pe = (2 ** b)
        if (pe == (paridades + 1)):

            iniciar = pe - 1
            i = iniciar
            toXor = []

            while(i < len(e)):
                block = e[i:i + pe]
                toXor.extend(block)
                i += 2 * pe

            for z in range(1,len(toXor)):
                e[iniciar] = e[iniciar] ^ toXor[z]
            paridadesArray.append(e [paridades])
            b += 1
    paridadesArray.reverse()
    error = sum(int(paridadesArray) * (2 ** i) for i, paridadesArray in enumerate(paridadesArray[:: -1]))
    
    if((error) == 0):
        print('Sucesso! Sem erro!')

    elif((error) >= len(e_copy)):
        print('Erro não foi detectado')

    else:
        print('Erro encontrado na posição: ',error)

else:
    print('Número digitado inválido.')