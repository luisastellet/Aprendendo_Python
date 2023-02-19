import random
print('O computador escolherá um número aleatório entre 0 e 5 e você deverá tentar acertá-lo.')
lista = [0, 1, 2, 3, 4, 5]
num = random.choice(lista)
chute = int(input('Digite um número de 0 a 5: '))
if chute == num:
    print('PARABÉNS!!! Você acertou!! O número escolhido foi {}'.format(num))
else: 
    print('Vish... Você errou o número escolhido. Você chutou {}, mas na verdade era {}'.format(chute, num))