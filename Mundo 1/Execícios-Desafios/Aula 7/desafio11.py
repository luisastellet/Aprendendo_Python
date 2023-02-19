lar = float(input('Qual a largura (em metros) da sua parede? '))
com = float(input('Qual o comprimento (em metros) da sua parede? '))
area = lar * com
litros = area / 2 
#1 litros custa 5 reais
custo = litros * 5
print('Você precisará comprar {:.0f} litros de tinta para cobrir a sua parede de {:.0f}m², logo gastará {:.0f} reais.'.format(litros, area, custo))