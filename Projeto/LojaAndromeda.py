# Projeto avaliativo - Algorítmos e Programação - ADS IFSP - 05/2022
# @author: Bruno Capelari de Lacerda SC3029492
# Tema 8: Controle de compras e vendas

# Bibliotecas
from os import system
import string
import datetime as dt

# Submenu genérico
def menu(x, clientes, produtos, movimentos):
    # Opções do submenu para clientes/produtos - decisão
    def subMenu_01(opc, x, lista):
        match opc:
            case '1':
                listaTodos(x, lista);   system('pause')
            case '2':
                listaUm(x, lista);      system('pause')
            case '3':
                incluir(x, lista);      system('pause')
            case '4':
                alterar(x, lista)
            case '5':
                excluir(x, lista);      system('pause')
            case _:
                return 0

    # Opções do submenu para compra/venda - decisão
    def subMenu_02(opc, x, clientes, produtos, movimentos):
        match opc:
            case '1':
                listaTodos(x, movimentos);                          system('pause')
            case '2':
                listaUm(x, movimentos);                             system('pause')
            case '3':
                cadastraMovimento(clientes, produtos, movimentos);  system('pause')
            case '4':
                alteraMovimento(clientes, produtos, movimentos);    arquivaMovimento(movimentos)
            case '5':
                excluirMovimento(clientes, movimentos);             system('pause')
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
        elif x == '3':
            for i in lista:
                listaMovimento(lista, i)
        print()
    
    # Função para leitura de elemento individual
    def listaUm(x, lista):
        i = int(input("Digite o elemento: "))
        print("\n========================================")
        if i <= len(lista) and i > 0:
            if   x == '1': listaCliente(lista, i-1)
            elif x == '2': listaProduto(lista, i-1)
            elif x == '3': listaMovimento(lista, list(lista.keys())[i-1])
        else: print("\n", "Não há elemento neste índice!".center(36))
        print()
    
    # Função para incluir elementos - decisão
    def incluir(x, lista):
        if   x == '1': cadastraCliente(lista); arquivaCliente(lista)
        elif x == '2': cadastraProduto(lista); arquivaProduto(lista)
        print()
    
    # Função para alterar elementos - decisão
    def alterar(x, lista):
        if   x == '1': alteraCliente(lista); arquivaCliente(lista)
        elif x == '2': alteraProduto(lista); arquivaProduto(lista)
    
    # Função para excluir elementos - decisão
    def excluir(x, lista):
        if   x == '1': excluirCliente(lista); arquivaCliente(lista)
        elif x == '2': excluirProduto(lista); arquivaProduto(lista)
        print()
    
    while True:
        system('cls')
        print("=================== ANDROMEDA ===================")
        print("Seja bem vinde ao santuário da Rainha dos Homens\n")
        if   x == '1': print("CLIENTES".center(48))
        elif x == '2': print("PRODUTOS".center(48))
        elif x == '3': print("COMPRA/VENDA".center(48))
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
            if x == '1':
                subMenu_01(opc, x, clientes)
            elif x == '2':
                subMenu_01(opc, x, produtos)
            elif x == '3':
                subMenu_02(opc, x, clientes, produtos, movimentos)

# Submenu de relatórios
def menuRelatorios(clientes, produtos, movimentos):
    while True:
        system('cls')
        print("=================== ANDROMEDA ===================")
        print("Seja bem vinde ao santuário da Rainha dos Homens\n")
        print("RELATÓRIOS".center(48))
        print()
        print("    1 - Clientes por Telefones")
        print("    2 - Produtos Vencidos     ")
        print("    3 - Vendas por Data       ")
        print("    0 - Retornar              ")
        print("\n(👁 ͜ʖ👁 )")
        opc = input("Escolha: ")
        if opc == '0':
            return 0
        if opc == '1':
            relatorioTelefones(clientes)
            system('pause')
        if opc == '2':
            relatorioValidade(produtos)
            system('pause')
        if opc == '3':
            relatorioMovimentos(clientes, produtos, movimentos)
            system('pause')

# Função para ler um elemento da lista de clientes
def listaCliente(clientes, i):
    print("CLIENTE {n:02n}".format(n = i+1).center(40))
    print("CPF                :", end=" ")
    for j in range(0, len(clientes[i][0])):
        print(clientes[i][0][j], end="")
        if   j == 2: print(".", end="")
        elif j == 5: print(".", end="")
        elif j == 8: print("/", end="")
    print()
    print("Nome               :", clientes[i][1].replace("_", " "))
    print("Data de Nascimento :", end=" ")
    for j in range(3):
        print(f"{clientes[i][2][j]:02n}", end="")
        if j == 2: print()
        else: print("/", end="")
    print("Sexo               :", clientes[i][3].replace("_", " "))
    print("Salário           R$ {val:.2f}".format(val = clientes[i][4]))
    print("E-mails            :", end=" ") 
    for j in range(0, len(clientes[i][5])):
        if j == len(clientes[i][5])-1:
            print(clientes[i][5][j])
        else:
            print(clientes[i][5][j], "\n\t\t   :", end=" ")
    print("Telefones          :", end=" ")
    for j in range(0, len(clientes[i][6])):
        if j == len(clientes[i][6])-1:
            print(clientes[i][6][j].replace("_", " "))
        else:
            print(clientes[i][6][j].replace("_", " "), "\n\t\t   :", end=" ")
    print("========================================")

# Função para ler um elemento da lista de produtos
def listaProduto(produtos, i):
    print("PRODUTO {n:02n}".format(n = i+1).center(40))
    print("Código           :", produtos[i][0])
    print("Descrição        :", produtos[i][1].replace("_", " "))
    print("Peso (kg)        :", produtos[i][2])
    print("Preço           R$ {val:.2f}".format(val = produtos[i][3]))
    print("Desconto        R$ {val:.2f}".format(val = produtos[i][4]))
    print("Data de Validade :", end=" ")
    for j in range(3):
        print(f"{produtos[i][5][j]:02n}", end="")
        if j == 2: print()
        else: print("/", end="")
    print("========================================")

# Função para ler um elemento da lista de compra/venda
def listaMovimento(movimentos, cpf):
    #print(cpf, ":", movimentos[cpf])
    print("CPF :", end=" ")
    for j in range(len(cpf)):
        print(cpf[j], end="")
        if   j == 2: print(".", end="")
        elif j == 5: print(".", end="")
        elif j == 8: print("/", end="")
    print()
    for j in range(len(movimentos[cpf])):
        print("\n", "PRODUTO {n:02n}".format(n = movimentos[cpf][j][0]+1).center(36))
        print("Data da Compra     :", end=" ")
        for k in range(3):
            print(f"{movimentos[cpf][j][1][k]:02n}", end="")
            if k == 2: print()
            else: print("/", end="")
        print("Hora               :", movimentos[cpf][j][2])
        print(f"Valor             R$ {movimentos[cpf][j][3]:.2f}")
    print("========================================")

# Função para filtrar uma string para int
def digitos(array):
    novoArray = ""
    if not array.isdigit():
        for i in array:
            if i in string.digits:
                novoArray += i
        return novoArray
    else:
        return array

# Função para filtrar uma string para int com negativo
def digito(array):
    novoArray = ""
    if not array.isdigit():
        for i in array:
            if i in string.digits or i == '-':
                novoArray += i
        return novoArray
    else:
        return array

# Função para filtrar uma string para float
def floating(array):
    novoArray = ""
    if not array.isdigit():
        for i in array:
            if i in string.digits or i in string.punctuation:
                novoArray += i
        return novoArray.replace(",", ".")
    else:
        return array

# Função para criar a lista de elementos de Datas
def data():
    # Função para verificar se o dia é válido
    def confirmaDia(dia):
        if dia.isdigit():
            d = int(dia)
            if d in range(1, 32):
                return int(dia)
            else: return 0
        elif dia == "": return 15
        else: return 0

    # Função para verificar se o dia e o mês são válidos
    def confirmaMes(dia, mes):
        MESES = {"janeiro": 1, "fevereiro": 2, "março": 3, "marco": 3, "abril": 4, "maio": 5, "junho": 6, "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12}
        if mes.isdigit():
            m = int(mes)
            if m in range(1, 13) and checkMes(dia, m):
                return int(mes)
            else:
                return 0

        elif mes.lower() in MESES:
            m = mes.lower()
            if checkMes(dia, MESES[m]):
                return MESES[m]
            else: return 0

        elif mes == "": return 4
        else: return 0

    # FunÇão para verificar se o ano é válido
    def confirmaAno(dia, mes, ano):
        if len(ano) == 4 and ano.isdigit():
            a = int(ano)
            if bissexto(dia, mes, a):
                return a
            else: return 0
        elif ano == "": return 1452
        else: return 0
            
    # Função para confirmar se o dia e o mês são válidos
    def checkMes(dia, mes):
        MESES_UM   = [1, 3, 5, 7, 8, 10, 12]
        MESES_ZERO = [4, 6, 9, 11]
        if mes in MESES_UM:
            if dia <= 31:   return True
            else:           return False

        elif mes in MESES_ZERO:
            if dia <= 30:   return True
            else:           return False

        elif mes == 2:
            if dia <= 29:   return True
            else:           return False
        
        else: return False

    # Função para verificar se o ano é bissexto
    def bissexto(dia, mes, ano):
        if mes == 2 and dia == 29:
            if ano%400 == 0 and ano%100 == 0:
                return True
            elif ano%4 == 0 and ano%100 != 0:
                return True
            else: 
                return False
        else:
            return True
    
    lista = []
    flag = False
    while not flag:
        dia = confirmaDia(input("Dia: "))
        if dia != 0:
            mes = confirmaMes(dia, input("Mês: "))
            if mes != 0:
                ano = confirmaAno(dia, mes, input("Ano: "))
                if ano != 0:
                    lista.append(dia)
                    lista.append(mes)
                    lista.append(ano)
                    flag = True
        if not flag:
            print("Digite uma data válida!\n")
    return lista

# Formulário para adicionar Clientes
def cadastraCliente(clientes):
    # Função para criar a lista de e-mails do cliente
    def email():
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
    
    form = []
    cpf = digitos(input("CPF: "))
    if percorreLista(cpf, clientes) == -1:                                             # Teste para checar se o cpf já
        form.append(cpf)                                                               # consta na lista de clientes
        nome    = input("Nome: ");                          form.append(nome)
        print("Data de Nascimento:")
        date    = data();                                   form.append(date)
        sexo    = input("Sexo: ");                          form.append(sexo)
        salario = float(floating(input("Salário: R$ ")));   form.append(salario)
        mail    = email();                                  form.append(mail)
        tel     = telefone();                               form.append(tel)
        clientes.append(form)
    else: 
        print("\n","Já existe cliente com esse CPF".center(30))

# Formulário para adicionar Produtos
def cadastraProduto(produtos):
    form = []
    cod = digitos(input("Código: "))
    if percorreLista(cod, produtos) == -1:                                             # Teste para checar se o código
        form.append(cod)                                                               # já consta na lista de produtos
        descr    = input("Descrição: ");                        form.append(descr)
        peso     = input("Peso (kg): ");                        form.append(peso)
        preco    = float(floating(input("Preço: R$ ")));        form.append(preco)
        desconto = float(floating(input("Desconto: R$ ")));     form.append(desconto)
        print("Data de Validade:"); date = data()
        form.append(date)
        produtos.append(form)
    else:
        print("\n", "Já existe produto com esse código".center(30))

# Formulário para adicionar compra/venda
def cadastraMovimento(clientes, produtos, movimentos):
    cpf = digitos(input("CPF: "))
    if percorreLista(cpf, clientes) == -1:
        print("\n", "Não existe cliente com esse CPF\n".center(30))
    else:
        movimentos[cpf] = []
        opc = 's'
        while opc == 's' or opc == 'S':
            cod = digitos(input("\nCódigo: "))
            produto = percorreLista(cod, produtos)
            if produto == -1:
                print("\n", "Não existe produto com esse código\n".center(30))
            else:
                form  = []
                prod  = produto;                                                form.append(prod)        
                print("Data da Compra:")
                date  = data();                                                 form.append(date)
                hora  = input("Hora: ");                                        form.append(hora)
                qtd   = float(input("Quantidade: "))
                valor = qtd*(produtos[produto][3] - produtos[produto][4]);      form.append(valor)
                movimentos[cpf].append(form)

            opc = input("Deseja adicionar outro produto? [s/S] ")
            if opc != 's' and opc != 'S':
                # Atualiza o arquivo MOVIMENTOS.txt
                arquivaMovimento(movimentos)
    print()

# Função para alterar Clientes
def alteraCliente(clientes):
    # Função para alterar especificamente e-mails ou telefones
    def editar(lista, i, x):
        # Função para sobrescrever e-mails ou telefones
        def escrever(lista, i, j, k):
            novo = input("Digite o novo: ")
            lista[i][j][k] = novo

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
            if   x == '5': lista[i][j].append(input("E-mail: "))
            elif x == '6': lista[i][j].append(input("Telefone: "))
        
        elif opc == 'r' or opc == 'R':
            rem = int(input("Qual o índice do elemento que deseja remover? "))
            if rem <= len(lista[i][j]) and rem != 0:
                del lista[i][j][rem-1]
                print("\n", "Removido!\n".center(30));                                      system('pause')
            else: 
                print("\n", "O elemento não se encontra na lista\n".center(30));            system('pause')
        
        elif opc.isdigit():
            if int(opc) <= len(lista[i][j]):
                k = int(opc)-1
                escrever(lista, i, j, k)
            else:
                print("\n", "O elemento não se encontra na lista\n".center(30));            system('pause')
        
        else: 
            print("\n", "Inválido!\n".center(30));                                          system('pause')
    
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
            elif opc == '1' or opc == '3':
                write(clientes, cliente, opc)
            elif opc == '2':
                print("Nova Data:")
                clientes[cliente][2] = data()
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
            elif opc == '1' or opc == '2':
                write(produtos, produto, opc)
            elif opc == '3' or opc == '4':
                floaters(produtos, produto, opc)
            elif opc == '5':
                print("Nova Data:")
                produtos[produto][5] = data()

# Função para alterar compra/venda
def alteraMovimento(clientes, produtos, movimentos):
    cpf = digitos(input("Digite o CPF: "))
    cliente = percorreLista(cpf, clientes)
    if cliente == -1:
        print("\n", "Não existe cliente com esse CPF\n".center(30))
        system('pause')
    else:
        if cpf in movimentos.keys():
            while True:
                system('cls')
                print("========================================")
                listaMovimento(movimentos, cpf)
                print("\nO que deseja alterar:")
                print(" 1 - Valor")
                print(" 0 - Retornar")
                print("\n(👁 ͜ʖ👁 )")
                opc = input("Escolha: ")
                
                if   opc == '0': return 0
                elif opc == '1':
                    print("\nQual valor deseja alterar?\n")
                    for i in range(len(movimentos[cpf])):
                        print(i+1, "-", movimentos[cpf][i][3])
                    print("\n(👁 ͜ʖ👁 )")
                    opc = input("Escolha: ")
                    if opc.isdigit() and opc != '0':
                        k = int(opc)-1
                        if k < len(movimentos[cpf]):
                            qtd = int(input("Digite a nova quantidade: "))
                            produto = movimentos[cpf][k][0]
                            movimentos[cpf][k][3] = qtd*(produtos[produto][3] - produtos[produto][4])
                        else:
                            print("\n", "O elemento não se encontra na lista\n".center(30))
                            system('pause')
                    else:
                        print("\n", "Inválido!\n".center(30))
                        system('pause')
        else:
            print("\n","Este cliente não possui movimentações na loja!\n".center(30))
            system('pause')

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

# Função para excluir Clientes
def excluirCliente(clientes):
    cpf = digitos(input("Digite o CPF do cliente que deseja excluir: "))
    print()
    cliente = percorreLista(cpf, clientes)
    if cliente == -1: print("Não existe cliente com esse CPF".center(30))
    else:
        print("========================================")
        listaCliente(clientes, cliente)
        opc = input("\nDeseja remover este cliente do sistema da loja? [s/S] ")
        if opc == 's' or opc == 'S': 
            del clientes[cliente]; print("\n", "Removido!".center(30))

# Função para excluir Produtos
def excluirProduto(produtos):
    cod = digitos(input("Digite o código do produto que deseja excluir: "))
    print()
    produto = percorreLista(cod, produtos)
    if produto == -1: print("Não existe produto com esse código".center(30))
    else:
        print("========================================")
        listaProduto(produtos, produto)
        opc = input("\nDeseja remover este produto do sistema da loja? [s/S] ")
        if opc == 's' or opc == 'S': 
            del produtos[produto]; print("\n", "Removido!".center(30))

# Função para excluir compra/venda
def excluirMovimento(clientes, movimentos):
    cpf = digitos(input("Digite o CPF do cliente cuja venda deseja excluir: "))
    print()
    cliente = percorreLista(cpf, clientes)
    if cliente == -1:
        print("Não existe cliente com esse CPF".center(30))
        print()
    else:
        if cpf in movimentos.keys():
            listaMovimento(movimentos, cpf)
            opc = input("\nDeseja remover esta movimentação do sistema da loja? [s/S] ")
            if opc == 's' or opc == 'S':
                del movimentos[cpf]
                arquivaMovimento(movimentos)
                print("\n", "Removido!".center(30))
                print()
                return 0
        else:
            print("\n","Este cliente não possui movimentações na loja!\n".center(30))
            system('pause')

# Função para ler o arquivo clientes
def lerClientes():
    LISTA = [0, 1, 3]; clientes = []; cliente = []; data = []; emails = []; telefones = []

    #arq = open("CLIENTES.txt", "r")
    arq = open("TESTE.txt", "r")
    linha = arq.readline()
    while linha:
        dados = linha.split()
        key = int(dados[0])
        if   key in LISTA:    cliente.insert(key,           str(dados[1]))
        elif key == 2:           data.insert(int(dados[1]), int(dados[2]))
        elif key == 4:        cliente.insert(key,           float(dados[1]))
        elif key == 5:         emails.insert(int(dados[1]), str(dados[2]))
        elif key == 6:      telefones.insert(int(dados[1]), str(dados[2]))
        elif key == -1:
            cliente.insert(2,      data[:]);      data.clear()
            cliente.insert(5,    emails[:]);    emails.clear()
            cliente.insert(6, telefones[:]); telefones.clear()
            clientes.append(    cliente[:]);   cliente.clear()
        linha = arq.readline()
    arq.close()

    return clientes

# Função para ler o arquivo produtos
def lerProdutos():
    LISTA = [0, 1, 2]; LISTAF = [3, 4]; produtos = []; produto = []; data = []

    #arq = open("PRODUTOS.txt", "r")
    arq = open("TESTE_P.txt", "r")
    linha = arq.readline()
    while linha:
        dados = linha.split()
        key = int(dados[0])
        if   key in LISTA:    produto.insert(key,           str(dados[1]))
        elif key in LISTAF:   produto.insert(key,           float(dados[1]))
        elif key == 5:           data.insert(int(dados[1]), int(dados[2]))
        elif key == -1:
            produto.insert (5,     data[:]);      data.clear()
            produtos.append(    produto[:]);   produto.clear()
        linha = arq.readline()
    arq.close()

    return produtos

# Função para ler o arquivo movimentos
def lerMovimentos():
    movimentos = {}; movimento = []; data = []; mov = []

    #arq = open("MOVIMENTOS.txt", "r")
    arq = open("TESTE_M.txt", "r")
    linha = arq.readline()
    while linha:
        dados = linha.split()
        key = int(dados[0])

        if key == 0:
            cpf = str(dados[1])
            movimentos[cpf] = []

        elif key == 1:  mov.insert(key-1,          int(dados[1]))
        elif key == 2: data.insert(int(dados[1]),  int(dados[2]))
        elif key == 3:  mov.insert(key-1,          str(dados[1]))
        elif key == 4:  mov.insert(key-1,          float(dados[1]))

        elif key == -1:
            mov.insert(1,   data[:]); data.clear()
            movimento.append(mov[:]);  mov.clear()
        elif key == -2:
            movimentos[cpf] = movimento[:]; movimento.clear()

        linha = arq.readline()
    arq.close()

    return movimentos

# Função para arquivar o conteúdo de clientes
def arquivaCliente(clientes):
    arq = open("TESTE.txt", "w")
    for cliente in clientes:
        arq.write("0 "   +     cliente[0]                   + "\n")
        arq.write("1 "   +     cliente[1].replace(" ", "_") + "\n")
        arq.write("2 0 " + str(cliente[2][0])               + "\n")
        arq.write("2 1 " + str(cliente[2][1])               + "\n")
        arq.write("2 2 " + str(cliente[2][2])               + "\n")
        arq.write("3 "   +     cliente[3]                   + "\n")
        arq.write("4 "   + str(cliente[4])                  + "\n")
        for i in range(len(cliente[5])):
            arq.write("5 " + str(i) + " " + str(cliente[5][i]) + "\n")
        for i in range(len(cliente[6])):
            arq.write("6 " + str(i) + " " + str(cliente[6][i]).replace(" ", "_") + "\n")
        arq.write("-1\n")
    arq.close()

# Função para arquivar o conteúdo de produtos
def arquivaProduto(produtos):
    arq = open("TESTE_P.txt", "w")
    for produto in produtos:
        arq.write("0 "   +     produto[0]                   + "\n")
        arq.write("1 "   +     produto[1].replace(" ", "_") + "\n")
        arq.write("2 "   +     produto[2]                   + "\n")
        arq.write("3 "   + str(produto[3])                  + "\n")
        arq.write("4 "   + str(produto[4])                  + "\n")
        arq.write("5 0 " + str(produto[5][0])               + "\n")
        arq.write("5 1 " + str(produto[5][1])               + "\n")
        arq.write("5 2 " + str(produto[5][2])               + "\n")
        arq.write("-1\n")
    arq.close()

# Função para arquivar o conteúdo de movimentos
def arquivaMovimento(movimentos):
    arq = open("TESTE_M.txt", "w")
    for cpf in movimentos.keys():
        for i in range(len(movimentos[cpf])):
            if i == 0: arq.write("0 "  +      cpf             + "\n")
            arq.write("1 "   + str(movimentos[cpf][i][0])     + "\n")
            arq.write("2 0 " + str(movimentos[cpf][i][1][0])  + "\n")
            arq.write("2 1 " + str(movimentos[cpf][i][1][1])  + "\n")
            arq.write("2 2 " + str(movimentos[cpf][i][1][2])  + "\n")
            arq.write("3 "   +     movimentos[cpf][i][2]      + "\n")
            arq.write("4 "   + str(movimentos[cpf][i][3])     + "\n")
            arq.write("-1\n")
        arq.write("-2\n")
    arq.close()

# Função para gerar o relatório de clientes por telefones
def relatorioTelefones(clientes):
    n = 'a'
    while not n.isdigit():
        system('cls')
        print("Este relatório mostra os clientes que possuem N ou mais telefones")
        n = digitos(input("Digite N: "))
        print("\n========================================")
        if n == "":
            print("\n", "Inválido!".center(30))
        else:
            reg = True
            for cliente in clientes:
                if len(cliente[6]) >= int(n):
                    listaCliente(clientes, clientes.index(cliente))
                    reg = False
            if reg:
                print("Não há nenhum cliente com", n, "telefones")
    print()

# Função para gerar o relatório de validade
def relatorioValidade(produtos):
    system('cls')
    Hoje = dt.datetime.now()
    print("Hoje:", Hoje.strftime("%A, %d %B %Y"))
    print("\nPRODUTOS VENCIDOS")

    # Solução um pouco menos elegante, porém "sem" orientação a objetos
    #
    # Este primeiro bloco recebe a data do sistema
    # dia = str(Hoje).split()[0].split("-")[2]
    # mes = str(Hoje).split()[0].split("-")[1]
    # ano = str(Hoje).split()[0].split("-")[0]
    #
    # flag = True
    # for produto in produtos:
    #    reg = True
    #    difAno = int(ano) - produto[5][2]
    #    difMes = int(mes) - produto[5][1]
    #    difDia = int(dia) - produto[5][0]
    #    if difAno == 0:
    #        if difMes == 0:
    #            if difDia > 0:
    #                reg = False
    #        elif difMes > 0:
    #            reg = False
    #    elif difAno > 0:
    #        reg = False
    #    if not reg:
    #        print()
    #        listaProduto(produtos, produtos.index(produto))
    #        flag = False
    # if flag:
    #    print("\nNão há produtos vencidos!")

    reg = True
    for produto in produtos:
        DataValidade = dt.datetime(day = produto[5][0], month = produto[5][1], year = produto[5][2])
        dif = str(Hoje - DataValidade).split()
        if int(digito(dif[0])) > 0:
            print("\nVenceu há:", dif[0], "dias\n")
            listaProduto(produtos, produtos.index(produto))
            reg = False
    if reg:
        print("\nNão há produtos vencidos!")
    
    print()

# Função para gerar o relatório de vendas por data
def relatorioMovimentos(clientes, produtos, movimentos):
    system('cls')
    Hoje = dt.datetime.now()
    print("Hoje:", Hoje.strftime("%A, %d %B %Y"))
    print("\nEste relatório mostra as vendas realizadas dentro de um certo período")
    print("\nData inicial")
    data1 = data()
    DataInicial = dt.datetime(day = data1[0], month = data1[1], year = data1[2])
    opc = input("\nData final [pressione 0 para inserir a data de Hoje, ou Enter para continuar] ")
    if opc == '0':
        #DataFinal = dt.datetime(year=int(str(Hoje.year)), month=int(str(Hoje.month)), day=int(str(Hoje.day)), hour=0, minute=0, second=0, microsecond=0)
        DataFinal = Hoje
        dif = str(DataFinal - DataInicial).split()
    else:
        data2 = data()
        DataFinal = dt.datetime(day = data2[0], month = data2[1], year = data2[2])
        dif = str(DataFinal - DataInicial).split()
    
    if int(digito(dif[0])) < 0:
        print("\n", "Datas digitadas são inválidas!".center(30))
    else:
        system('cls')
        print("Data inicial :", DataInicial.strftime("%A %d %B %Y"))
        print("Data final   :",   DataFinal.strftime("%A %d %B %Y"))
        print("\n==============================================")
        for cpf in movimentos.keys():
            flag = True
            for movimento in movimentos[cpf]:
                DataMovimento = dt.datetime(day = movimento[1][0], month = movimento[1][1], year = movimento[1][2])
                difInicial = int(digito(str(DataInicial - DataMovimento).split()[0]))
                difFinal   = int(digito(str(DataFinal   - DataMovimento).split()[0]))
                if difInicial <= 0 and difFinal >= 0:
                    if flag:
                        i = percorreLista(cpf, clientes)
                        print(f"CLIENTE {i+1:02n}".center(40))
                        print()
                        print("Nome:", clientes[i][1].replace("_", " "))
                        print("CPF :", end=" ")
                        for j in range(len(cpf)):
                            print(cpf[j], end="")
                            if   j == 2: print(".", end="")
                            elif j == 5: print(".", end="")
                            elif j == 8: print("/", end="")
                        print()
                        flag = False
                    print()
                    print("PRODUTO {n:02n}".format(n = movimento[0]+1).center(40))
                    print("Código             :", produtos[movimento[0]][0])
                    print("Descrição          :", produtos[movimento[0]][1].replace("_", " "))
                    print("Data da Compra     :", end=" ")
                    for k in range(3):
                        print(f"{movimento[1][k]:02n}", end="")
                        if k == 2: print()
                        else: print("/", end="")
                    print("Hora               :", movimento[2])
                    print(f"Valor             R$ {movimento[3]:.2f}")
            if not flag:
                print("==============================================")
    print()

# Declaração da função main()
def main():
    # Função para acrescentar algum conteúdo nas listas
    def conteudo(clientes, produtos, movimentos):
        client = ["22339988556", "Björn_Hilmarsson", [23, 5, 1996], "masc", 9393.93, ["bjorn@gmail.com", "raposa@gmail.com"], ["(11)_9369-2378", "(16)_8678-6532"]]
        clientes.append(client)
        client = ["93939393936", "Björn_Hilmarsson", [7, 10, 1993], "masc", 9393.93, ["bjorn@gmail.com", "raposa@gmail.com"], ["(11)_9369-2378", "(16)_8678-6532"]]
        clientes.append(client)
        product = ["93", "Algo_muito_específico", "23.0", 69.87, 2.3, [23, 7, 1993]]
        produtos.append(product)
        product = ["23", "Algo_muito_específico", "23.0", 69.87, 2.3, [9, 11, 2023]]
        produtos.append(product)
        movimentos['93939393936'] = [[1, [5, 6, 2022], '17:23', 6284.0], [0, [5, 6, 2022], '17:23', 4662.33]]
    
    #conteudo(clientes, produtos, movimentos)
    #clientes = []
    #produtos = []
    #movimentos = {}
    clientes = lerClientes()
    produtos = lerProdutos()
    movimentos = lerMovimentos()
    relatorios = []
    while True:
        system('cls')
        print("╔════     .     *      -   .     +    .     ════╗")
        print("║ '    `     '     ,                *         ` ║")
        print("    `    '    -         *    `    `    +   '     ")
        print(" *   +      .   ,    `     '    -   .     `   *  ")
        print("=================== ANDROMEDA ===================")
        print("Seja bem vinde ao santuário da Rainha dos Homens\n")
        print("    1 - CLIENTES")
        print("    2 - PRODUTOS")
        print("    3 - COMPRA/VENDA")
        print("    4 - RELATÓRIOS")
        print("    0 - SAIR    ")
        print("\n(👁 ͜ʖ👁 )")
        opc = input("Escolha: ")
        if   opc == '0': return 0
        elif opc >= '1' and opc <= '3': menu(opc, clientes, produtos, movimentos)
        elif opc == '4': menuRelatorios(clientes, produtos, movimentos)

# Chamada do Programa
main()