r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and r1 == r2 == r3:
    print('É possível formar um triângulo equilátero')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and r1 == r2 or r1 == r3 or r2 == r3:
    print('É possível formar um triângulo isósceles')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and r1 != r2 != r3 != r1:
    print('É possível formar um triêngulo escaleno')
else:
    print('Não é possível formar um triângulo')