valorcasa=float(input('qual o valor da casa? '))
salario=float(input('qual seu salario? '))
prazo=int(input('em quanto tempo voce quer pagar? '))
prestaçao = valorcasa / (prazo * 12)
minimo= salario* 30/100
print('para uma casa de $ {:.2f} em {} anos. a prestação será de {:.1f}'.format(valorcasa,prazo,prestaçao))
if prazo<= minimo:
    print('concedido')
else:
    print('pode nao filhao!')