print('Gerador de PA')
print('=-=' * 10)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = a1
cont = 1
while cont <= 10:
    print('{} ' .format(termo), end='')
    termo += r
    cont += 1
    print('-> ' if cont < 11 else '', end='')