from fastapi import FastAPI, HTTPException
from typing import List
from models import Tarea

app = FastAPI(title="SomosEquipo API")

tareas: List[Tarea] = []

@app.get("/tareas", response_model=List[Tarea])
def listar_tareas():
    return tareas

@app.post("/tareas", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    if any(t.id == tarea.id for t in tareas):
        raise HTTPException(status_code=400, detail="ID ya existe")
    tareas.append(tarea)
    return tarea

# NUEVO endpoint para marcar tarea como completada
@app.put("/tareas/{tarea_id}/completar", response_model=Tarea)
def completar_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea.id == tarea_id:
            tarea.completada = True
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
