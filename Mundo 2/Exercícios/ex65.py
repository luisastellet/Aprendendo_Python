soma = 0
cont = 0
quer = 'a'
maior = 0
menor = 0

while quer != 'N':
    n = int(input('Digite um número: '))
    quer = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
    soma += n
    media = soma / cont
    if cont <= 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        else:
            menor = n

print('Você digitou {} números e a média foi {}' . format(cont, media))
print('O maior número foi {} e o menor número foi {}' .format(maior, menor))