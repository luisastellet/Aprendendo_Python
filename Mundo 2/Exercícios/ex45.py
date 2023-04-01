import random 
nome = input('Qual o seu nome? ')
j1 = input('Você quer pedra, papel ou tesoura? ')
opçoes = ['papel', 'pedra', 'tesoura']
j2 = random.choice(opçoes)
a = 'pedra'
b = 'papel'
c = 'tesoura'

print(nome, 'escolheu {} e o outro jogador escolheu {}' .format(j1, j2))

if j1 == a and j2 == c:
    print(nome, 'ganhou')
elif j1 == c and j2 == a:
    print (nome, 'perdeu')
elif j1 == c and j2 == b:
    print(nome, 'ganhou')
elif j1 == b and j2 == c:
    print (nome, 'perdeu')
elif j1 == b and j2 == a:
    print(nome, 'ganhou')
elif j1 == a and j2 == b:
    print (nome, 'perdeu')
elif j1 == j2:
    print('O jogo empatou')

