n1 = float(input('Qual a sua nota 1? '))
n2 = float(input('Qual a sua nota 2? '))
media = (n1 + n2) / 2

if media < 5.0:
    print('REPROVADO')
elif 5 < media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')