num=int(input('\033[35m digite um numero  '))
tot=0
for c in range (1,num+1):
    if num % c ==0:
        print('\033[32m', end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print(c,end=' ')
print('\n \033[0m o numero {} foi divizivel {} vezes'.format(num,tot))
if tot ==2:
    print('\n \033[0m é um numero primo')
else:
    print('\n \033[0mnão é primo')