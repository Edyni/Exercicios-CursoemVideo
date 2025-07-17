frase=input('digite sua frase: ').strip() .upper()
print('a letre aparece {} vezes'. format (frase.count('A') ))
print('a primeira vez que ela aparece é: {}'.format(frase.find('A')+1))
print('a ultima posição da letra A é: {} '.format(frase.rfind('A')+1))