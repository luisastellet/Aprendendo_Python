ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Você está em um ano bissexto.')
else:
    print('Você não está em um ano bissexto.')


#Outra forma de fazer isso
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Você está em um ano bissexto.')
else:
    print('Você não está em um ano bissexto.')
