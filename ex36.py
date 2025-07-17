soma=0
cont=0
for c in range(1,7):
    num=int(input('digite numero inteiro: \n '))
    if num %2==0:
        soma += num
        cont += +1
print('a soma de todos os numeros pares é: {} \n' 'os nmeros pares digitados foram:{}'.format(soma,cont))