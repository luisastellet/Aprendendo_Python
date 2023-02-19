#escolhido = choice(alunos)
#print('O alunos sorteado para apagar o quadro foi: {}'.format(escolhido))

from random import choice
aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)
print('O alunos sorteado para apagar o quadro foi: {}'.format(escolhido))


#OUTRA FORMA DE FAZER ISSO 

#alunos = [aluno1, aluno2, aluno3, aluno4]
#print('O aluno escolhido foi: {}' .format(random.choice(alunos)))

import random
aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi: {}' .format(random.choice(alunos)))