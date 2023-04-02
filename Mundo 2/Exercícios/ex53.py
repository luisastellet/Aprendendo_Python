frase = str(input('Digite uma frase: ')).strip().upper() # .strip() faz tirar os espaços de antes e depois da frase e .upper() deixa tudo maiúsculo 
palavras = frase.split() # split() e join() separam em termos e juntam eles, eliminando espaços internos
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('Você digitou a frase {} que ao contrário fica {}' .format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!!!')
else:
    print('A frase digitada NÃO é um palíndromo!!!')