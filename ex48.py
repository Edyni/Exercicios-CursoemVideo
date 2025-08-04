r='s'
media= quant=soma=maior=menor=0
while r in 'Ss':
    n=int(input('digite um numero '))
    soma += n
    quant+=1
    if quant ==1:
        maior= menor =n
    else:
        if n>maior:
            maior=n
        if n< menor:
            menor=n
    r=(input('quer continuar? [s/n] ')).upper().strip()[0]
media= soma /quant
print('voce digitou {} numeros a media entre ele é {} e a soma é {}'.format(quant,media, soma)) 
print('O maior numero foi: {} e o menor numero foi: {}'.format(maior, menor))