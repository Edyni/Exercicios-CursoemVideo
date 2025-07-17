numero=int(input('digite um valor inteiro: ' ))
print('''escolha uma opção
      [ 1 ] para coverter em BINARIO 
      [ 2 ] para converter em OCTAL
      [ 3 ] para convertte em HEXADECIAML''')
opcao = int(input('qual a opção? '))
if opcao==1:
    print('o nmero {} convertido em BINARIO é: {} '.format(numero, bin(numero)[2:]))
elif opcao==2:
    print(' o nmero {} convertido em OCTAL é: {}'.format(numero, oct(numero)[2:]))
elif opcao==3:
    print(' o numero {} convertido em HEXADECIMAL é: {}'.format(numero,hex(numero)[2:]))
else:
    print('opção invalida')