tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else: 
    print('Carro velho')
print('--FIM--')

#Outra forma mais simplificada de fazer
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')


#----------------------------------------------
nome = str(input('Qual é o seu nome? '))
if nome == 'Luisa':
    print('Que nome lindo!')
else: 
    print('Seu nome é muito normal :(')
print('Bom dia, {}!!' .format(nome))

