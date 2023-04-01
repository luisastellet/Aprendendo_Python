nome = str(input('Qual o seu nome? '))
if nome == 'luisa':
    print('Que nome bonito!')

elif nome == 'pedro' or nome == 'maria' or nome == 'ana':
    print('Seu nome é bem popular no Brasil')

elif nome in 'clara cláudia jéssica juliana':
    print('Belo nome feminino')
else: 
    print('Seu nome é bem normal')

print('Tenha um bom dia, {}' .format(nome))