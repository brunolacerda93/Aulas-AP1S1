# Exercícios da Aula de Funções de Algorítmos e Programação - ADS IFSP 01/2022

from os import system
import random

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
        case '11':
            ex_11(); system('pause')
        case _ :
            return 0
            
def ex_1():
    print("1. Faça uma função InteiroPositivo(n) que verifica se uma string fornecida como parâmetro pode ser convertida para um número inteiro positivo. A função deverá retornar True em caso afirmativo e False, caso contrário. O programa principal deverá fazer a conversão para inteiro, caso o resultado da função seja True, ou imprimir a mensagem adequada, caso o resultado seja False.\n")

    n = input("Digite algo: ")
    if InteiroPositivo(n):
        print("\nConvertido para inteiro:", int(n))
    else:
        print("\nNão pode ser convertido para inteiro...")

    print()

def InteiroPositivo(n):
    return n.isdigit()

def ex_2():
    print("2. Faça uma função Inteiro(n) que verifica se uma string fornecida como parâmetro pode ser convertida para um número inteiro positivo ou negativo. A função deverá retornar True em caso afirmativo e False, caso contrário. O programa principal deverá fazer a conversão para inteiro, caso o resultado da função seja True, ou imprimir a mensagem adequada, caso o resultado seja False.\n")

    n = input("Digite algo: ")
    if Inteiro(n):
        print("\nConvertido para inteiro:", int(n))
    else:
        print("\nNão pode ser convertido para inteiro...")

    print()

def Inteiro(n):
    return n.replace("-", "").isdigit()

def ex_3():
    print("3. Faça uma função Real(n) que verifica se uma string fornecida como parâmetro pode ser convertida para um número real. A função deverá retornar True em caso afirmativo e False, caso contrário. O programa principal deverá fazer a conversão para inteiro, caso o resultado da função seja True, ou imprimir a mensagem adequada, caso o resultado seja False.\n")

    n = input("Digite algo: ")
    if Real(n):
        print("\nConvertido para real:", float(n))
    else:
        print("\nNão pode ser convertido para real...")

    print()

def Real(n):
    return n.replace("-", "").replace(".", "").isdigit()

def ex_4():
    print("4. Crie uma função que receba como parâmetro um número inteiro. A função deve retornar um número inteiro, conforme a seguir:\n a) Retornar 1 se o número recebido é positivo\n b) Retornar -1 se o número recebido é negativo\n c) Retornar 0 se o número recebido é zero\n")

    n = input("Digite algo: ")
    if Inteiro(n):
        print(Polaridade(int(n)))
    else:
        print("\nOh gee, Rick")
    print()

def Polaridade(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def ex_5():
    print("5. Faça uma função que receba quatro valores reais (faça a consistência usando a função definida no exercício 3 ), referentes as notas que um aluno obteve nos bimestres. A função deve retornar a média final desse aluno.\n")

    n1 = input("Digite a 1ª nota: ")
    n2 = input("Digite a 2ª nota: ")
    n3 = input("Digite a 3ª nota: ")
    n4 = input("Digite a 4ª nota: ")
    print()

    if Real(n1) and Real(n2) and Real(n3) and Real(n4):
        print("Eis a média das notas:", Media(n1, n2, n3, n4))
    else:
        print("Você não digitou valores válidos para as notas...")
    
    print()

def Media(n1, n2, n3, n4):
    return (float(n1) + float(n2) + float(n3) + float(n4))/4

def ex_6():
    print("6. Faça uma função que calcule o fatorial de um número inteiro positivo fornecido como parâmetro. Use a função definida no exercício 1) para verificar se o número é inteiro positivo. A função deverá retornar o fatorial do número, ou False (caso não seja um inteiro positivo). O resultado (ou a mensagem) deve ser impresso pelo programa principal.\n")

    n = input("Digite um número: ")
    if InteiroPositivo(n):
        print(f"Eis {n}! =", Fatorial(n))
    else:
        print("Oh gee, Rick")
    print()
    
def Fatorial(n):
    fat = 1
    for i in range(1, int(n)+1): fat *= i
    return fat

def ex_7():
    print("7. Faça uma função que receba 2 listas de valores inteiros e retorne a lista UNIÃO.\n")

    lista1 = []
    lista2 = []

    for i in range(4): 
        lista1.append(random.randint(10, 100))
        lista2.append(random.randint(10, 100))

    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print()

    listaUniao = Uniao(lista1, lista2)
    print("Lista UNIÃO:", listaUniao, "\n")

def Uniao (lista1, lista2):
    return lista1 + lista2

def ex_8():
    print("8. Faça uma função que receba 2 listas de valores inteiros e retorne a lista INTERSECÇÃO\n")

    lista1 = []
    lista2 = []

    for i in range(10): 
        lista1.append(random.randint(10, 100))
        lista2.append(random.randint(10, 100))

    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print()

    listaInter = Interseccao(lista1, lista2)
    print("Lista INTERSECÇÃO:", listaInter, "\n")

def Interseccao(lista1, lista2):
    inter = []
    for i in lista1:
        if i in lista2:
            inter.append(i)
    return inter

def ex_9():
    print("9. Faça uma função que receba 2 listas de valores inteiros e retorne a lista DIFERENÇA.\n")

    lista1 = []
    lista2 = []

    for i in range(5): 
        lista1.append(random.randint(0, 9))
        lista2.append(random.randint(0, 9))

    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print()

    listaDif = Diferenca(lista1, lista2)
    print("Lista DIFERENÇA:", listaDif, "\n")

def Diferenca(lista1, lista2):
    dif = []
    listaInter = Interseccao(lista1, lista2)
    for i in Uniao(lista1, lista2):
        if i not in listaInter:
            dif.append(i)
    return dif

def ex_10():
    print("10. Faça uma função que receba 2 listas de valores inteiros, o modo de saída (U:união, I:intersecção, D:diferença) e retorne a lista resultante. Obs: a função deverá invocar as funções definida nos exercícios de 7 a 9, para calcular U, I ou D.\n")

    lista1 = []
    lista2 = []

    for i in range(5): 
        lista1.append(random.randint(0, 9))
        lista2.append(random.randint(0, 9))

    print("Lista 1:", lista1)
    print("Lista 2:", lista2)

    opr = input("\nDigite a operação: ")

    novaLista = ordem(lista1, lista2, opr)
    print("Eis a lista resultante:", novaLista)
    print()

def ordem(lista1, lista2, opr):
    print()
    if opr == 'u' or opr == 'U':
        print("Você escolheu UNIÃO")
        return Uniao(lista1, lista2)
    elif opr == 'i' or opr == 'I':
        print("Você escolheu INTERSECÇÃO")
        return Interseccao(lista1, lista2)
    elif opr == 'd' or opr == 'D':
        print("Você escolheu DIFERENÇA")
        return Diferenca(lista1, lista2)
    else:
        print("Operação Inválida!!!\n")
        return 0

def ex_11():
    print("11. Faça uma função que receba 2 strings e retorne Verdadeiro se a segunda string é um anagrama da primeira, ou Falso caso contrário.\n")

    frase1 = input("Digite uma frase: ")
    frase2 = input("Digite uma frase: ")
    print("\nAs frases:\n\n", frase1.strip(), "\n", frase2.strip(), "\n")

    if Anagrama(frase1, frase2):
        print("São anagramas!")
    else:
        print("Não são anagramas!")
    print()

def Anagrama(frase1, frase2):
    NO_OF_CHARS = 256
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    for i in frase1.replace(" ", "").lower():
        count1[ord(i)] += 1

    for i in frase2.replace(" ", "").lower():
        count2[ord(i)] += 1

    if len(frase1.replace(" ", "")) != len(frase2.replace(" ", "")):
        return False
    else:
        i = 0
        for i in range(NO_OF_CHARS):
            if count1[i] != count2[i]:
                return False

    return True

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
    print("11 - Exercício 11")
    print("Digite 0 para encerrar!")
    opc = input("Escolha: ")

    if opc == '0':
        break
    else:
        system('cls')
        menu(opc)
