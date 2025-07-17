from random import randint
print('''opcoes
      [0] pedra 
      [1] papel
      [2] esoura''')
jogador=int(input('digite um numero '))
itens=('pedra','papel','tesoura')
computador = randint ( 0,2)
print('o jogador jogou {}'.format(itens[jogador]))
print('o computador escolheu {}'.format(itens[computador]))
if computador ==0:
    if jogador ==0:
        print('empate')
    elif jogador == 1:
        print('jogador Ganhou!!')
    elif jogador ==2:
        print('computador ganhou!')
    else:
        print('jogada invalida')
elif computador ==1:
    if jogador ==0:
        print('computador venceu')
    elif jogador == 1:
            print('empate!!')
    elif jogador ==2:
        print('jogar ganhou!!')
    else:
        print('jogada invalida')
elif computador==2:
    if jogador ==0:
        print('computador venceu!')
    elif jogador == 1:
        print('jogador Ganhou!!')
    elif jogador ==2:
        print('empate!')
    else:
        print('jogada invalida')