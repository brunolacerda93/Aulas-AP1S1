# Exercícios da aula de Matrizes de Algorítmos e Programação - ADS IFSP 01/2022

from os import system

def menu(opc):
    match opc:
        case '1':
            ex_1(); system('pause')
        case '2':
            ex_2(); system('pause')
        case '4':
            ex_4(); system('pause')
        case '5':
            ex_5(); system('pause')
        case '6':
            ex_6(); system('pause')
        case _ :
            return 0

def ex_1():
    print("1. Crie um programa que solicita do usuário um valor N representando a quantidade linhas e um valor M representando a quantidade de colunas de uma matriz. Depois, o programa deverá solicitar do usuário N x M elementos para serem incluídos na matriz. Por fim, o programa deverá percorrer a matriz para encontrar e imprimir o seu maior elemento e o seu menor elemento.\n")

    n = int(input("Digite a quantidade de linhas da Matriz : "))
    m = int(input("Digite a quantidade de colunas da Matriz: "))
    
    matrix = []
    for i in range(n):
        line = []
        print(f"\nDigite os elementos da linha {i+1}:\n")
        for j in range(m):
            x = int(input(f"Digite o elemento {j+1}: "))
            line.append(x)
        matrix.append(line)

    system('cls')
    print("1. Crie um programa que solicita do usuário um valor N representando a quantidade linhas e um valor M representando a quantidade de colunas de uma matriz. Depois, o programa deverá solicitar do usuário N x M elementos para serem incluídos na matriz. Por fim, o programa deverá percorrer a matriz para encontrar e imprimir o seu maior elemento e o seu menor elemento.\n")

    print("Eis a Matriz:\n")
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

    maior = menor = matrix[0][0]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > maior:
                maior = matrix[i][j]
            elif matrix[i][j] < menor:
                menor = matrix[i][j]

    print("\nEis o maior elemento:", maior)
    print("Eis o menor elemento:", menor, "\n")

def ex_2():
    print("2. Faça um programa que solicite do usuário um valor N, representando a dimensão de uma matriz quadrada (matriz A). Em seguida, o programa deverá solicitar do usuário os elementos da matriz A e, posteriormente, deverá criar a matriz transposta de A (At). Ao final, deve ser mostrada a matriz original e sua respectiva transposta. Lembre-se que a matriz transposta At será obtida a partir da matriz A trocando-se ordenadamente as linhas por colunas (ou as colunas por linhas).\n")

    n = int(input("Digite a dimensão da Matriz quadrada: "))

    matrix = []
    for i in range(n):
        line = []
        print(f"\nDigite os elementos da linha {i+1}:\n")
        for j in range(n):
            x = int(input(f"Digite o elemento {j+1}: "))
            line.append(x)
        matrix.append(line)

    system('cls')
    print("2. Faça um programa que solicite do usuário um valor N, representando a dimensão de uma matriz quadrada (matriz A). Em seguida, o programa deverá solicitar do usuário os elementos da matriz A e, posteriormente, deverá criar a matriz transposta de A (At). Ao final, deve ser mostrada a matriz original e sua respectiva transposta. Lembre-se que a matriz transposta At será obtida a partir da matriz A trocando-se ordenadamente as linhas por colunas (ou as colunas por linhas).\n")
    
    print("Eis a Matriz Original:\n")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

    print("\nEis a Matriz Transposta:\n")
    for i in range(n):
        for j in range(n):
            print(matrix[j][i], end=" ")
        print()

    print()

def ex_4():
    print("4. Faça um programa que solicite do usuário um valor N, representando a dimensão de uma matriz quadrada (matriz A). Em seguida, o programa deverá solicitar do usuário os elementos da matriz A e, posteriormente, deverá verificar se A é simétrica. Obs: Matriz simétrica: matriz quadrada de ordem n tal que A = At\n")

    n = int(input("Digite a dimensão da Matriz quadrada: "))

    matrix = []
    for i in range(n):
        line = []
        print(f"\nDigite os elementos da linha {i+1}:\n")
        for j in range(n):
            x = int(input(f"Digite o elemento {j+1}: "))
            line.append(x)
        matrix.append(line)

    system('cls')
    print("4. Faça um programa que solicite do usuário um valor N, representando a dimensão de uma matriz quadrada (matriz A). Em seguida, o programa deverá solicitar do usuário os elementos da matriz A e, posteriormente, deverá verificar se A é simétrica. Obs: Matriz simétrica: matriz quadrada de ordem n tal que A = At\n")
    
    print("A Matriz:\n")
    flag = True
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
            if matrix[j][i] != matrix[i][j]:
                flag = False
        print()

    if flag:
        print("\nÉ simétrica!\n")
    else:
        print("\nNão é simétrica...\n")

def ex_5():
    print("5. Escreva um programa que leia inteiros positivos M e N e os elementos de uma matriz A de números inteiros de dimensão M x N e ao final mostra a quantidade de linhas e colunas que tem apenas zeros (linhas nulas e colunas nulas).\n")

    n = int(input("Digite a quantidade (N) de linhas da Matriz : "))
    m = int(input("Digite a quantidade (M) de colunas da Matriz: "))
    
    matrix = []
    for i in range(n):
        line = []
        print(f"\nDigite os elementos da linha {i+1}:\n")
        for j in range(m):
            x = int(input(f"Digite o elemento {j+1}: "))
            line.append(x)
        matrix.append(line)

    system('cls')
    print("5. Escreva um programa que leia inteiros positivos M e N e os elementos de uma matriz A de números inteiros de dimensão M x N e ao final mostra a quantidade de linhas e colunas que tem apenas zeros (linhas nulas e colunas nulas).\n")

    line_count = column_count = 0

    for i in range(n):
        soma = 0
        for j in range(m):
            soma += matrix[i][j]
        if soma == 0:
            line_count += 1

    for i in range(m):
        soma = 0
        for j in range(n):
            soma += matrix[j][i]
        if soma == 0:
            column_count += 1

    print("Na Matriz:\n")
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

    print("\nHá", line_count, "linhas nulas.")
    print("Há", column_count, "colunas nulas.\n")

def ex_6():
    print("6. Escreva um programa que leia inicialmente os elementos de 2 matrizes, de dimensões M linhas x N colunas e P linhas x Q colunas, fornecidas pelo usuário. Ao final o programa deve mostrar a matriz 1 (MxN), a matriz 2 (PxQ) e a matriz produto (MxQ).\n")

    print("Matriz A")
    n = int(input("Digite a quantidade (N) de linhas da Matriz : "))
    m = int(input("Digite a quantidade (M) de colunas da Matriz: "))
    
    matrix_A = []
    for i in range(n):
        line = []
        print(f"\nDigite os elementos da linha {i+1}:\n")
        for j in range(m):
            x = int(input(f"Digite o elemento {j+1}: "))
            line.append(x)
        matrix_A.append(line)

    system('cls')
    print("6. Escreva um programa que leia inicialmente os elementos de 2 matrizes, de dimensões M linhas x N colunas e P linhas x Q colunas, fornecidas pelo usuário. Ao final o programa deve mostrar a matriz 1 (MxN), a matriz 2 (PxQ) e a matriz produto (MxQ).\n")

    print("Matriz B")
    p = int(input("Digite a quantidade (P) de linhas da Matriz : "))
    if p != m:
        print("oh gee!")
        return 0
    
    q = int(input("Digite a quantidade (Q) de colunas da Matriz: "))
    
    matrix_B = []
    for i in range(p):
        line = []
        print(f"\nDigite os elementos da linha {i+1}:\n")
        for j in range(q):
            x = int(input(f"Digite o elemento {j+1}: "))
            line.append(x)
        matrix_B.append(line)

    system('cls')
    print("6. Escreva um programa que leia inicialmente os elementos de 2 matrizes, de dimensões M linhas x N colunas e P linhas x Q colunas, fornecidas pelo usuário. Ao final o programa deve mostrar a matriz 1 (MxN), a matriz 2 (PxQ) e a matriz produto (MxQ).\n")

    print("Matriz A:\n")
    for i in range(n):
        for j in range(m):
            print(matrix_A[i][j], end=" ")
        print()
    
    print("\nMatriz B:\n")
    for i in range(p):
        for j in range(q):
            print(matrix_B[i][j], end=" ")
        print()

    print("\nMatriz A x B:\n")
    matrix_prod = []
    for i in range(n):
        line = []
        for j in range(q):
            x = 0
            for k in range(p):
                x += matrix_A[i][k]*matrix_B[k][j]
            line.append(x)
        matrix_prod.append(line)

    for i in range(n):
        for j in range(q):
            print(matrix_prod[i][j], end=" ")
        print()
    print()

while True:
    system('cls')
    print("LISTAS")
    print(" 1 - Exercício 01")
    print(" 2 - Exercício 02")
    print(" Ø - Exercício 03")
    print(" 4 - Exercício 04")
    print(" 5 - Exercício 05")
    print(" 6 - Exercício 06")
    print("Digite 0 para encerrar!")
    opc = input("Escolha: ")

    if opc == '0':
        break
    else:
        system('cls')
        menu(opc)
