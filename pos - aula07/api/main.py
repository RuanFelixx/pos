from fastapi import FastAPI,HTTPException
from models import Veiculo
from typing import List

app = FastAPI()

veiculos: List[Veiculo] = []

@app.get("/veiculos")
def listar_veiculos():
    return veiculos

@app.post("/veiculos")
def cadastrar_veiculo(veiculo: Veiculo):
    for v in veiculos:
        if v.placa == veiculo.placa:
            raise HTTPException(status_code=400, detail="Placa já cadastrada.")
    veiculos.append(veiculo)
    return {"mensagem": "Veículo cadastrado com sucesso."}

@app.put("/veiculos/{placa}")
def atualizar_veiculo(placa: str, veiculo: Veiculo):
    for i, v in enumerate(veiculos):
        if v.placa == placa:
            veiculos[i] = veiculo
            return {"mensagem": "Veículo atualizado com sucesso."}
    raise HTTPException(status_code=404, detail="Veículo não encontrado.")

@app.delete("/veiculos/{placa}")
def deletar_veiculo(placa: str):
    for i, v in enumerate(veiculos):
        if v.placa == placa:
            del veiculos[i]
            return {"mensagem": "Veículo deletado com sucesso."}
    raise HTTPException(status_code=404, detail="Veículo não encontrado.")