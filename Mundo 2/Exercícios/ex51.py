print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for pa in range (a1, a1+r*9+1, r):
    print(pa, end=' → ')
print('FIM')