from fastapi import FastAPI, HTTPException
from typing import List
from models import Tarea

app = FastAPI(title="SomosEquipo API")

# Base temporal en memoria
tareas: List[Tarea] = []

# Endpoint para listar todas las tareas
@app.get("/tareas", response_model=List[Tarea])
def listar_tareas():
    return tareas

# Endpoint para crear una tarea
@app.post("/tareas", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    # Valida que el id sea único
    if any(t.id == tarea.id for t in tareas):
        raise HTTPException(status_code=400, detail="ID ya existe")
    tareas.append(tarea)
    return tarea
