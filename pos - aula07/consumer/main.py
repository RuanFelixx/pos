# app_terminal.py
import requests

URL = "http://127.0.0.1:8000/veiculos"

def menu():
    while True:
        print("\n1. Cadastrar veículo")
        print("2. Listar veículos")
        print("3. Atualizar veículo")
        print("4. Deletar veículo")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            deletar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def cadastrar():
    nome = input("Nome: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    placa = input("Placa: ")
    dados = {"nome": nome, "marca": marca, "modelo": modelo, "placa": placa}
    r = requests.post(URL, json=dados)
    print(r.json())

def listar():
    r = requests.get(URL)
    for v in r.json():
        print(f"{v['nome']} | {v['marca']} | {v['modelo']} | {v['placa']}")

def atualizar():
    placa = input("Placa do veículo a atualizar: ")
    nome = input("Novo nome: ")
    marca = input("Nova marca: ")
    modelo = input("Novo modelo: ")
    nova_placa = input("Nova placa: ")
    dados = {"nome": nome, "marca": marca, "modelo": modelo, "placa": nova_placa}
    r = requests.put(f"{URL}/{placa}", json=dados)
    print(r.json())

def deletar():
    placa = input("Placa do veículo a deletar: ")
    r = requests.delete(f"{URL}/{placa}")
    print(r.json())

menu()
