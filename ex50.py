from time import sleep
while True:
    n=int(input('Qual tabuada você deseja ver? '))
    print('Procenssando...')
    sleep(1)
    print('-'*45)
    if n==0:
        break
    print(f'tabuada de {n} :')
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*45)
print('fim!')