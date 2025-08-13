from random import randint
v=0
while True:
    jogador=int(input('Digite um numero! '))
    computador=randint(0,10)
    total=jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input(" você escolher Par ou Impar?")).upper().strip() [0]
    print(f'jogadaor escolheu: {jogador} e amaquina: {computador} o total da partida foi: {total}')
    if tipo=='P':
        if total % 2==0:
            print('voce venceu!')
            v+=1
        else:
            print('voce perdeu!')
            break
    elif tipo == 'I':
        if total % 2==1:
            print('voce venceu!')
            v+=1
        else:
            print('voce perdeu')
            break
print(f'vitorias {v}')