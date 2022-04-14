# Exercícios da Lista 1 de Algorítmos e Programação - ADS IFSP 01/2022

from os import system

def menu(opc):
    match opc:
        case '1':
            ex_1(); system('pause')
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
    print("1. Escreva um programa que remove a primeira ocorrência de uma letra de uma string. A string e a letra devem ser fornecidas pelo usuário.")
    print("2. Escreva um programa que remove todas as ocorrências de uma letra de uma string. A string e a letra devem ser fornecidas pelo usuário.\n")

    frase = input("Digite uma frase: ")
    letra = input("Digite uma letra para ser removida: ")

    #for i in range(len(frase)):
    #    if frase[i] == letra:
    #        nova_frase = frase[0:i] + frase[i+1:len(frase)]
    #        break

    i = 0
    flag = True
    nova_frase = frase
    while i < len(frase) and flag == True:
        if frase[i].lower() == letra.lower():
            nova_frase = frase[0:i] + frase[i+1:len(frase)]
            flag = False
        i += 1

    nova_frase_1 = ""
    for i in frase:
        if i.lower() == letra.lower():
            nova_frase_1 += ""
        else:
            nova_frase_1 += i

    print(f"\nRemovendo a primeira ocorrência de '{letra}': [{nova_frase}]")
    print(f"Removendo todas as ocorrências de  '{letra}': [{nova_frase_1}]")
    print(f"Removendo todas as ocorrências de  '{letra}':", frase.replace(letra, ""), "\n")

def ex_3():
    print("3. Escreva um programa que verifique se duas strings fornecidas pelo usuário são iguais e mostre o total de caracteres de cada uma delas. Diferencie letras maiúsculas das minúsculas.\n")

    frase_1 = input("Digite uma frase: ")
    frase_2 = input("Digite uma frase: ")

    if frase_1.replace(" ", "") == frase_2.replace(" ", ""):
        print("\nAs frases são iguais!")
    else:
        print("\nAs frases são diferentes!")

    print("\nA primeira frase possui:", len(frase_1.replace(" ", "")), "caracteres.")
    print("A segunda  frase possui:", len(frase_2.replace(" ", "")), "caracteres.\n")

def ex_4():
    print("4. Escreva um programa que reconhece se uma string é um palíndromo, ou seja, se lida do início para o fim é igual se lida do fim para o início. Exemplos: arara, ovo, reter, Renner e Miriam.\n")

    frase = input("Digite uma frase: ")

    nova_frase = ""
    for i in range(1, len(frase)+1):
        nova_frase += frase[-i]

    # for i in range(len(frase)):
    #    nova_frase += frase[len(frase)-i-1]

    if frase.replace(" ", "").lower() == nova_frase.replace(" ", "").lower():
        print(f"\nA frase [{frase.strip()}] é palíndromo!\n")
    else:
        print(f"\nA frase [{frase.strip()}] não é palíndromo!\n")

def ex_5():
    print("5. Faça um programa que recebe uma frase e retorna o número de palavras que a frase contém.\n")

    frase = input("Digite uma frase: ")

    if frase == "":
        count = 0
    else:
        count = 1

    for i in frase.strip():
        if i == " ":
            count+=1

    print(f"\nA frase [{frase.strip()}] possui", count, "palavras\n")

def ex_6():
    print("6. Faça um programa que solicite o nome do usuário e imprima-o na vertical e em formato de escada. Por exemplo, o nome “Fulano”, o programa deverá imprimir: \nF\nFu\nFul\nFula\nFulan\nFulano\n")

    nome = input("Digite seu nome: ")
    print()
    for i in range(len(nome)):
        print(nome[0:i+1])
    print()

def ex_7():
    print("7. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre-o de trás para frente utilizando somente letras maiúsculas.\n")

    nome = input("Digite seu nome: ")
    print()
    novo_nome = ""
    for i in range(len(nome)):
        novo_nome += nome[len(nome)-i-1]

    print(novo_nome.upper())
    print()

def ex_8():
    print("8. Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte a quantidade de espaços em branco e a quantidade de vezes que aparecem as vogais a, e, i, o, u.\n")
    
    frase = input("Digite uma frase: ")
    spc=0; a=0; e=0; i=0; o=0; u=0
    
    for j in frase.strip():
        if j == " ":
            spc += 1
        elif j == 'a' or j == 'A':
            a += 1
        elif j == 'e' or j == 'E':
            e += 1
        elif j == 'i' or j == 'I':
            i += 1
        elif j == 'o' or j == 'O':
            o += 1
        elif j == 'u' or j == 'U':
            u += 1
    
    print(f"\nNa frase: [{frase.strip()}] há", spc, "espaços em branco.\n")
    print("A vogal 'A' aparece", a, "vez(es)")
    print("A vogal 'E' aparece", e, "vez(es)")
    print("A vogal 'I' aparece", i, "vez(es)")
    print("A vogal 'O' aparece", o, "vez(es)")
    print("A vogal 'U' aparece", u, "vez(es)\n")

def ex_9():
    print("9. Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. Por exemplo, “Iracema” é um anagrama para “America”. Escreva um programa que decida se uma string é um anagrama de outra string, ignorando os espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, “a” = “A”.\n")
    NO_OF_CHARS = 256

    frase1 = input("Digite uma frase: ")
    frase2 = input("Digite uma frase: ")

    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    for i in frase1.replace(" ", "").lower():
        count1[ord(i)] += 1

    for i in frase2.replace(" ", "").lower():
        count2[ord(i)] += 1

    flag = True
    if len(frase1.replace(" ", "")) != len(frase2.replace(" ", "")):
        flag = False
    else:
        for i in range(NO_OF_CHARS):
            if count1[i] != count2[i]:
                flag = False
                break

    if flag:
        print("\nAs frases:\n\n", frase1.strip(), "\n", frase2.strip(), "\n\nSão anagramas!\n")
    else:
        print("\nAs frases:\n\n", frase1.strip(), "\n", frase2.strip(), "\n\nNão são anagramas!\n")

def ex_10():
    print("10. Escreva um programa que solicite ao usuário a entrada de um número inteiro positivo ou negativo e mostre a quantidade de dígitos desse número.\n")
    
    num = input("Digite um número: ")
    count = 0
    n = int(num)
    if n>0:
        while n>0:
            n //= 10
            count += 1
    else:
        while n<-1:
            n //= 10
            count += 1

    print("\nO número", num, "possui", count, "digitos")
    print("O número", num, "possui", len(num.replace("-", "")), "digitos\n")

while True:
    system('cls')
    print("LISTA 01 - STRINGS")
    print(" 1 - Exercício 01 e 02")
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
