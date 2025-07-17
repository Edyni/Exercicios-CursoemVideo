print(20*'-')
print('   loja do Edyni')
print(20*'-')
compra=float(input('qual o valor da compra?'))
print('''opcoes de pagamento
      [ 1 ] pix
      [ 2 ]a vista cartao
      [ 3 ]2x cartao
      [ 4 ]3x no cartao ou mais''')
opcao=int(input('qual opcao?'))
if opcao == 1:
    desconto = compra - (compra * 10/100)
    print(' sua compra no valor de {} com desconto fica: {} '.format(compra, desconto))
elif opcao==2:
    desconto= compra- (compra * 5/100)
    print('sua compra no cartao de {} fica de {}'.format(compra,desconto))
elif opcao==3:
    parcela= compra/2
    print('sua compra de {}realizada com sucesso, parcelada em 2x de {}'.format(compra,parcela))
elif opcao==4:
    juros = compra +(compra*20/100)
    totparcela=int(input('parcelar em quantas vezes?'))
    parcela= juros/totparcela
    print('sua compra de {} parcelado em {}x com juros fica de {}'.format(compra,totparcela,juros))
else:
    print('Opçao invalida')