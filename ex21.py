d=float(input('qaul a distancia da viajem: '))
valor1= d* 0.50
valor2= d* 0.45
if d <=200:
    print('valor{:.2f}'.format(valor1))
else:
    print("valor {:.2f}".format(valor2))