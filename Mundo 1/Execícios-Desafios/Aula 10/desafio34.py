antigo = float(input('Qual o seu salário atualmente? '))
if antigo > 1250:
    print('Seu novo salário sofrerá um aumento de 10% e passará a ser {:.1f}'.format(1.1 * antigo))
else:
    print('Seu novo salário sofrerá um aumento de 15% e passará a ser {:.1f}'.format(1.15 * antigo))


#Outro jeito de fazer isso
antigo = (float(input('Qual é o seu salário atualmente? ')))
if antigo <= 1250:
    novo = antigo + (antigo * 15 / 100)
else:
    novo = antigo + (antigo * 10 / 100)
print('Já que você ganhava {} reais, passará a ganhar {} reais agora.'.format(antigo, novo))