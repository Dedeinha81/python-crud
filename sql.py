import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

# Criar a tabela 'usuarios' se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    idade INTEGER
)
''')
conexao.commit()

# Função para criar um novo usuário
def criar_usuario(nome, email, idade):
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, idade) VALUES (?, ?, ?)", (nome, email, idade))
        conexao.commit()
        print("Usuário adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Email já existe.")

# Função para ler todos os usuários
def ler_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

# Função para atualizar um usuário
def atualizar_usuario(id, nome, email, idade):
    cursor.execute("UPDATE usuarios SET nome = ?, email = ?, idade = ? WHERE id = ?", (nome, email, idade, id))
    conexao.commit()
    if cursor.rowcount > 0:
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

# Função para deletar um usuário
def deletar_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()
    if cursor.rowcount > 0:
        print("Usuário deletado com sucesso!")
    else:
        print("Usuário não encontrado.")

# Menu para interagir com o CRUD
def menu():
    while True:
        print("\n--- Menu CRUD ---")
        print("1. Criar usuário")
        print("2. Ler usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            idade = int(input("Idade: "))
            criar_usuario(nome, email, idade)
        elif opcao == "2":
            ler_usuarios()
        elif opcao == "3":
            id = int(input("ID do usuário a ser atualizado: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            idade = int(input("Nova idade: "))
            atualizar_usuario(id, nome, email, idade)
        elif opcao == "4":
            id = int(input("ID do usuário a ser deletado: "))
            deletar_usuario(id)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()

# Fecha a conexão com o banco de dados ao finalizar
conexao.close()
