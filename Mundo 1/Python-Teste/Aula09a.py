frase = 'Curso em Vídeo Python'
print(frase[2:17])
print(frase[:6])
print(frase[5:18:2])
print(frase[::3])


print('Look at the stars')
print('Look how they shine for you')
print('And everything you do')
print('Yeah, they were all yellow')

#Outra forma de fazer isso mais fácil e rápido
print("""Look at the stars
Look how they shine for you
And everything you do
Yeah, they were all yellow""")

print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))

dividido = frase.split()
print(dividido[2])
print(dividido[2][3])

print('-'.join(frase))
print(frase.replace('Python', 'JavaScrip'))
print('Curso' in frase)
print(frase.find('Python'))
print('Oie' in frase)
print(frase.find('Oie'))
print(frase.lower().find('vídeo'))
