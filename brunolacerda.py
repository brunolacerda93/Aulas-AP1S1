# Algorítimos e Programação AP1S1 - Prova 1 - 18/05/2022
# @author: Bruno Capelari de Lacerda SC3029492

from os import system
import random

def menu (opc):
    match (opc):
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
        case _:
            return 0

def ex_1():
    print("1.\n")
    L1 = [7, 132, 5, 28, -1, 69, -16] # [0 2 4 6 8 10 12] / [0 1 2 3 4 5 6] r = *2
    L2 = [0, -8, 267, 21, 9, 18, 755] # [1 3 5 7 9 11 13] / [0 1 2 3 4 5 6] r = *2 +1
    L3 = L1[:]

    #L1 = []
    #for i in range(7):
    #    L1.append(L3[i])
    #    L1.append(L2[i])

    L1 += [0, 0, 0, 0, 0, 0, 0]

    for i in range(7):
        x = i*2
        L1[x] = L3[i]
        y = (i*2)+1
        L1[y] = L2[i]

    print(L1)
    print()

def ex_2():
    print("2.\n")

    print("DIGITE UM NÚMERO NEGATIVO PARA ENCERRAR!")
    n = int(input("Digite números: "))
    num = [n]
    while n >= 0:
        n = int(input("Digite números: "))
        if n >= 0:
            num.append(n)

    print(num)
    pot = []
    for i in range(len(num)):
        pot.append(num[i]**i)

    soma = 0
    for i in pot:
        soma += i

    print(pot)
    print("Soma:", soma)
    print()

def ex_3():
    print("3.\n")
    word = input("Digite uma palavra: ")
    for i in range(len(word)+1):
        print(word[:i])
    for i in range(len(word)):
        print(word[0:len(word)-i])
    print()

def ex_4():
    print("4.\n")
    frase = input("Digite uma frase: ")
    fraseInv = ''
    for i in range(len(frase)):
        fraseInv += frase[-i-1]
    # print(fraseInv)

    stringA = frase.lower().strip().replace(" ", "").replace("-", "")
    stringB = fraseInv.lower().strip().replace(" ", "").replace("-", "")
    flag = True

    if len(stringA) != len(stringB):
        flag = False
    else:
        for i in range(len(stringA)):
            if stringA[i] != stringB[i]:
                flag = False

    print()
    if flag:
        print("É palíndromo!")
    else: 
        print("Não é palíndromo...")

    print()

def ex_5():
    print("5.\n")
    
    matrix = []
    line = []
    for i in range(3):
        line = random.sample(range(0, 20), 4)
        matrix.append(line)

    for line in matrix:
        for i in line:
            print(i, end=" ")
        print()

    menor = matrix[0][0]
    menorX = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < menor:
                menor = matrix[i][j]
                menorX = i

    maior = matrix[menorX][0]
    for i in matrix[menorX]:
        if i > maior:
            maior = i

    print()
    print("MINMAX:", maior)
    print()

while True:
    system('cls')
    print("PROVA 1")
    print("1 - EXERCÍCIO 01")
    print("2 - EXERCÍCIO 02")
    print("3 - EXERCÍCIO 03")
    print("4 - EXERCÍCIO 04")
    print("5 - EXERCÍCIO 05")
    opc = input("Escolha: ")
    if opc == '0':
        break
    else:
        system('cls')
        menu(opc)
