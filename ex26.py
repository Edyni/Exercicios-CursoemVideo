from datetime import date
atual=date.today().year
nsc=int(input('qual a sua data de nasciimento?'))
idade=atual-nsc
print('quem nasceu em {} tem {} anos de idade'.format(nsc,idade))
if idade < 18:
    print('voce ainda nao pode se alistar')
elif idade==18:
    print('se aliste agora')
elif idade > 18:
    print('ja passou da hora de se alistar')