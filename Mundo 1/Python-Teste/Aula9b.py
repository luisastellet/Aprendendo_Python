mat = int(input('Qual a sua nota em Matemática? '))
port = int(input('Qual a sua nota em Português? '))
bio = int(input('Qual a sua nota em biologia? '))
hist = int(input('Qual a sua nota em história? '))
media = (mat + port + bio + hist) / 4
if media >= 6:
    print('PARABÉNS!!! Você foi aprovado com a média {}!'.format(media))
else: 
    print('Precisa estudar mais da próxima vez!! Você repetiu de ano com a média {}.'.format(media))