import os
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #Função para selecionar números primos
    def print_primos(n):
        primos = [True] * (n+1)
        primos[0], primos[1] = False, False
        for i in range(2, int(n**0.5)+1):
            if primos[i]:
                for j in range(i*i , n+1, i):
                    primos[j] = False
        for i in range(n+1):
            if primos[i]:
                print(i)

    #Repetição para inserir o número máximo
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            numero = int(input("Os números primos entre 2 e "))
            break
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')
            input('\nPressione Enter para selcionar uma opção novamente ')
            continue

    #Função com o número definido
    print_primos(numero)

    saida = input('Pressione Enter ou S para sair ')
    if saida == 's' or saida == 'S':
        break
    else:
        continue