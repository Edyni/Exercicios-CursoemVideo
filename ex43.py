from math import factorial
n=int(input('Digite um numero \npara calcular seu fatorial: '))
c=n
f=factorial(n)
print(' o fatrial de {}! é: '.format(n))
while c>0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=' '{}'.format(f),end=' ')
    c-=1