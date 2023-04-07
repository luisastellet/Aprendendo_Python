from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

escolha = 0
while escolha != 5 and escolha <= 4:
    sleep(1.5)
    escolha = int(input('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa
    ========================
    Qual você quer? '''))
 
    if escolha == 1:
        print('A soma dos valores é', n1 + n2)
    elif escolha == 2:
        print('A multiplicação dos valores é', n1 * n2)
    elif escolha == 3:
        if n1 > n2:
            print('O maior valor é o', n1)
        else:
            print('O maior valor é o', n2)
    elif escolha == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um valor: '))

    

