from fastapi import FastAPI, HTTPException
from typing import List
from models import Tarea, TareaActualizacion  # 👈 NUEVO: importamos TareaActualizacion

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

@app.put("/tareas/{tarea_id}/completar", response_model=Tarea)
def completar_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea.id == tarea_id:
            tarea.completada = True
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    global tareas
    for i, tarea in enumerate(tareas):
        if tarea.id == tarea_id:
            del tareas[i]
            return {"detail": f"Tarea {tarea_id} eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# 👇 NUEVO: Endpoint PATCH para actualización parcial
@app.patch("/tareas/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: int, cambios: TareaActualizacion):
    for tarea in tareas:
        if tarea.id == tarea_id:
            if cambios.titulo is not None:
                tarea.titulo = cambios.titulo
            if cambios.descripcion is not None:
                tarea.descripcion = cambios.descripcion
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
