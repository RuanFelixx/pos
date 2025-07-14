import requests

BASE_URL = "https://portaldatransparencia.gov.br/api-de-dados"
HEADERS = {"Accept": "application/json"}

def consulta_bolsa_familia_cpf_nis(cpf_ou_nis, mes_ano):
    url = f"{BASE_URL}/bolsa-familia-por-cpf-ou-nis"
    params = {"codigoBeneficiario": cpf_ou_nis, "mesAno": mes_ano, "pagina": 1}
    return requests.get(url, headers=HEADERS, params=params).json()

def consulta_bolsa_familia_municipio(codigo_ibge, mes_ano):
    url = f"{BASE_URL}/bolsa-familia-por-municipio"
    params = {"codigoIbge": codigo_ibge, "mesAno": mes_ano, "pagina": 1}
    return requests.get(url, headers=HEADERS, params=params).json()

def consulta_garantia_safra(cpf_ou_nis, mes_ano):
    url = f"{BASE_URL}/garantia-safra-por-cpf-ou-nis"
    params = {"codigoBeneficiario": cpf_ou_nis, "mesAno": mes_ano, "pagina": 1}
    return requests.get(url, headers=HEADERS, params=params).json()

def consulta_seguro_defeso(cpf_ou_nis, mes_ano):
    url = f"{BASE_URL}/seguro-defeso-por-cpf-ou-nis"
    params = {"codigoBeneficiario": cpf_ou_nis, "mesAno": mes_ano, "pagina": 1}
    return requests.get(url, headers=HEADERS, params=params).json()

def consulta_servidor_publico(cpf):
    url = f"{BASE_URL}/servidores"
    params = {"cpf": cpf, "pagina": 1}
    return requests.get(url, headers=HEADERS, params=params).json()
