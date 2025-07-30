from time import sleep
n1=int(input('Digite um numero '))
n2=int(input('Digite o segundo numero '))
opcao=0
while opcao != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] ENCERRAR''')
    opcao=int(input('Qual a sua opção? '))
    if opcao==1:
        soma=n1+n2
        print('a soma entre {} e {} é:{} '.format(n1,n2,soma))
    elif opcao==2:
        mult=n1*n2
        print('A mltiplicação ente {} e {} é:`{} '.format(n1,n2,mult))
    elif opcao==3:
        if n1>n2:
            maior = n1
        else:
            maior=n2
        print('Entre {} e {} o maior numero é:{}'.format(n1,n2,maior))
    elif opcao==4:
        print('Informe os numeros novamente:')
        n1=int(input('Digite o primeiro valor:'))
        n2=int(input('digite o segundo valor'))
    elif opcao == 5:
        print('finalizando...')
        sleep(2)
    else:
        print('opção invalida')
print('Fim do Progama.')