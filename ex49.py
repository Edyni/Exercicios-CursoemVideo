soma=quant=0
while True:
    n=int(input('Digite um numero: '))
    if n== 999:
        break
    soma+=n
    quant +=1
print(f'voce digitou {quant} e a soma entre eles é: {soma}')
