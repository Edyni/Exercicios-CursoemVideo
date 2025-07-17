from random import randint
from time import sleep
numero= randint (0,5)
palpite=int(input('Qua seu palpite? '))
print('PRECESSANDO...')
sleep(3)
if palpite== numero:
    print('acertou mizeravi')
else:
    print('errou tente outra vez')