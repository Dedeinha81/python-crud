import json
from pathlib import Path

# Caminho do arquivo JSON para armazenar a biblioteca
ARQUIVO_BIBLIOTECA = Path("biblioteca.json")

# Função para carregar dados do arquivo JSON
def carregar_biblioteca():
    if ARQUIVO_BIBLIOTECA.exists():
        with open(ARQUIVO_BIBLIOTECA, "r") as file:
            return json.load(file)
    return []

# Função para salvar dados no arquivo JSON
def salvar_biblioteca(biblioteca):
    with open(ARQUIVO_BIBLIOTECA, "w") as file:
        json.dump(biblioteca, file, indent=4)

# Função para adicionar um livro
def adicionar_livro(biblioteca):
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    ano = input("Ano de publicação: ")
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    biblioteca.append(livro)
    print(f"O livro '{titulo}' foi adicionado com sucesso!")

# Função para remover um livro pelo título
def remover_livro(biblioteca):
    titulo = input("Título do livro para remover: ")
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            biblioteca.remove(livro)
            print(f"O livro '{titulo}' foi removido com sucesso!")
            return
    print(f"Livro '{titulo}' não encontrado.")

# Função para buscar um livro pelo título
def buscar_livro(biblioteca):
    titulo = input("Título do livro para buscar: ")
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            print(f"\nLivro encontrado:\nTítulo: {livro['titulo']}\nAutor: {livro['autor']}\nAno: {livro['ano']}\n")
            return
    print(f"Livro '{titulo}' não encontrado.")

# Função para listar todos os livros
def listar_livros(biblioteca):
    if biblioteca:
        print("\nLista de livros na biblioteca:")
        for livro in biblioteca:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    else:
        print("A biblioteca está vazia.")

# Menu principal
def menu():
    biblioteca = carregar_biblioteca()

    while True:
        print("\n--- Biblioteca de Livros ---")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Buscar Livro")
        print("4. Listar Livros")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro(biblioteca)
        elif opcao == "2":
            remover_livro(biblioteca)
        elif opcao == "3":
            buscar_livro(biblioteca)
        elif opcao == "4":
            listar_livros(biblioteca)
        elif opcao == "5":
            salvar_biblioteca(biblioteca)
            print("Saindo... Dados salvos.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()
