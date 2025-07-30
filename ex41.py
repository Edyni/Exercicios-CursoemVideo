from random import randint
computador=randint(0,10)
jogador=int(input('sou seu comutador e acabei de pensar em um numero de 0 a 10, consegue adivinhar? \n'))
while jogador not in computador:
    print('errou tente outra vez')
print('acertou')