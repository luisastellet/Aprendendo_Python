maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa? ' .format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso
print('O maior peso lido foi de {:.1f}Kg' .format(maior))
print('O menor peso lido foi de {:.1f}Kg.' .format(menor))