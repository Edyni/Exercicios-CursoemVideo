n1=float(input('digite sua primeira nota:'))
n2=float(input('digite sua segunda nota: '))
media = (n1+n2) / 2
if 7 > media >=5:
    print('aluno em recupeção media:{}'.format(media))
elif media >7:
    print('aprovado com media{}'.format(media))
else:
    print('aluno reprovado {}'.format(media))