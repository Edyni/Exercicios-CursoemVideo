from datetime import date
atual= date.today().year
nsc=int(input('Qual seu ano de nascimento?'))
idade = atual-nsc
if idade<=9:
    print('atleta Mirim idade: {}'.format(idade))
elif idade <=14:
    print('atleta infantil idade: {}'.format(idade))
elif idade <=19:
    print('atleta junior idade: {}'.format(idade))
elif idade <=25:
    print('atleta senior idade: {}'.format(idade))
else:
    print('atleta topado idade: {}'.format(idade))