nome = str(input('Digite o seu nome completo: ')).strip()
blocos = nome.split()
print('Primeiro nome: {}' .format(blocos[0]))
print('Último nome: {}' .format(blocos[len(blocos)-1]))