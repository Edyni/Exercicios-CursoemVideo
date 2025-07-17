salario=float(input(' Qual seu Salario? '))
if salario <=1250:
    novosalario = salario + (salario *  15/100)
    print ('Seu Novo salario é {} '.format(novosalario))
else: 
    novosalario = salario + (salario * 10/100)
    print('novo salario {} '.format(novosalario))