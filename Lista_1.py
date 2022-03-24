# Exercícios da Lista 1 de Algorítmos e Programação - ADS IFSP 01/2022

from os import system
from time import sleep

def timer():
    system('pause')
    #for i in range(4):
    #    print(4-i)
    #    sleep(1)

def menu(opc):
    match opc:
        case 'a':
            ex_1(); timer()
        case 'b':
            ex_3(); timer()
        case 'c':
            ex_4(); timer()
        case 'd':
            ex_5(); timer()
        case 'e':
            ex_6(); timer()
        case 'f':
            ex_7(); timer()
        case 'g':
            ex_8(); timer()
        case 'h':
            ex_9(); timer()
        case 'i':
            ex_10(); timer()
        case _ :
            return 0

def ex_1():
    print("1. Escreva um programa que remove a primeira ocorrência de uma letra de uma string. A string e a letra devem ser fornecidas pelo usuário.")
    print("2. Escreva um programa que remove todas as ocorrências de uma letra de uma string. A string e a letra devem ser fornecidas pelo usuário.\n")

    frase = input("Digite uma frase: ")
    letra = input("Digite uma letra para ser removida: ")

    for i in range(len(frase)):
        if frase[i] == letra:
            nova_frase = frase[0:i] + frase[i+1:len(frase)]
            break

    nova_frase_1 = ""
    for i in range(len(frase)):
        if frase[i] == letra:
            nova_frase_1 += ""
        else:
            nova_frase_1 += frase[i]

    print(nova_frase)
    print(frase.replace(letra, ""))
    print(nova_frase_1)

def ex_3():
    print("Escreva um programa que verifique se duas strings fornecidas pelo usuário são iguais e mostre o total de caracteres de cada uma delas. Diferencie letras maiúsculas das minúsculas.\n")

    frase_1 = input("Digite uma frase: ")
    frase_2 = input("Digite uma frase: ")

    if frase_1 == frase_2:
        print("As frases são iguais!")
    else:
        print("As frases são diferentes!")

    print("A primeira frase possui:", len(frase_1), "caracteres.")
    print("A segunda frase possui :", len(frase_2), "caracteres.")

def ex_4():
    print("Escreva um programa que reconhece se uma string é um palíndromo, ou seja, se lida do início para o fim é igual se lida do fim para o início. Exemplos: arara, ovo, reter, Renner e Miriam.\n")

    frase = input("Digite uma frase: ")

    nova_frase = ""
    for i in range(len(frase)):
        nova_frase += frase[len(frase)-i-1]

    if frase.lower() == nova_frase.lower():
        print("A frase '", frase, "' é palíndromo!")
    else:
        print("A frase '", frase, "' não é palíndromo!")

def ex_5():
    print("Faça um programa que recebe uma frase e retorna o número de palavras que a frase contém.\n")

    frase = input("Digite uma frase: ")

    if frase == "":
        count = 0
    else:
        count = 1

    for i in range(len(frase)):
        if frase[i] == " ":
            count+=1

    print("A frase '", frase, "' possui", count, "palavras")

def ex_6():
    print("Faça um programa que solicite o nome do usuário e imprima-o na vertical e em formato de escada. Por exemplo, o nome “Fulano”, o programa deverá imprimir: \nF\nFu\nFul\nFula\nFulan\nFulano\n")

    nome = input("Digite seu nome: ")

    for i in range(len(nome)):
        print(nome[0:i+1])

def ex_7():
    print("Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre-o de trás para frente utilizando somente letras maiúsculas.\n")

    nome = input("Digite seu nome: ")

    novo_nome = ""
    for i in range(len(nome)):
        novo_nome += nome[len(nome)-i-1]

    print(novo_nome.upper())

def ex_8():
    print("Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte a quantidade de espaços em branco e a quantidade de vezes que aparecem as vogais a, e, i, o, u.\n")

def ex_9():
    print("Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. Por exemplo, “Iracema” é um anagrama para “America”. Escreva um programa que decida se uma string é um anagrama de outra string, ignorando os espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, “a” = “A”.\n")

def ex_10():
    print("Escreva um programa que solicite ao usuário a entrada de um número inteiro positivo ou negativo e mostre a quantidade de dígitos desse número.\n")

while True:
    system('cls')
    print("LISTA 01")
    print("a - Exercício 01 e 02")
    print("b - Exercício 03")
    print("c - Exercício 04")
    print("d - Exercício 05")
    print("e - Exercício 06")
    print("f - Exercício 07")
    print("g - Exercício 08")
    print("h - Exercício 09")
    print("i - Exercício 10")
    print("Digite 0 para encerrar!")
    opc = input("Escolha: ")

    if opc == '0':
        break
    else:
        system('cls')
        menu(opc)
