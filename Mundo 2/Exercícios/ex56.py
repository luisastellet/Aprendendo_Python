somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheresnovas = 0

for p in range(1,5):
    print('----- {}° PESSOA ---' .format(p))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if sexo in 'Ff' and idade < 20:
        mulheresnovas += 1

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if idade > maioridadehomem and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

mediaidade = somaidade / 4

print('A média de idade do grupo é de {} anos' .format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}' .format(maioridadehomem, nomevelho))
print('{} mulheres têm menos de 20 anos' .format(mulheresnovas))