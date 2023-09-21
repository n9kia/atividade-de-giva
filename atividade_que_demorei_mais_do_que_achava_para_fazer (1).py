import os
import time
import keyboard

contatos = []  # Lista para armazenar os contatos

def limpar_tela():
    os.system("cls")

def esperaTecla(teclasvalidas):
    while True:
        key_pressed = keyboard.read_key()
        if key_pressed in teclasvalidas:
            return key_pressed
        time.sleep(0.3)

def fechar_agenda():
    print("Deseja salvar a agenda antes de fechar? (S/N): ")
    a = esperaTecla(["s", "n", "S", "N"])
    if a.lower() == 's':
        salvar_agenda()
    contatos.clear()
    print("Agenda fechada.")

def criar_contato():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    categoria = input("Categoria (pessoal, profissional ou romantico): ").lower()
    contato = {
        'nome': nome,
        'endereco': endereco,
        'telefone': telefone,
        'categoria': categoria
    }
    contatos.append(contato)
    print(f"Contato de {nome} adicionado com sucesso.")

def remover_contato_por_nome(nome):
    global contatos
    contatos_mantidos = []
    encontrado = False
    for contato in contatos:
        if contato["nome"] != nome:
            contatos_mantidos.append(contato)
        else:
            print(f"Contato excluído: {contato}")
            time.sleep(2)
            encontrado = True
    if not encontrado:
        print("Contato não encontrado!")
    contatos = contatos_mantidos

def listar_contatos():
    limpar_tela()
    time.sleep(1)
    print("============= CONTATINHOS ===========")
    for contato in contatos:
        print(f"Nome: {contato['nome']}")
        print(f"Endereço: {contato['endereco']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Categoria: {contato['categoria']}")
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print("Clique 'esc' para continuar.")
    opcao = esperaTecla(["esc"])
    if opcao == 'esc':
        return

def editar_contato():
    listar_contatos()
    nome = input("Digite o nome do contato que deseja editar: ")
    contato_encontrado = None

    for contato in contatos:
        if contato["nome"] == nome:
            contato_encontrado = contato
            break

    if contato_encontrado:
        print(f"Editando contato: {contato_encontrado['nome']}")
        novo_nome = input(f"Novo nome ({contato_encontrado['nome']}): ")
        novo_endereco = input(f"Novo endereço ({contato_encontrado['endereco']}): ")
        novo_telefone = input(f"Novo telefone ({contato_encontrado['telefone']}): ")
        nova_categoria = input(f"Nova categoria ({contato_encontrado['categoria']}): ").lower()

        if novo_nome:
            contato_encontrado['nome'] = novo_nome
        if novo_endereco:
            contato_encontrado['endereco'] = novo_endereco
        if novo_telefone:
            contato_encontrado['telefone'] = novo_telefone
        if nova_categoria:
            contato_encontrado['categoria'] = nova_categoria

        print(f"Contato {contato_encontrado['nome']} editado com sucesso.")
    else:
        print("Contato não encontrado.")

def carregar_contatos():
    global contatos
    filename = "contatos.txt"
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            linhas = file.readlines()
            for linha in linhas:
                dados = linha.strip().split(";")
                if len(dados) == 4:
                    contato = {
                        'nome': dados[0],
                        'endereco': dados[1],
                        'telefone': dados[2],
                        'categoria': dados[3]
                    }
                    contatos.append(contato)

def salvar_agenda():
    filename = "contatos.txt"
    with open(filename, "w") as file:
        for contato in contatos:
            file.write(f"{contato['nome']};{contato['endereco']};{contato['telefone']};{contato['categoria']}\n")
    print("Agenda salva com sucesso.")

def menu():
    rodandolisinho = True
    while rodandolisinho:
        limpar_tela()
        print("abrindo agenda...")
        time.sleep(2)
        limpar_tela()
        print("\n===== Agenda de Contatinhos ===== (by César Henrique)")
        time.sleep(1)
        print("1. Listar Contatos")
        print("2. Criar Contato")
        print("3. Editar Contato")
        print("4. Excluir Contato")
        print("5. Salvar Agenda")
        print("6. Fechar Agenda")
        print("0. Sair")

        opcao = esperaTecla(["1", "2", "3", "4", "5", "6", "0"])

        if opcao == '1':
            listar_contatos()
        elif opcao == '2':
            criar_contato()
        elif opcao == '3':
            editar_contato()
        elif opcao == '4':
            nome_contato = input("Digite o nome do contato que deseja excluir: ")
            remover_contato_por_nome(nome_contato)
        elif opcao == '5':
            salvar_agenda()
        elif opcao == '6':
            fechar_agenda()
        elif opcao == '0':
            print("Deseja salvar a agenda? (S/N)")
            a= esperaTecla(["s","S","N","n"])
            if (a== "s" or a=="S"):
                salvar_agenda()
                rodandolisinho= False
print(menu())


# César