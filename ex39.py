somaidade=0
mediaidade=0
maioridadehomem=0
nomevelhor=''
for p in range (1,3):
    print('-------- {}º pessoa-------'.format(p))
    nome=(input('nome: ')).strip()
    idade=int(input('idade: '))
    sexo=(input('sexo [M / F]: ')).strip()
    somaidade += idade
mediaidade=somaidade/4
print('a media  da idade do grupo é: {}'.format(mediaidade))