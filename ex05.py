n1=float(input('digite sua primeira nota aqui!'))
n2=float(input('digite sua segunda nota aqui'))
m = (n1+n2)/2
print('a media entre {} e {} é {} '.format(n1,n2,(n1+n2)/2))
if (m <= 6):
    print ('aluno reprovado!')
else:
    print('aluno aprovado!')