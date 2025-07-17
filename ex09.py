from random import choice
n1=(input('primeiro nome: '))
n2=(input('segundo nome: '))
n3=(input('terceiro nome: '))
lista=[n1,n2,n3]
sorteado= choice (lista)
print('o sortudo foi {}'.format(sorteado))