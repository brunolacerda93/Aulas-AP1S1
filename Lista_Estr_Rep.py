# Exercícios da Lista de Estruturas de Repetição de Algorítmos e Programação - ADS IFSP 01/2022

from os import system

def menu(opc):
    match opc:
        case '1':
            ex_1(); system('pause')
        case '2':
            ex_2(); system('pause')
        case '3':
            ex_3(); system('pause')
        case '4':
            ex_4(); system('pause')
        case '5':
            ex_5(); system('pause')
        case '6':
            ex_6(); system('pause')
        case '7':
            ex_7(); system('pause')
        case '8':
            ex_8(); system('pause')
        case '9':
            ex_9(); system('pause')
        case '10':
            ex_10(); system('pause')
        case _ :
            return 0

def ex_1():
    print("1. Faça um programa que exiba todos os números de 1 a 100 que são divisíveis por 7.\n")

    for i in range(1, 101):
        if i%7 == 0:
            print(i, end=" ")
    print("\n")

def ex_2():
    print("2. Faça um programa que exiba todos os números de 1 a 100 que são divisíveis por 7 e por 3.\n")

    for i in range(1, 101):
        if i%21 == 0:
            print(i, end=" ")
    print("\n")

def ex_3():
    print("3. Faça um programa para mostrar a tabuada de um número qualquer fornecido pelo usuário. Por exemplo, se o número fornecido for igual a 3, o programa de apresentar a seguinte saída:\n\n1 x 3 = 3\n2 x 3 = 6\n3 x 3 = 9\n4 x 3 = 12\n5 x 3 = 15\n6 x 3 = 18\n7 x 3 = 21\n8 x 3 = 24\n9 x 3 = 27\n")

    n = int(input("Digite um número: "))
    print()
    for i in range(1, 10):
        print(i, "x", n, "=", n*i)
    print()

def ex_4():
    print("4. Faça um programa para mostrar as tabuadas de todos os números de 1 a 10.\n")

    for i in range(1, 11):
        for j in range(1, 10):
            print(j, "x", i, "=", j*i)
        print()

def ex_5():
    print("5. Faça um programa que receba um número inteiro maior que 1, verifique se o número é primo ou não e mostre a mensagem de número primo ou de número não primo. Obs: Um número é primo quando é divisível apenas por 1 e por ele mesmo.\n")

    n = int(input("Digite um número: "))
    flag = True
    i = 2
    h = (n+1)/2
    while i < h and flag:
        if n%i == 0:
            flag = False
        i += 1
    
    if flag:
        print("\nÉ primo!\n")
    else:
        print("\nNão é primo!\n")

def ex_6():
    print("6. Faça um programa em Python que receba dois valores inteiros, representando a base e o expoente. O programa deverá calcular e apresentar o resultado da base elevada ao expoente. Por exemplo, para base = 5 e expoente = 3, ou seja, 5³, o programa deverá imprimir 125.\nObs: não utilize o operador de exponenciação (**). Utilize somente estrutura de repetição.\n")

    base = int(input("Digite a base: "))
    exp = int(input("Digite o expoente: "))

    pot = 1
    for i in range(0, exp):
        pot *= base
        # i += 1 <- no "for" esta linha é redundante, porém necessária no "while"

    print(f"\n{base}^{exp} = {pot}\n")

def ex_7():
    print("7. Faça um programa em Python que leia um conjunto de valores correspondentes às notas que os alunos obtiveram em uma prova de Algoritmos. Quando o valor fornecido for um número negativo, significa que não existem mais notas para serem lidas. Após isso seu programa deverá:\n• Escrever quantas notas são maiores ou iguais a 6.0\n• Escrever quantas notas são maiores ou iguais a 4.0 e menores que 6.0\n• Escrever quantos notas são menores que 4.0\n• Escrever a média das notas fornecidas pelo usuário.\n")

    # Minha resolução com Vetor
    n = 1
    nota = 0.0
    notas = []
    while nota >= 0.0:
        nota = float(input(f"Digite a nota {n}: "))
        if nota >= 0.0:
            notas.append(nota)
        n += 1
    
    system('cls')
    print("7. Faça um programa em Python que leia um conjunto de valores correspondentes às notas que os alunos obtiveram em uma prova de Algoritmos. Quando o valor fornecido for um número negativo, significa que não existem mais notas para serem lidas. Após isso seu programa deverá:\n• Escrever quantas notas são maiores ou iguais a 6.0\n• Escrever quantas notas são maiores ou iguais a 4.0 e menores que 6.0\n• Escrever quantos notas são menores que 4.0\n• Escrever a média das notas fornecidas pelo usuário.\n")
    print(notas)
    
    print("\nNotas maiores ou iguais a 6.0:")
    for i in notas:
        if i >= 6.0:
            print("-", i)

    print("\nNotas maiores ou iguais a 4.0 e menores do que 6.0:")
    for i in notas:
        if i >= 4.0 and i < 6.0:
            print("-", i)

    print("\nNotas menores do que 4.0:")
    for i in notas:
        if i < 4.0:
            print("-", i)

    media = 0.0
    for i in notas:
        media += i
    print("\nMédia das notas:", media/len(notas))
    print("\n=================//================\n")

    # Resolução da professora sem Vetor
    # Note que sem vetor é impossível exibir as notas
    # Podemos apenas mostrar quantas atendem cada condição
    n = 0; x1 = 0; x2 = 0; x3 = 0
    nota = 0.0
    media = 0.0
    while nota >= 0.0:
        nota = float(input(f"Digite a nota {n+1}: "))
        if nota >= 0.0:
            n += 1
            media += nota
            if nota >= 6.0:
                x1 += 1
            elif nota >= 4.0 and nota < 6.0:
                x2 += 1
            elif nota < 4.0:
                x3 += 1

    print()
    print(x1, "notas são maiores ou iguais a 6.0")
    print(x2, "notas são maiores ou iguais a 4.0 e menores do que 6.0")
    print(x3, "notas são menores do que 4.0")
    print("\nMédia das notas:", media/n, "\n")

def ex_8():
    print("8. Faça um programa que mostre os 8 primeiros termos da sequência de Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...\n")

    # RESOLUÇÃO SEM VETOR
    termo0 = 0
    termo1 = 1
    print(f" {termo0}, {termo1}", end="")
    for i in range(2, 11):
        termo = termo0 + termo1
        print(",", termo, end="")
        termo0 = termo1
        termo1 = termo

    # RESOLUÇÃO COM VETOR
    fib = [0, 1]
    for i in range(2, 11):
        fib.append(fib[i-1] + fib[i-2])
        # fib[i] = fib[i-1] + fib[i-2] <- Isto é como seria a linha de cima em C
    print(f"\n\n{fib}\n")

def ex_9():
    print("9. Faça um programa que leia um número inteiro >= 0 e calcule o seu fatorial.\n")

    n = int(input("Digite um número: "))
    fat = 1
    for i in range(1, n+1):
        fat *= i

    print(f"\n{n}! = {fat}\n")

def ex_10():
    print("10. Faça um programa que receba um número N fornecido pelo usuário e mostre os N termos da série a seguir. Depois, imprima a soma total da série.\nS = 1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + N/M\n")

    n = int(input("Digite N: "))
    soma = 1
    print("\nS = 1", end="")
    for i in range(1, n):
        N = i+1
        M = 2*i+1
        print(f" + {N}/{M}", end="")
        soma += N/M
    print("\nS =", soma, "\n")

while True:
    system('cls')
    print("ESTRUTURAS DE REPETIÇÃO")
    print(" 1 - Exercício 01")
    print(" 2 - Exercício 02")
    print(" 3 - Exercício 03")
    print(" 4 - Exercício 04")
    print(" 5 - Exercício 05")
    print(" 6 - Exercício 06")
    print(" 7 - Exercício 07")
    print(" 8 - Exercício 08")
    print(" 9 - Exercício 09")
    print("10 - Exercício 10")
    print("Digite 0 para encerrar!")
    opc = input("Escolha: ")

    if opc == '0':
        break
    else:
        system('cls')
        menu(opc)
