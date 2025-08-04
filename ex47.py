nu=soma=cont=0
cont=0
nu=int(input('Digite um numero 999 para parar: '))
while nu != 999:
    soma +=nu
    cont +=1
    nu=int(input('Digite um numero 999 para parar: '))
print('voce digitou {} numros e a soma entre eles é: {}'.format(cont,soma))