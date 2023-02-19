dias = int(input('Por quantos dias esse carro foi alugado? '))
km = int(input('Quantos kilômetros foram percorridos? '))
c_aluguel = 60 * dias
c_km = 0.15 * km
total = c_aluguel + c_km
print('Você deverá pagar {:.0f} reais pelos dias alugados e {:.0f} reais pelos kilômetros rodados. Sua conta totalizou, então, {:.0f} reais.' .format(c_aluguel, c_km, total))