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
            system('pause')
        case '5':
            system('pause')
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
    cpf = input("CPF: "); form.append(cpf)
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
    cod = input("Código: "); form.append(cod)
    descr = input("Descrição: "); form.append(descr)
    peso = input("Peso: "); form.append(peso)
    preco = input("Preço: R$"); form.append(preco)
    desconto = input("Desconto: "); form.append(desconto)
    data = input("Data de Validade: "); form.append(data)
    return form

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
        else:
            system('cls')
            menu(opc)

main()