import requests

API_URL = "http://127.0.0.1:8000/pedidos"

def main():
    try:
        id_pedido = int(input("Digite o ID do pedido: "))
        resposta = requests.get(f"{API_URL}/{id_pedido}")
        if resposta.status_code == 200:
            pedido = resposta.json()
            print("\n--- Dados do Pedido ---")
            for chave, valor in pedido.items():
                print(f"{chave}: {valor}")
        else:
            print("❌ Pedido não encontrado (Erro 404)")
    except ValueError:
        print("❌ ID inválido. Digite um número inteiro.")

if __name__ == "__main__":
    main()
