from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import Tarefa
from typing import List
from fastapi import status

app = FastAPI()

app.mount("/css", StaticFiles(directory="css"), name="css")

templates = Jinja2Templates(directory="templates")

tarefas: List[Tarefa] = []

@app.get("/", response_class=HTMLResponse)
def exibir_formulario(request: Request):
    return templates.TemplateResponse("cadastrar_tarefa.html", {"request": request})

@app.get("/listar", response_class=HTMLResponse)
def exibir_listagem(request: Request):
    return templates.TemplateResponse("listar_tarefa.html", {"request": request})

@app.get("/tarefas/", response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.post("/tarefas/", response_model=Tarefa)
def criar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)
    return tarefa

@app.delete("/tarefas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(id: int):
    for i, tarefa in enumerate(tarefas):
        if tarefa.id == id:
            del tarefas[i]
            return
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
