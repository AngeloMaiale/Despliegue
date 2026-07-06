from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="To-Do API - Demo Despliegue")

# Base de datos temporal en memoria
db_tareas = []

# Modelo de datos para validar la entrada
class Tarea(BaseModel):
    titulo: str
    completada: bool = False

@app.get("/", tags=["Inicio"])
def raiz():
    return {"mensaje": "¡API funcionando correctamente!"}

@app.post("/tareas", tags=["Tareas"])
def crear_tarea(tarea: Tarea):
    db_tareas.append(tarea.dict())
    return {"mensaje": "Tarea guardada con éxito", "tarea": tarea}

@app.get("/tareas", response_model=List[Tarea], tags=["Tareas"])
def listar_tareas():
    return db_tareas