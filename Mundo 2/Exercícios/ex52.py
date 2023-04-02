cont = 0
num = int(input('Digite um número: ' '\033[32m'))
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} ' .format(c), end=' ')

if cont > 2:
    print('\033[m' '\nEsse número tem {} divisores. \nEle não é primo!' .format(cont))
elif cont == 1:
    print('\033[m' '\nO número 1 é especial!')
else:
    print('\033[m' '\nEsse número só se divide por 1 e ele mesmo. \nEle é primo!')


