ano = int(input('Em qual ano você nasceu? '))
idade = 2023 - ano

if idade < 18:
    print('Você ainda irá se alistar no exército')
    print ('Faltam {} anos para isso' .format(18 - idade))
elif idade == 18:
    print('Está na hora de você se alistar no exército')
else:
    print('Já passou o seu alistamento')
    print('Já se passaram {} anos do seu alistamento' .format(idade - 18))