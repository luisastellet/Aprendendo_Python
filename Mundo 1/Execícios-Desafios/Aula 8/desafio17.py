import math
o = float(input('Qual o comprimento(cm) do cateto oposto do triângulo retângulo em questão? '))
a = float(input('Qual o comprimento(cm) do cateto adjacente do triângulo retângulo em questão? '))
h = (o**2) + (a**2) 
raiz = math.sqrt(h)
print('O comprimento da hipotenusa do triângulo retângulo em questão é {:.2f}cm' .format(raiz))

# Outra forma de fazer isso mais fácil e rápido
o = float(input('Qual o comprimento(cm) do cateto oposto do triângulo retângulo em questão? '))
a = float(input('Qual o comprimento(cm) do cateto adjacente do triângulo retângulo em questão? '))
h = math.hypot(o,a)
print('O comprimento da hipotenusa do triêngulo retângulo em questão é {:.2f}cm' .format(h))