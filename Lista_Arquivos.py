# Exercícios da Lista de Arquivos de Algorítmos e Programação - ADS IFSP 01/2022

from os import system
import random
import string

# Função para filtrar uma string para int
def digitos(array):
    novoArray = ""
    if not array.isdigit():
        for i in array:
            if i in string.digits:
                novoArray += i
    else:
        return array

    if array == "" or novoArray == "":
        return 0
    else:
        return novoArray

def menu (opc):
    match opc:
        case '1':
            ex_1(); system('pause')
        case '2':
            ex_2(); system('pause')
        case _:
            return 0

def ex_1():
    # Inclui pessoa pesquisa
    def cadastraPessoa():
        pessoa = ""
        opc = input("\nSexo\n\n 1 - Masculino\n 2 - Feminino\n\nEscolha: ")
        if   opc == '1': pessoa += "masculino "
        elif opc == '2': pessoa += "feminino "
        
        idade = digitos(input("\nIdade [em anos]: "))
        pessoa += idade + " "
        
        opc = input("\nFumante?\n\n 1 - SIM\n 2 - NÃO\n\nEscolha: ")
        if   opc == '1': pessoa += "sim "
        elif opc == '2': pessoa += "não "
        
        opc = input("\nEscolaridade:\n\n 1 - Fundamental\n 2 - Médio\n 3 - Superior\n\nEscolha: ")
        if   opc == '1': pessoa += "fundamental\n"
        elif opc == '2': pessoa += "médio\n"
        elif opc == '3': pessoa += "superior\n"
        
        arq = open("pesquisa.txt", "a")
        arq.write(pessoa)
        arq.close()
        print()

    # Lê o arquivo pesquisa.txt
    def lerPessoas():
        Pessoas = []
        pessoa = []
        arq = open("pesquisa.txt", "r")
        line = arq.readline()
        while line:
            if line != "":
                dados = line.split()
                if   dados[0] == 'masculino':   pessoa.append(1)
                elif dados[0] == 'feminino' :   pessoa.append(2)
                
                pessoa.append(int(dados[1]))
                
                if   dados[2] == 'sim':         pessoa.append(1)
                elif dados[2] == 'não':         pessoa.append(2)
                
                if   dados[3] == 'fundamental': pessoa.append(1)
                elif dados[3] == 'médio'      : pessoa.append(2)
                elif dados[3] == 'superior'   : pessoa.append(3)
                
                Pessoas.append(pessoa[:]);      pessoa.clear()
            line = arq.readline()
        arq.close()
        return Pessoas

    # Relatório fumantes
    def relatorioFumantes():
        Pessoas = lerPessoas()
        
        count = 0
        for pessoa in Pessoas:
            if pessoa[2] == 1:
                count += 1
        print(f"Das {len(Pessoas):2n} pessoas  entrevistadas, {count/len(Pessoas)*100:4.1f}% são fumantes")

        count = 0; count1 = 0
        for pessoa in Pessoas:
            if pessoa[0] == 1:
                count1 += 1
                if pessoa[2] == 2 and pessoa[1] < 40:
                    count += 1
        print(f"Dos {count1:2n} homens   entrevistados, {count/count1*100:4.1f}% possuem menos de 40 anos e não são fumantes")

        count = 0; count1 = 0
        for pessoa in Pessoas:
            if pessoa[0] == 2:
                count1 += 1
                if pessoa[2] == 1 and pessoa[1] > 40:
                    count += 1
        print(f"Das {count1:2n} mulheres entrevistadas, {count/count1*100:4.1f}% possuem mais  de 40 anos e são fumantes")
        print()
    
    # Corpo da função
    arq = open("pesquisa.txt", "a")
    arq.write("masculino 23 não superior\nfeminino 45 sim médio\n")
    arq.close()

    opc = ""
    while opc != 'n' and opc != 'N':
        system('cls')
        print("EXERCÍCIO 01\n")
        relatorioFumantes()
        opc = input("Deseja cadastrar uma pessoa? [n/N] ")
        if opc != 'n' and opc != 'N':
            cadastraPessoa(); system('pause')
    print()

def ex_2():
    # Inclui voto
    def cadastraVoto():
        opc = input("Pressione Enter para um voto aleatório ou digite o número do candidato: ")
        if opc == "":
            voto = random.randint(1, 6)*100
        else:
            voto = int(digitos(opc))
        
        arq = open("votos.txt", "a")
        arq.write(str(voto) + "\n")
        arq.close()
        
        print("Seu voto:", voto, "\n")

    # Lê o arquivo votos.txt
    def lerVotos():
        votos = []
        arq = open("votos.txt", "r")
        line = arq.readline()
        while line:
            if line != "":
                votos.append(int(line))
            line = arq.readline()
        arq.close()
        return votos

    # Relatório votos
    def relatorioVotos():
        votos = lerVotos()
        Votos = {'100': 0, '200': 0, '300': 0, '400': 0, '500': 0, 'Nulos': 0}
        for voto in votos:
            if   voto == 100: Votos['100'] += 1
            elif voto == 200: Votos['200'] += 1
            elif voto == 300: Votos['300'] += 1
            elif voto == 400: Votos['400'] += 1
            elif voto == 500: Votos['500'] += 1
            else: Votos['Nulos'] += 1
        print()

        for key in Votos.keys():
            print(f"{key}\t{Votos[key]:2n} votos")
        print()

        maior = '100'
        for key in Votos.keys():
            if key != 'Nulos' and Votos[key] > Votos[maior]:
                maior = key
        print(f"O candidato mais  votado foi {maior}, com {Votos[maior]:2n} votos")

        menor = '100'
        for key in Votos.keys():
            if key != 'Nulos' and Votos[key] < Votos[menor]:
                menor = key
        print(f"O candidato menos votado foi {menor}, com {Votos[menor]:2n} votos")
        print()

    # Corpo da função
    arq = open("votos.txt", "w")
    for i in range(1000):
        arq.write(str(random.randint(1, 6)*100) + "\n")
    arq.close()

    opc = ""
    while opc != 'n' and opc != 'N':
        system('cls')
        print("EXERCÍCIO 02")
        relatorioVotos()
        opc = input("Deseja registrar um voto? [n/N] ")
        if opc != 'n' and opc != 'N':
            cadastraVoto(); system('pause')
    print()

while True:
    system('cls')
    print("ARQUIVOS")
    print("1 - EXERCÍCIO 01")
    print("2 - EXERCÍCIO 02")
    print("0 - Encerrar")
    opc = input("Escolha: ")
    if opc == '0':
        break
    else:
        menu(opc)
