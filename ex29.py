peso=float(input('qual seu peso? KG:'))
altura=float(input('qual sua altura?'))
imc= peso / (altura ** 2)
if imc <18.5:
    print('abaixo do peso. seu imc: {:.1Ff}'.format(imc))
elif 18.5 <= imc <25:
    print('peso ideal. imc: {:.1f}'.format(imc))
elif 25 <= imc <30:
    print('sobre peso. imc: {:.1f}'.format (imc))
elif 30<= imc <40:
    print('obesidade')
else:
    print('vai morrer')