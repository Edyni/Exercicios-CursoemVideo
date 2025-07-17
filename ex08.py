from math import sin,radians,tan,cos
angulo=int(input('digite o angulo que deseja'))
seno = sin(radians (angulo))
print('o seno de {:.2f} é {:.2f}'. format(angulo,seno))
cosseno = cos(radians(angulo))
print('o coseno de {} é {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('a tangente de {} é {:.2f}'.format(angulo,tangente))