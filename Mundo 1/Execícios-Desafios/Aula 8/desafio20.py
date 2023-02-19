import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
alunos = [a1, a2, a3, a4]
print('A ordem dos alunos será essa: {}' .format(random.choices(alunos, k=4)))


#Outra forma de fazer isso
import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
alunos = [a1, a2, a3, a4]
ordem = random.shuffle(alunos)
print('A ordem dos alunos será essa: {}' .format(ordem))
