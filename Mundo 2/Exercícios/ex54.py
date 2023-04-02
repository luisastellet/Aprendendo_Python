from datetime import date
menor = 0
maior = 0

for pess in range(1, 8):
    nasc = int(input('Em qual ano a {}° pessoa nasceu? ' .format(pess)))
    atual = date.today().year
    idade = atual - nasc
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade \nE também tivemos {} pessoas menores de idade' .format(maior, menor))