import requests

API_URL = "http://127.0.0.1:8000/pedido"

def buscar_pedido_por_id():
    id_pedido = input("Digite o ID do pedido: ")

    resposta = requests.get(f"{API_URL}/{id_pedido}")

    if resposta.status_code == 200:
        pedido = resposta.json()
        print("\n--- Dados do Pedido ---")
        for chave, valor in pedido.items():
            print(f"{chave}: {valor}")
    elif resposta.status_code == 404:
        print("\n Pedido não encontrado (Erro 404).")
    else:
        print("\n Ocorreu um erro ao buscar o pedido.")

if __name__ == "__main__":
    buscar_pedido_por_id()
