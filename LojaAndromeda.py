# Projeto avaliativo - Algorítmos e Programação - ADS IFSP - 05/2022
# @author: Bruno Capelari de Lacerda SC3029492
# Tema 8: Controle de compras e vendas

# Bibliotecas
from os import system
import string

# Submenu genérico
def menu(x, lista):
    while True:
        safeCheck(lista)
        system('cls')
        print("=================== ANDROMEDA ===================")
        print("Seja bem vinde ao santuário da Rainha dos Homens\n")
        if x == '1': print("CLIENTES".center(48))
        elif x == '2': print("PRODUTOS".center(48))
        print()
        print(" 1 - Listar Todos".center(24))
        print(" 2 - Listar Um   ".center(24))
        print(" 3 - Incluir     ".center(24))
        print(" 4 - Alterar     ".center(24))
        print(" 5 - Excluir     ".center(24))
        print(" 0 - Retornar    ".center(24))
        print("\n(👁 ͜ʖ👁 )")
        opc = input("Escolha: ")
        if opc == '0':
            return 0
        elif opc >= '1' and opc <= '5':
            system('cls')
            subMenu(opc, x, lista)

# Opções do submenu - decisão
def subMenu(opc, x, lista):
    match opc:
        case '1':
            listaTodos(x, lista); system('pause')
        case '2':
            listaUm(x, lista); system('pause')
        case '3':
            incluir(x, lista); system('pause')
        case '4':
            alterar(x, lista)
        case '5':
            excluir(x, lista); system('pause')
        case _:
            return 0

# Função para leitura completa das listas
def listaTodos(x, lista):
    print("========================================")
    if x == '1':
        for i in range(len(lista)):
            listaCliente(lista, i)
    elif x == '2':
        for i in range(len(lista)):
            listaProduto(lista, i)
    print()

# Função para ler um elemento da lista de clientes
def listaCliente(lista, i):
    print("CLIENTE {n:02n}".format(n = i+1).center(40))
    print("CPF                :", end=" ")
    for j in range(0, len(lista[i][0])):
        print(lista[i][0][j], end="")
        if j == 2: print(".", end="")
        elif j == 5: print(".", end="")
        elif j == 8: print("/", end="")
    print()
    print("Nome               :", lista[i][1])
    print("Data de Nascimento :", lista[i][2])
    print("Sexo               :", lista[i][3])
    print("Salário           R$ {val:.2f}".format(val = lista[i][4]))
    print("E-mails            :", end=" ") 
    for j in range(0, len(lista[i][5])):
        if j == len(lista[i][5])-1:
            print(lista[i][5][j])
        else:
            print(lista[i][5][j], "\n\t\t   :", end=" ")
    print("Telefones          :", end=" ")
    for j in range(0, len(lista[i][6])):
        if j == len(lista[i][6])-1:
            print(lista[i][6][j])
        else:
            print(lista[i][6][j], "\n\t\t   :", end=" ")
    print("========================================")

# Função para ler um elemento da lista de produtos
def listaProduto(lista, i):
    print("PRODUTO {n:02n}".format(n = i+1).center(40))
    print("Código           :", lista[i][0])
    print("Descrição        :", lista[i][1])
    print("Peso (kg)        :", lista[i][2])
    print("Preço           R$ {val:.2f}".format(val = lista[i][3]))
    print("Desconto        R$ {val:.2f}".format(val = lista[i][4]))
    print("Data de Validade :", lista[i][5])
    print("========================================")

# Função para leitura de elemento individual
def listaUm(x, lista):
    i = int(input("Digite o elemento: "))
    print("\n========================================")
    if i <= len(lista) and i > 0:
        if x == '1': listaCliente(lista, i-1)
        elif x == '2': listaProduto(lista, i-1)
    else: print("\n", "Não há elemento neste índice!".center(36))
    print()

# Função para filtrar em uma string apenas números
def digitos(array):
    novoArray = ""
    if not array.isdigit():
        for i in array:
            if i in string.digits:
                novoArray += i
        return novoArray
    else:
        return array

# Função para converter uma string em float
def floating(array):
    novoArray = ""
    if not array.isdigit():
        for i in array:
            if i in string.digits or i in string.punctuation:
                novoArray += i
        return novoArray.replace(",", ".")
    else:
        return array

# Função para incluir elementos
def incluir(x, lista):
    if x == '1': lista.append(formCliente(lista))
    elif x == '2': lista.append(formProduto(lista))
    print()

# Formulário para adicionar Clientes
def formCliente(lista):
    form = []
    cpf = digitos(input("CPF: "))
    if percorreLista(cpf, lista) == -1:                                     # Teste para checar se o cpf já
        form.append(cpf)                                                    # consta na lista de clientes
        nome = input("Nome: "); form.append(nome)
        data = input("Data de Nascimento: "); form.append(data)
        sexo = input("Sexo: "); form.append(sexo)
        salario = float(floating(input("Salário: R$ "))); form.append(salario)
        email = mail(); form.append(email)
        tel = telefone(); form.append(tel)
        return form
    else: 
        print("\n","Já existe cliente com esse CPF".center(30))
        return -1 # Elemento para ser excluído pela função safeCheck()

# Função para criar a lista de e-mails do cliente
def mail():
    email = input("E-mail: ")
    lista = []
    lista.append(email)
    opc = 's'
    while opc == 's' or opc == 'S':
        opc = input("Deseja adicionar mais um e-mail? [s/S] ")
        if opc == 's' or opc == 'S':
            email = input("E-mail: ")
            lista.append(email)
    return lista

# Função para criar a lista de telefones do cliente
def telefone():
    tel = input("Telefone: ")
    lista = []
    lista.append(tel)
    opc = 's'
    while opc == 's' or opc == 'S':
        opc = input("Deseja adicionar mais um telefone? [s/S] ")
        if opc == 's' or opc == 'S':
            tel = input("Telefone: ")
            lista.append(tel)
    return lista

# Formulário para adicionar Produtos
def formProduto(lista):
    form = []
    cod = digitos(input("Código: "))
    if percorreLista(cod, lista) == -1:                                     # Teste para checar se o código
        form.append(cod)                                                    # já consta na lista de produtos
        descr = input("Descrição: "); form.append(descr)
        peso = input("Peso (kg): "); form.append(peso)
        preco = float(floating(input("Preço: R$ "))); form.append(preco)
        desconto = float(floating(input("Desconto: R$ "))); form.append(desconto)
        data = input("Data de Validade: "); form.append(data)
        return form
    else: 
        print("\n", "Já existe produto com esse código".center(30))
        return -1 # Elemento para ser excluído pela função safeCheck()

# Função para alterar elementos - decisão
def alterar(x, lista):
    if x == '1': alteraCliente(lista)
    elif x == '2': alteraProduto(lista)

# Função para alterar Clientes
def alteraCliente(clientes):
    cpf = digitos(input("Digite o CPF: "))
    cliente = percorreLista(cpf, clientes) 
    if cliente == -1:
        print("\n", "Não existe cliente com esse CPF\n".center(30))
        system('pause')
    else:
        while True:
            system('cls')
            print("========================================")
            listaCliente(clientes, cliente)
            print("\nO que deseja alterar:")
            print(" 1 - Nome")
            print(" 2 - Data de Nascimento")
            print(" 3 - Sexo")
            print(" 4 - Salário")
            print(" 5 - E-mails")
            print(" 6 - Telefones")
            print(" 0 - Retornar")
            print("\n(👁 ͜ʖ👁 )")
            opc = input("Escolha: ")
            if opc == '0':
                return 0
            elif opc >= '1' and opc <= '3':
                write(clientes, cliente, opc)
            elif opc == '4':
                floaters(clientes, cliente, opc)
            elif opc == '5' or opc == '6':
                editar(clientes, cliente, opc)

# Função para alterar Produtos
def alteraProduto(produtos):
    cod = digitos(input("Digite o código: "))
    produto = percorreLista(cod, produtos)
    if produto == -1:
        print("\n", "Não existe produto com esse código\n".center(30))
        system('pause')
    else:
        while True:
            system('cls')
            print("========================================")
            listaProduto(produtos, produto)
            print("\nO que deseja alterar:")
            print(" 1 - Descrição")
            print(" 2 - Peso")
            print(" 3 - Preço")
            print(" 4 - Desconto")
            print(" 5 - Data de Validade")
            print(" 0 - Retornar")
            print("\n(👁 ͜ʖ👁 )")
            opc = input("Escolha: ")
            if opc == '0':
                return 0
            elif opc == '1' or opc == '2' or opc == '5':
                write(produtos, produto, opc)
            elif opc == '3' or opc == '4':
                floaters(produtos, produto, opc)

# Função para alterar especificamente e-mails ou telefones
def editar(lista, i, x):
    j = int(x)
    print("\nQual elemento deseja alterar?\n")
    for k in range(len(lista[i][j])):
        print(k+1, "-", lista[i][j][k])
    print()
    print("[a/A] para adicionar um elemento!")
    print("[r/R] para remover   um elemento!")
    print("\n(👁 ͜ʖ👁 )")
    opc = input("Escolha: ")
    
    if opc == '0': 
        return 0
    elif opc == 'a' or opc == 'A':
        if x == '5': lista[i][j].append(input("E-mail: "))
        elif x == '6': lista[i][j].append(input("Telefone: "))
    elif opc == 'r' or opc == 'R':
        rem = int(input("Qual o índice do elemento que deseja remover? "))
        if rem <= len(lista[i][j]) and rem != 0:
            del lista[i][j][rem-1]
            print("\n", "Removido!\n".center(30)); system('pause')
        else: 
            print("\n", "O elemento não se encontra na lista\n".center(30)); system('pause')
    elif opc.isdigit():
        if int(opc) <= len(lista[i][j]):
            k = int(opc)-1
            escrever(lista, i, j, k)
        else:
            print("\n", "O elemento não se encontra na lista\n".center(30)); system('pause')
    else: 
        print("\n", "Inválido!\n".center(30)); system('pause')

# Função para sobrescrever e-mails ou telefones
def escrever(lista, i, j, k):
    novo = input("Digite o novo: ")
    lista[i][j][k] = novo

# Função para sobrescrever strings de uma lista
def write(lista, i, j):
    novo = input("Digite o novo: ")
    lista[i][int(j)] = novo

# Função para sobrescrever um float em uma lista
def floaters(lista, i, j):
    novo = float(floating(input("Digite o novo: ")))
    lista[i][int(j)] = novo

# Função para percorrer elementos em uma lista em busca de um igual
def percorreLista(val, lista):
    for i in range(len(lista)):
        if lista[i][0] == val:
            return i
    return -1

# Função para excluir um elemento de uma lista
def excluir(x, lista):
    if x == '1':
        cpf = digitos(input("Digite o CPF do cliente que deseja excluir: "))
        print()
        cliente = percorreLista(cpf, lista)
        if cliente == -1: print("Não existe cliente com esse CPF".center(30))
        else:
            print("========================================")
            listaCliente(lista, cliente)
            opc = input("\nDeseja remover este cliente do sistema da loja? [s/S] ")
            if opc == 's' or opc == 'S': 
                del lista[cliente]; print("\n", "Removido!".center(30))

    elif x == '2':
        cod = digitos(input("Digite o código do produto que deseja excluir: "))
        print()
        produto = percorreLista(cod, lista)
        if produto == -1: print("Não existe produto com esse código".center(30))
        else:
            print("========================================")
            listaProduto(lista, produto)
            opc = input("\nDeseja remover este produto do sistema da loja? [s/S] ")
            if opc == 's' or opc == 'S': 
                del lista[produto]; print("\n", "Removido!".center(30))

    print()

'''
Função destinada a corrigir um pequeno bug que ocasiona da possibilidade de o usuário digitar um cpf
ou código já existente na função "incluir". No caso o programa inevitavelmente irá gravar 'None' na 
posição do array que aquele suposto cadastro deveria estar. Só que isto gera um conflito na função 
"percorreLista", porque esta não é capaz de ler elementos nulos. Então, ao invés de permitir que 
ocorresse um elemento nulo no array, eu optei por acrescentar "-1", e o papel desta função é encontrar 
elementos com esse valor e excluí-los do array.
'''
def safeCheck(lista):
    for i in range(len(lista)): 
        if lista[i] == -1: del lista[i]

# Função para acrescentar algum conteúdo nas listas
def conteudo(clientes, produtos):
    client = ["22339988556", "Björn Hilmarsson", "28/10/1996", "masc", 9393.93, ["bjorn@gmail.com", "raposa@gmail.com"], ["(11) 9369-2378", "(16) 8678-6532"]]
    clientes.append(client)
    product = ["93", "Algo muito específico", "23.0", 69.87, 2.3, "30/02/2997"]
    produtos.append(product)

# Declaração da função main()
def main():
    clientes = []
    produtos = []
    conteudo(clientes, produtos)
    while True:
        system('cls')
        print("╔════     .     *      -   .     +    .     ════╗")
        print("║ '    `     '     ,                *         ` ║")
        print("    `    '    -         *    `    `    +   '     ")
        print(" *   +      .   ,    `     '    -   .     `   *  ")
        print("=================== ANDROMEDA ===================")
        print("Seja bem vinde ao santuário da Rainha dos Homens\n")
        print("1 - CLIENTES".center(20))
        print("2 - PRODUTOS".center(20))
        print("0 - SAIR    ".center(20))
        print("\n(👁 ͜ʖ👁 )")
        opc = input("Escolha: ")
        if opc == '0': return 0
        elif opc == '1': menu(opc, clientes)
        elif opc == '2': menu(opc, produtos)
        elif opc == 'cc': del clientes[len(clientes)-1] # Limpeza para quando um elemento "None" é adicionado na lista
        elif opc == 'cp': del produtos[len(produtos)-1] # Limpeza para quando um elemento "None" é adicionado na lista

# Chamada do Programa
main()