frase = str(input('Digite uma frase: ')).lower().strip()
print('Vezes que a letra A aparece: ', frase.count('a'))
print('A letra "a" aparece primeiramente na posição: ', frase.find('a')+1)
print('A letra "a" aparece por último na posição: ', frase.rfind('a')+1)
