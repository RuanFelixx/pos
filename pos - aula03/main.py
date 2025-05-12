#pip install fastapi uvicorn
# python -m venv .virtual
#.\.virtual\Scripts\activate
#uvicorn main:app
#url/docs
from fastapi import FastAPI, HTTPException
from models import Usuario, Livro, Biblioteca, Emprestimo
from typing import List

app = FastAPI()

usuarios: List[Usuario] = []
livros: List[Livro] = []
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []

#Teste de usuarios
@app.get("/usuarios/",response_model=List[Usuario])
def listar_usuarios():
    return usuarios

@app.post("/usuarios/",response_model=Usuario)
def criar_usuario(usuario:Usuario):
    usuario.id = len(usuarios)+1
    usuarios.append(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}", response_model=Usuario)
def excluir_usuario(usuario_id: int):
    for index, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuario_excluido = usuarios.pop(index) #ocorreu um erro no del, ai troquei para pop
            return usuario_excluido
    raise HTTPException(status_code=404, detail="Usuário não localizado")

#teste para livros 
@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros

@app.post("/livros/", response_model=Livro)
def criar_livro(livro: Livro):
    livro.id = len(livros) + 1
    livros.append(livro)
    return livro

@app.delete("/livros/{livro_id}", response_model=Livro)
def excluir_livro(livro_id: int):
    for index, livro in enumerate(livros):
        if livro.id == livro_id:
            return livros.pop(index)
    raise HTTPException(status_code=404, detail="Livro não localizado")

#teste para biblioteca
@app.get("/bibliotecas/", response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas

@app.post("/bibliotecas/", response_model=Biblioteca)
def criar_biblioteca(biblioteca: Biblioteca):                         
    biblioteca.id = len(bibliotecas) + 1
    bibliotecas.append(biblioteca)
    return biblioteca

@app.delete("/bibliotecas/{biblioteca_id}", response_model=Biblioteca)
def excluir_biblioteca(biblioteca_id: int):
    for index, biblioteca in enumerate(bibliotecas):
        if biblioteca.id == biblioteca_id:
            return bibliotecas.pop(index)
    raise HTTPException(status_code=404, detail="Biblioteca não localizada")


#teste para emprestimos
@app.get("/emprestimos/", response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos

@app.post("/emprestimos/", response_model=Emprestimo)
def criar_emprestimo(emprestimo: Emprestimo):
    emprestimo.id = len(emprestimos) + 1
    emprestimos.append(emprestimo)
    return emprestimo

@app.delete("/emprestimos/{emprestimo_id}", response_model=Emprestimo)
def excluir_emprestimo(emprestimo_id: int):
    for index, emprestimo in enumerate(emprestimos):
        if emprestimo.id == emprestimo_id:
            return emprestimos.pop(index)
    raise HTTPException(status_code=404, detail="Empréstimo não localizado")

