import random
num = random.randint(1,10)
print(num)

# import math
# raiz = math.sqrt(num)
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}' .format(num, raiz))

# OUTRO JEITO DE FAZER A MESMA COISA
#from math import sqrt
#raiz = sqrt(num)
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}' .format(num, raiz))

import emoji
print(emoji.emojize("Olá, Mundo :sunglasses:", use_alises=True))
