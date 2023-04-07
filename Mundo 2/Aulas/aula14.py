'''for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('FIM')

c = 1 
while c < 10:
    print(c)
    c = c + 1
print('FIM')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM!')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r =str(input('Quer continuar? [S/N] ')).upper()
print('FIM!')'''

'''FOR é utilizado quando se sabe a quantidade das repetições
   WHILE é utilizado quando não se sabe a quatidade das repetições '''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))

    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números pares e {} números ímpares' .format(par, impar))
