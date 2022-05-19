# Projeto avaliativo - Algorítmos e Programação - ADS IFSP - 05/2022
# @author: Bruno Capelari de Lacerda SC3029492
# Tema 8: Controle de compras e vendas

# Bibliotecas
from os import system

# Variáveis Globais
clientes = []
produtos = []

# Submenu genérico
def menu(x):
    while True:
        system('cls')
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
            subMenu(opc, x)
        elif opc == 'cc': del clientes[len(clientes)-1] # Limpeza para quando um elemento "None" é adicionado na lista
        elif opc == 'cp': del produtos[len(produtos)-1] # Limpeza para quando um elemento "None" é adicionado na lista

# Opções do submenu
def subMenu(opc, x):
    match opc:
        case '1':
            listarTodos(x); system('pause')
        case '2':
            listarUm(x); system('pause')
        case '3':
            incluir(x); system('pause')
        case '4':
            alterar(x); system('pause')
        case '5':
            excluir(x); system('pause')
        case _:
            return 0

# Função para leitura das listas
def listarTodos(x):
    if x == '1': print(clientes)
    elif x == '2': print(produtos)

# Função para leitura de elemento individual
def listarUm(x):
    i = int(input("Digite o elemento: "))
    if x == '1': print(clientes[i-1])
    elif x == '2': print(produtos[i-1])

# Função para incluir elementos
def incluir(x):
    if x == '1': clientes.append(formCliente())
    elif x == '2': produtos.append(formProduto())

# Formulário para adicionar Clientes
def formCliente():
    form = []
    cpf = input("CPF: "); 
    if percorreCliente(cpf) == -1: form.append(cpf)                         # Teste para checar se o cpf já
    else: print("Já existe cliente com esse CPF"); return form.clear()      # consta na lista de clientes
    nome = input("Nome: "); form.append(nome)
    data = input("Data de Nascimento: "); form.append(data)
    sexo = input("Sexo: "); form.append(sexo)
    salario = input("Salário: "); form.append(salario)
    email = input("E-mail: "); form.append(email)
    tel = input("Telefone: "); form.append(tel)
    return form

#Formulário para adicionar Produtos
def formProduto():
    form = []
    cod = input("Código: "); 
    if percorreProduto(cod) == -1: form.append(cod)                         # Teste para checar se o código
    else: print("Já existe produto com esse código"); return form.clear()   # já consta na lista de produtos
    descr = input("Descrição: "); form.append(descr)
    peso = input("Peso: "); form.append(peso)
    preco = input("Preço: R$"); form.append(preco)
    desconto = input("Desconto: "); form.append(desconto)
    data = input("Data de Validade: "); form.append(data)
    return form

#Função para alterar elementos
def alterar(x):
    if x == '1':
        cpf = input("Digite o CPF: ")
        cliente = percorreCliente(cpf) 
        if cliente == -1:
            print("Não existe cliente com esse CPF")
        else:
            mostraCliente(cliente)
            while True:
                system('cls')
                print(clientes[cliente])
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
                    write(clientes, cliente, opc)

    elif x == '2':
        cod = input("Digite o código: ")
        produto = percorreProduto(cod)
        if produto == -1:
            print("Não existe produto com esse código")
        else:
            mostraProduto(produto)
            while True:
                system('cls')
                print(produtos[produto])
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
                    write(produtos, produto, opc)

#Função para sobrescrever elementos de uma lista global
def write(lista, i, j):
    novo = input("Digite o novo: ")
    lista[i][int(j)] = novo

# Função para percorrer clientes em busca de um CPF igual
def percorreCliente(cpf):
    for i in range(len(clientes)):
        if clientes[i][0] == cpf:
            return i
    return -1

# Função para exibir o conteúdo da lista de Clientes
def mostraCliente(cliente):
    print(clientes[cliente])

# Função para percorrer produtos em busca de um código igual
def percorreProduto(cod):
    for i in range(len(produtos)):
        if produtos[i][0] == cod:
            return i
    return -1

# Função para exibir o conteúdo da lista de Produtos
def mostraProduto(produto):
    print(produtos[produto])

# Função para excluir um elemento de uma lista
def excluir(x):
    if x == '1':
        cpf = input("Digite o CPF do cliente que deseja excluir: ")
        cliente = percorreCliente(cpf)
        if cliente == -1: print("Não existe cliente com esse CPF")
        else:
            mostraCliente(cliente)
            opc = input("Deseja remover este cliente do sistema da loja? [s/S]")
            if opc == 's' or opc == 'S': del clientes[cliente]; print("Removido!")

    elif x == '2':
        cod = input("Digite o código do produto que deseja excluir: ")
        produto = percorreProduto(cod)
        if produto == -1: print("Não existe produto com esse código")
        else:
            mostraProduto(produto)
            opc = input("Deseja remover este produto do sistema da loja? [s/S]")
            if opc == 's' or opc == 'S': del produtos[produto]; print("Removido!")

# Declaração da função main()
def main():
    while True:
        system('cls')
        print("=================== ANDROMEDA ===================")
        print("Seja bem vinde ao santuário da Rainha dos Homens")
        print(" 1 - CLIENTES")
        print(" 2 - PRODUTOS")
        print(" 0 - SAIR")
        opc = input("Escolha: ")
        if opc == '0':
            break
        elif opc == '1' or opc == '2':
            system('cls')
            menu(opc)

main()