from api import (
    consulta_bolsa_familia_cpf_nis,
    consulta_bolsa_familia_municipio,
    consulta_garantia_safra,
    consulta_seguro_defeso,
    consulta_servidor_publico,
)

def mostrar_resultado(resultado):
    if not resultado:
        print("Nenhum resultado encontrado.")
        return
    for item in resultado:
        print("-" * 40)
        for chave, valor in item.items():
            print(f"{chave}: {valor}")
        print("-" * 40)

def menu():
    while True:
        print("\n==== Consulta Portal da Transparência ====")
        print("1. Bolsa Família por CPF/NIS e Período")
        print("2. Bolsa Família por Município")
        print("3. Garantia-Safra por CPF/NIS e Período")
        print("4. Seguro Defeso por CPF/NIS e Período")
        print("5. Servidor Público Federal por CPF")
        print("0. Sair")
        opcao = input("Escolha a opção: ")

        if opcao == "1":
            codigo = input("CPF ou NIS: ")
            mes_ano = input("Mês/Ano (ex: 012024): ")
            resultado = consulta_bolsa_familia_cpf_nis(codigo, mes_ano)
            mostrar_resultado(resultado)
        elif opcao == "2":
            ibge = input("Código IBGE do município: ")
            mes_ano = input("Mês/Ano (ex: 012024): ")
            resultado = consulta_bolsa_familia_municipio(ibge, mes_ano)
            mostrar_resultado(resultado)
        elif opcao == "3":
            codigo = input("CPF ou NIS: ")
            mes_ano = input("Mês/Ano (ex: 012024): ")
            resultado = consulta_garantia_safra(codigo, mes_ano)
            mostrar_resultado(resultado)
        elif opcao == "4":
            codigo = input("CPF ou NIS: ")
            mes_ano = input("Mês/Ano (ex: 012024): ")
            resultado = consulta_seguro_defeso(codigo, mes_ano)
            mostrar_resultado(resultado)
        elif opcao == "5":
            cpf = input("Digite o CPF: ")
            resultado = consulta_servidor_publico(cpf)
            mostrar_resultado(resultado)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
