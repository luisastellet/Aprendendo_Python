print(3**5)


print(81**(1/2))
print(81**1/2)
#Esse segundo caso dá errado porque a exponenciação tem prioridade frente à divisão, o que faz com que ocorra 81 elevado a 1 dividido por 2 == 40.5
#Já no primeiro caso, com os parênteses, primeiro faz-se a divisão do 1 pelo dois e depois eleva o 81 a 0.5 == 9
#Raiz quadrada == **(1/2) | Raiz cúbica == **(1/3)

print('Oi'*3)

nome = input('Qual o seu nome? ')
print('Parzer em te conhecer, {:=^20}!'.format(nome))



#Números
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multiplicação = n1 * n2
divisão = n1 / n2 
div_inteira = n1 // n2
exponeciação = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.1f}.' .format(soma, multiplicação, divisão), end=' ')
print('A divisão inteira é {} e a potência é {}' .format(div_inteira, exponeciação))