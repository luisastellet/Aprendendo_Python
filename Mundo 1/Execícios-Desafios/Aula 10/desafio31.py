dist = float(input('Qual a distância da sua viagem (em km)? '))
if dist <= 200:
    print('A sua passagem custará {:.0f} reais, já que andará {:.0f}km e o custo é calculado pela distância vezes 0,50 reais.'.format(dist * 0.5, dist))
else:
    print('A sua passegm custará {:.0f} reais, já que andará {:.0f}km e o custo é calculado pela distância vezes 0,45 reais.'.format(dist * 0.45, dist))