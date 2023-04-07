sexo = str(input('Digite o seu sexo [M ou F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos, digite novamente [M ou F]: ')).upper()
print('Obrigada pela resposta!')
