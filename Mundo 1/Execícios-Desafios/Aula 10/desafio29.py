vel = float(input('Qual a sua velocidade em km/h? '))
if vel > 80:
    multa = 7 * (vel - 80)
    print('Você ultrapasssou a velocidade permitida, portanto receberá uma multa de {} reais.'.format(multa)) 
else:
    multa = 0 
    print('Você está dentro da velocidade permitida.')
if vel == 80:
    print('ATENÇÃO!!! Você está no limite da velocidade, precisa reduzí-la para evitar uma multa.')