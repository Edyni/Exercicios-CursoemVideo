sexo=str(input('Digite seu sexo [F/M]:')).strip().upper()[0]
while sexo not in 'FM':
    sexo=str(input('dados invalido por favor digite uma opção verdadeira: \n')).strip().upper()[0]
print('sexo {} cadastrado'.format(sexo))
