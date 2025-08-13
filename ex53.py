tot=tot1=cont=menor=0
while True:
    produto=(input('qual o produto '))
    preco=float(input('qual o preço R$: '))
    cont+=1
    tot+=preco
    if preco >= 1000:
        tot1+=1
    if cont ==1:
        menor = preco
    else:
        if preco< menor:
            menor=preco
    resp=' '
    while resp not in 'SN':
        resp=(input('quer continuar ? [S/N] ')).strip().upper()
    if resp =='N':
        break
print('{:-^40}'. format(' fom do progama '))
print(f'total da compra: {tot}')
print(f'produto a cima de meil: {tot1}')
print(f'o mais barato foi : {menor}')