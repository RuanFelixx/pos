# pip install requests

import requests

API_URL = "http://127.0.0.1:8000/livros"

def listar_livros():
    resposta = requests.get(API_URL)
    if resposta.status_code == 200:
        livros = resposta.json()
        if livros:
            print("\n--- Lista de Livros ---")
            for livro in livros:
                print(f"Título: {livro['titulo']}, Ano: {livro['ano']}, Edição: {livro['edicao']}")
        else:
            print("Nenhum livro cadastrado.")
    else:
        print("Erro ao listar os livros.")

def pesquisar_livro():
    titulo = input("Digite o título do livro para pesquisar: ")
    resposta = requests.get(f"{API_URL}/{titulo}")
    if resposta.status_code == 200:
        livro = resposta.json()
        print(f"\nLivro encontrado:\nTítulo: {livro['titulo']}, Ano: {livro['ano']}, Edição: {livro['edicao']}")
    else:
        print("Livro não encontrado.")

def cadastrar_livro():
    titulo = input("Título do livro: ")
    ano = int(input("Ano de publicação: "))
    edicao = int(input("Edição: "))
    livro = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }
    resposta = requests.post(API_URL, json=livro)
    if resposta.status_code == 200:
        print("Livro cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar o livro.")

def deletar_livro():
    titulo = input("Digite o título do livro que deseja deletar: ")
    resposta = requests.delete(f"{API_URL}/{titulo}")
    if resposta.status_code == 200:
        print("Livro deletado com sucesso!")
    else:
        print("Livro não encontrado para exclusão.")

def menu():
    while True:
        print("\n==== MENU ====")
        print("1 - Listar todos os livros")
        print("2 - Pesquisar livro por título")
        print("3 - Cadastrar um livro")
        print("4 - Deletar um livro")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            pesquisar_livro()
        elif opcao == "3":
            cadastrar_livro()
        elif opcao == "4":
            deletar_livro()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
