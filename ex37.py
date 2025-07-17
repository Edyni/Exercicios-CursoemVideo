pa=int(input('digite o termo da PA '))
razao=int(input('digite a razao da PA '))
decimo= pa + (10-1)* razao
for c in range (pa , decimo + razao , razao):
    print(c, end=(" "))