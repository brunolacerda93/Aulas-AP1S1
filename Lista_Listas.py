# Exercícios da Lista de "Listas" de Algorítmos e Programação - ADS IFSP 01/2022

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
        case _ :
            return 0

def ex_1():
    print("1. Gere uma lista de contendo os múltiplos de 3 entre 1 e 150.\n")

    three = list(range(3, 151, 3))
    print(three, "\n")

def ex_2():
    print("2. Crie um programa que leia inicialmente uma sequência de N notas de alunos fornecidas pelo usuário e ao final mostre a sequência e sua média aritmética. Defina um critério de parada para a entrada de notas pelo usuário.\n")

    n = 1
    nota = 0.0
    notas = []
    print("Digite um número negativo para encerrar!")
    while nota >= 0.0:
        nota = float(input(f"Digite a nota {n}: "))
        if nota >= 0.0:
            notas.append(nota)
        n += 1

    print("\n", notas)

    media = 0.0
    for i in notas:
        media += i

    if len(notas) > 0:
        print("\nMédia das notas:", media/len(notas), "\n")
    else:
        print("\nNenhuma nota foi digitada.\n")

def ex_3():
    print("3. Crie um programa que leia inicialmente uma sequência de N números inteiros e ao seu final mostre a sequência original, a soma de seus elementos que forem pares e a multiplicação dos elementos que forem ímpares.\n")
    
    n = int(input("Digite a quantidade de elementos da lista: "))
    nums = []
    for i in range(n):
        nums.append(int(input("Digite um número: ")))

    print("\nEis os números que foram digitados:\n", nums)

    soma = 0
    prod = 1
    for i in nums:
        if i%2 == 0:
            soma += i
        else:
            prod *= i

    print("\nSoma dos elementos pares:", soma)
    print("Produto dos elementos ímpares:", prod, "\n")

def ex_4():
    print("4. Crie um programa que leia inicialmente uma sequencia de N números inteiros. Depois, o programa deve gerar e mostrar 2 novas listas a partir da primeira: uma sem repetição de elementos e outra com os elementos que se repetem na lista original.\n")

    n = int(input("Digite a quantidade de elementos da lista: "))
    nums = []
    for i in range(n):
        nums.append(int(input(f"Digite o {i+1}° número: ")))

    print("\nEis os números que foram digitados:\n", nums)

    # RESOLUÇÃO COMO SERIA NA LINGUAGEM C

    # for i in range(len(nums)):
    #    for j in range(i+1, len(nums)):
    #        flag = False
    #        if nums[j] == nums[i]:
    #            for aux in rep:
    #                if aux == nums[i]:
    #                    flag = True
    #            if not flag:
    #                rep.append(nums[i])

    # for i in nums:
    #    flag = True
    #    for j in rep:
    #        if i == j:
    #            flag = False
    #    if flag:
    #        nrep.append(i)

    # RESOLUÇÃO EM PYTHON

    rep = []
    nrep = []
    array = []                      # Esse array serve apenas para registrar o array
    for i in nums:                  # com apenas uma ocorrência de cada elemento
        if i not in array:
            array.append(i)
        else:
            if i not in rep:
                rep.append(i)

    for i in nums:
        if i not in rep:
            nrep.append(i)

    print("\nEis os repetidos:\n", rep)
    print("\nEis os não repetidos:\n", nrep, "\n")

def ex_5():
    print("5. Crie um programa que leia inicialmente duas sequências de N elementos cada uma e ao final mostre as duas sequências originais e a sequência resultante da soma de seus elementos. Exemplo:\n\n   A = [5, 9, 0]\tB = [12, 34, 101]\tSoma = [17, 43, 101]")

    n = int(input("\nDigite a quantidade de elementos das sequências: "))

    print("\nSequência A")
    seqA = []
    for i in range(n):
        x = int(input(f"Digite o {i+1}° elemento: "))
        seqA.append(x)

    print("\nSequência B")
    seqB = []
    for i in range(n):
        x = int(input(f"Digite o {i+1}° elemento: "))
        seqB.append(x)

    soma = []
    for i in range(n):
        sum = seqA[i] + seqB[i]
        soma.append(sum)

    print("\nA =", seqA, "\nB =", seqB, "\nS =", soma, "\n")

def ex_6():
    print("6. Crie um programa que dada uma sequência de N elementos fornecidos pelo usuário mostre a sequência original e a sequência elevada ao cubo.\n")

    n = int(input("\nDigite a quantidade de elementos das sequências: "))
    seq = []
    for i in range(n):
        x = int(input(f"Digite o {i+1}° elemento: "))
        seq.append(x)

    cub = []
    for i in seq:
        cub.append(i**3)

    print("\nSequência original:\n", seq, "\n\nSequência ao cubo:\n", cub, "\n")

def ex_7():
    print("7. Crie um programa que leia inicialmente uma sequência de N números inteiros fornecidos pelo usuário e mostre ao final da leitura a sequência original e a sequência invertida.\n")

    n = int(input("Digite a quantidade de elementos das sequências: "))
    seq = []
    for i in range(n):
        x = int(input(f"Digite o {i+1}° elemento: "))
        seq.append(x)

    inv = []
    for i in range(1, len(seq)+1):
        inv.append(seq[-i])
    
    print("\nSequência original:\n", seq, "\n\nSequência invertida:\n", inv, "\n")

def ex_8():
    print("8. Crie um programa que leia inicialmente uma sequência de N elementos inteiros positivos fornecidos pelo usuário e substitua seus elementos de valor ímpar por -1 e os pares por +1. Ao final imprima a sequência original e a sequência alterada.\n")

    n = int(input("Digite a quantidade de elementos das sequências: "))
    seq = []
    for i in range(n):
        x = int(input(f"Digite o {i+1}° elemento: "))
        seq.append(x)

    nova = []
    for i in seq:
        if i%2 == 0:
            nova.append(1)
        else:
            nova.append(-1)

    print("\nSequência original:\n", seq, "\n\nSequência alterada:\n", nova, "\n")

while True:
    system('cls')
    print("LISTAS")
    print(" 1 - Exercício 01")
    print(" 2 - Exercício 02")
    print(" 3 - Exercício 03")
    print(" 4 - Exercício 04")
    print(" 5 - Exercício 05")
    print(" 6 - Exercício 06")
    print(" 7 - Exercício 07")
    print(" 8 - Exercício 08")
    print("Digite 0 para encerrar!")
    opc = input("Escolha: ")

    if opc == '0':
        break
    else:
        system('cls')
        menu(opc)
