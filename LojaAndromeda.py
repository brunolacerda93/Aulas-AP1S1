# Projeto avaliativo - Algorítmos e Programação - ADS IFSP - 05/2022
# @author: Bruno Capelari de Lacerda SC3029492
# Tema 8: Controle de compras e vendas

# Bibliotecas
from os import system

# Submenu genérico
def menu(x, lista):
    while True:
        safeCheck(lista)
        system('cls')
        print("=================== ANDROMEDA ===================")
        print("Seja bem vinde ao santuário da Rainha dos Homens\n")
        if x == '1': print("CLIENTES")
        elif x == '2': print("PRODUTOS")
        print()
        print(" 1 - Listar Todos")
        print(" 2 - Listar Um")
        print(" 3 - Incluir")
        print(" 4 - Alterar")
        print(" 5 - Excluir")
        print(" 0 - Retornar")
        opc = input("\nEscolha: ")
        if opc == '0':
            return 0
        elif opc >= '1' and opc <= '5':
            subMenu(opc, x, lista)

# Opções do submenu
def subMenu(opc, x, lista):
    match opc:
        case '1':
            listaTodos(x, lista); system('pause')
        case '2':
            listaUm(x, lista); system('pause')
        case '3':
            incluir(x, lista); system('pause')
        case '4':
            alterar(x, lista); system('pause')
        case '5':
            excluir(x, lista); system('pause')
        case _:
            return 0

# Função para leitura completa das listas
def listaTodos(x, lista):
    if x == '1':
        for i in range(len(lista)):
            listaCliente(lista, i)

    elif x == '2':
        for i in range(len(lista)):
            listaProduto(lista, i)

# Função para ler um elemento da lista de clientes
def listaCliente(lista, i):
    print()
    print("CPF                :", lista[i][0])
    print("Nome               :", lista[i][1])
    print("Data de Nascimento :", lista[i][2])
    print("Sexo               :", lista[i][3])
    print("Salário            :", lista[i][4])
    print("E-mail             :", lista[i][5])
    print("Telefones          :", lista[i][6])

# Função para ler um elemento da lista de produtos
def listaProduto(lista, i):
    print()
    print("Código           :", lista[i][0])
    print("Descrição        :", lista[i][1])
    print("Peso             :", lista[i][2])
    print("Preço           R$", lista[i][3])
    print("Desconto         :", lista[i][4])
    print("Data de Validade :", lista[i][5])

# Função para leitura de elemento individual
def listaUm(x, lista):
    i = int(input("Digite o elemento: "))
    if i <= len(lista) and i > 0:
        if x == '1': listaCliente(lista, i-1)
        elif x == '2': listaProduto(lista, i-1)
    else: print("Não há elemento neste índice!")

# Função para incluir elementos
def incluir(x, lista):
    if x == '1': lista.append(formCliente(lista))
    elif x == '2': lista.append(formProduto(lista))

# Formulário para adicionar Clientes
def formCliente(lista):
    form = []
    cpf = input("CPF: "); 
    if percorreLista(cpf, lista) == -1:                             # Teste para checar se o cpf já
        form.append(cpf)                                            # consta na lista de clientes
        nome = input("Nome: "); form.append(nome)
        data = input("Data de Nascimento: "); form.append(data)
        sexo = input("Sexo: "); form.append(sexo)
        salario = input("Salário: "); form.append(salario)
        email = input("E-mail: "); form.append(email)
        tel = input("Telefone: "); form.append(tel)
        return form
    else: 
        print("Já existe cliente com esse CPF")
        return -1

# Formulário para adicionar Produtos
def formProduto(lista):
    form = []
    cod = input("Código: "); 
    if percorreLista(cod, lista) == -1:                             # Teste para checar se o código
        form.append(cod)                                            # já consta na lista de produtos
        descr = input("Descrição: "); form.append(descr)
        peso = input("Peso: "); form.append(peso)
        preco = input("Preço: R$"); form.append(preco)
        desconto = input("Desconto: "); form.append(desconto)
        data = input("Data de Validade: "); form.append(data)
        return form
    else: 
        print("Já existe produto com esse código")
        return -1

# Função para alterar elementos
def alterar(x, lista):
    if x == '1':
        cpf = input("Digite o CPF: ")
        cliente = percorreLista(cpf, lista) 
        if cliente == -1:
            print("Não existe cliente com esse CPF")
        else:
            while True:
                system('cls')
                listaCliente(lista, cliente)
                print("\nO que deseja alterar:")
                print(" 1 - Nome")
                print(" 2 - Data de Nascimento")
                print(" 3 - Sexo")
                print(" 4 - Salário")
                print(" 5 - E-mail")
                print(" 6 - Telefones")
                print(" 0 - Retornar")
                opc = input("Escolha: ")
                if opc == '0':
                    return 0
                elif opc >= '1' and opc <= '6':
                    write(lista, cliente, opc)

    elif x == '2':
        cod = input("Digite o código: ")
        produto = percorreLista(cod, lista)
        if produto == -1:
            print("Não existe produto com esse código")
        else:
            while True:
                system('cls')
                listaProduto(lista, produto)
                print("\nO que deseja alterar:")
                print(" 1 - Descrição")
                print(" 2 - Peso")
                print(" 3 - Preço")
                print(" 4 - Desconto")
                print(" 5 - Data de Validade")
                print(" 0 - Retornar")
                opc = input("Escolha: ")
                if opc == '0':
                    return 0
                elif opc >= '1' and opc <= '5':
                    write(lista, produto, opc)

# Função para sobrescrever elementos de uma lista global
def write(lista, i, j):
    novo = input("Digite o novo: ")
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
        cpf = input("Digite o CPF do cliente que deseja excluir: ")
        cliente = percorreLista(cpf, lista)
        if cliente == -1: print("Não existe cliente com esse CPF")
        else:
            listaCliente(lista, cliente)
            opc = input("Deseja remover este cliente do sistema da loja? [s/S] ")
            if opc == 's' or opc == 'S': del lista[cliente]; print("Removido!")

    elif x == '2':
        cod = input("Digite o código do produto que deseja excluir: ")
        produto = percorreLista(cod, lista)
        if produto == -1: print("Não existe produto com esse código")
        else:
            listaProduto(lista, produto)
            opc = input("Deseja remover este produto do sistema da loja? [s/S] ")
            if opc == 's' or opc == 'S': del lista[produto]; print("Removido!")

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

# Declaração da função main()
def main():
    clientes = []
    produtos = []
    while True:
        system('cls')
        print("=================== ANDROMEDA ===================")
        print("Seja bem vinde ao santuário da Rainha dos Homens\n")
        print(" 1 - CLIENTES")
        print(" 2 - PRODUTOS")
        print(" 0 - SAIR")
        opc = input("\nEscolha: ")
        if opc == '0':
            break
        elif opc == '1': menu(opc, clientes)
        elif opc == '2': menu(opc, produtos)
        elif opc == 'cc': del clientes[len(clientes)-1] # Limpeza para quando um elemento "None" é adicionado na lista
        elif opc == 'cp': del produtos[len(produtos)-1] # Limpeza para quando um elemento "None" é adicionado na lista

# Chamada do Programa
main()