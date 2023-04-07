import random
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
comp = random.choice(n)

user = 1
palpite = 0
print(comp)
while user != comp:
    user = int(input('Chute qual número foi sorteado: '))
    palpite += 1
    if user == comp + 1 or user == comp + 2:
        print('=== Desce um pouco esse valor ===')
    elif user == comp - 1 or user == comp - 2:
        print('=== Sobe um pouco esse valor ===')
print('PARABÉNSSSS! VOCÊ ACERTOU! Você precisou de {} palpites para acertar.' .format(palpite))
