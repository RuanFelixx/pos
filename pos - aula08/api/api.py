from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()


df = pd.read_csv("20250702_Pedidos_csv_2025.csv", sep=';', encoding="utf-16", dtype=str)


df.columns = df.columns.str.strip().str.replace('\ufeff', '')


df["IdPedido"] = df["IdPedido"].astype(str)

@app.get("/pedido/{id_pedido}")
def get_pedido(id_pedido: str):
    pedido = df[df["IdPedido"] == id_pedido]
    if not pedido.empty:
        return pedido.iloc[0].to_dict()
    else:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
