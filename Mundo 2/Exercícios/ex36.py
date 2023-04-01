valor = int(input('Qual o valor da sua casa? '))
salario = int(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você pretende pagá-la? '))
parcela = valor / (anos * 12)

if parcela <= 0.3 * salario:
    print('Seu empréstimo foi aceito e o valor da sua parcela durante os próximos {} meses será de {} reais.' .format(anos * 12, parcela))
else:
    print('O seu empréstimo foi negado!')

print('O valor da sua parcela será de:' .format(parcela))