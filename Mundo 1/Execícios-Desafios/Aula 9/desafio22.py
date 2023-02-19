nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print('Seu nome tem ao todo', len(nome) - nome.count(' '), 'letras')
print('Seu primeiro nome tem', nome.find(' '), 'letras')


#Outra forma de fazer a última parte 
blocos = nome.split()
print('Seu primeiro nome tem {} letras' . format(len(blocos [0])))