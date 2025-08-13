tot18=toth=totm20=0
while True:
    nome=(input('Qual seu nome ')).strip().upper()
    idade=int(input('qual sua idade? '))
    sexo=' '
    while sexo not in 'MF':
        sexo=(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    if idade >=18:
        tot18+=1
    if sexo =='M':
        toth+=1
    if sexo=='F' and idade < 20:
        totm20+=1
    resp=' '
    while resp not in 'SN':
        resp=input('Quer Continuar? ').strip().upper()
    if resp =='N':
        break
print('finish')
print(f'total de pessoas com mais de 18 anos {tot18} ')
print(f'ao todo temos {toth} homens cadastrados ')
print(f'e temos {totm20} com menos de 20 anos ')