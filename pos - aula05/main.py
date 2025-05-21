from fastapi import FastAPI, HTTPException
from models import Carro, Cliente, Reserva
from typing import List
from datetime import date

app = FastAPI()

carros: List[Carro] = []
clientes: List[Cliente] = []
reservas: List[Reserva] = []

# ----------- CARROS ------------
@app.get("/carros", response_model=List[Carro])
def listar_carros():
    return carros

@app.post("/carros", response_model=Carro)
def criar_carro(carro: Carro):
    carro.id = len(carros) + 1
    carros.append(carro)
    return carro

@app.put("/carros/{id}", response_model=Carro)
def atualizar_carro(id: int, carro: Carro):
    for i, c in enumerate(carros):
        if c.id == id:
            carro.id = id
            carros[i] = carro
            return carro
    raise HTTPException(status_code=404, detail="Carro não encontrado.")

@app.delete("/carros/{id}")
def remover_carro(id: int):
    for i, c in enumerate(carros):
        if c.id == id:
            del carros[i]
            return {"message": "Carro removido com sucesso."}
    raise HTTPException(status_code=404, detail="Carro não encontrado.")

@app.get("/carros/disponiveis", response_model=List[Carro])
def listar_carros_disponiveis():
    return [carro for carro in carros if carro.disponivel]

# ---------- CLIENTES ------------
@app.get("/clientes", response_model=List[Cliente])
def listar_clientes():
    return clientes

@app.post("/clientes", response_model=Cliente)
def criar_cliente(cliente: Cliente):
    cliente.id = len(clientes) + 1
    clientes.append(cliente)
    return cliente

@app.get("/clientes/{id}", response_model=Cliente)
def buscar_cliente(id: int):
    for cliente in clientes:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")

# ---------- RESERVAS ------------
@app.get("/reservas", response_model=List[Reserva])
def listar_reservas():
    return reservas

@app.post("/reservas", response_model=Reserva)
def criar_reserva(reserva: Reserva):
    cliente = next((c for c in clientes if c.id == reserva.cliente_id), None)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")

    carro = next((c for c in carros if c.id == reserva.carro_id), None)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado.")

    if not carro.disponivel:
        raise HTTPException(status_code=400, detail="Carro indisponível.")

    if reserva.data_fim < reserva.data_inicio:
        raise HTTPException(status_code=400, detail="Data de fim anterior à data de início.")

    reserva.id = len(reservas) + 1
    reservas.append(reserva)
    carro.disponivel = False
    return reserva

@app.delete("/reservas/{id}")
def cancelar_reserva(id: int):
    for i, reserva in enumerate(reservas):
        if reserva.id == id:
            carro = next((c for c in carros if c.id == reserva.carro_id), None)
            if carro:
                carro.disponivel = True
            del reservas[i]
            return {"message": "Reserva cancelada com sucesso."}
    raise HTTPException(status_code=404, detail="Reserva não encontrada.")
