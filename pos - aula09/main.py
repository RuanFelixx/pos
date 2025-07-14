from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from models import Pedido
from sqlmodel import select, Session, create_engine, SQLModel
from typing import Annotated
import pandas as pd

# Ler CSV
df = pd.read_csv("20250702_Pedidos_csv_2025.csv", sep=';', encoding="utf-16", dtype=str)
df.columns = df.columns.str.strip().str.replace('\ufeff', '')

# Conexão SQLite
sqlite_url = "sqlite:///banco.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    with Session(engine) as session:
        existe = session.exec(select(Pedido)).first()
        if not existe:
            for _, row in df.iterrows():
                # Corrige datas
                for campo in ["DataRegistro", "PrazoAtendimento", "DataResposta"]:
                    try:
                        row[campo] = pd.to_datetime(row[campo], format="%d/%m/%Y", errors='coerce').date()
                    except:
                        row[campo] = None

                # Corrige inteiros
                for campo in ["IdPedido", "IdSolicitante"]:
                    valor = row[campo]
                    if pd.notna(valor) and str(valor).strip().isdigit():
                        row[campo] = int(str(valor).strip())
                    else:
                        row[campo] = None

                # Substitui quaisquer NaN restantes por None para evitar erros no SQLAlchemy
                dados = {k: (None if pd.isna(v) else v) for k, v in row.items()}

                pedido = Pedido(**dados)
                session.add(pedido)
            session.commit()

    yield

app = FastAPI(lifespan=lifespan)

@app.get("/pedidos/{id}")
def get_pedido(id: int, session: SessionDep):
    pedido = session.exec(select(Pedido).where(Pedido.IdPedido == id)).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido
