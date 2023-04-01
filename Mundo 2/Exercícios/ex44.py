valor = int(input('Qual o valor da compra? '))
print('''Digite o número correspondente à forma de pagamento desejada: \n1 - À vista no dinheiro ou cheque \n2 - À vista no cartão \n3 - Em até 2 vezes no cartão \n4 - 3 vezes ou mais no cartão''' )
pag = int(input('Digite o número: '))

if pag == 1:
    print('Você pagará {}' .format(0.9 * valor))
elif pag == 2:
    print('Você pagará {}' .format(0.95 * valor))
elif pag == 3:
    print('Você pagará {}' .format(valor))
elif pag == 4:
    print('Você pagará {}' .format(1.2 * valor))
else:
    print('Selecione uma forma de pagamento')