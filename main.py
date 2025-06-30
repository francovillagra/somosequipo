from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request
from fastapi import status

from fastapi import FastAPI, HTTPException
from typing import List, Optional
from models import Tarea, TareaActualizacion  # 👈 NUEVO: importamos TareaActualizacion
from storage import guardar_tareas_en_archivo, cargar_tareas_desde_archivo


app = FastAPI(title="SomosEquipo API")

tareas: List[Tarea] = cargar_tareas_desde_archivo()


# 👇 MODIFICADO: ahora acepta query param "completadas"
@app.get("/tareas", response_model=List[Tarea])
def listar_tareas(completadas: Optional[bool] = None):
    """
    Lista todas las tareas o filtra por estado de completadas.
    - Sin parámetros: devuelve todas.
    - completadas=true: solo completadas.
    - completadas=false: solo pendientes.
    """
    if completadas is None:
        return tareas
    return [t for t in tareas if t.completada == completadas]

@app.post("/tareas", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    if any(t.id == tarea.id for t in tareas):
        raise HTTPException(status_code=400, detail="ID ya existe")
    tareas.append(tarea)
    guardar_tareas_en_archivo(tareas)  # 👈 NUEVO
    return tarea


@app.put("/tareas/{tarea_id}/completar", response_model=Tarea)
def completar_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea.id == tarea_id:
            tarea.completada = True
            guardar_tareas_en_archivo(tareas)  # 👈 NUEVO
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    global tareas
    for i, tarea in enumerate(tareas):
        if tarea.id == tarea_id:
            del tareas[i]
            guardar_tareas_en_archivo(tareas)  # 👈 NUEVO
            return {"detail": f"Tarea {tarea_id} eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


@app.patch("/tareas/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: int, cambios: TareaActualizacion):
    for tarea in tareas:
        if tarea.id == tarea_id:
            if cambios.titulo is not None:
                tarea.titulo = cambios.titulo
            if cambios.descripcion is not None:
                tarea.descripcion = cambios.descripcion
            if cambios.responsable is not None:
                tarea.responsable = cambios.responsable
            guardar_tareas_en_archivo(tareas)  # 👈 NUEVO
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


@app.get("/tareas/{tarea_id}", response_model=Tarea)
def obtener_tarea(tarea_id: int):
    """
    Devuelve la tarea con el ID especificado.
    """
    for tarea in tareas:
        if tarea.id == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


# 👇 NUEVO: capturar y traducir errores de validación
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores_traducidos = []
    for error in exc.errors():
        campo = " ➜ ".join(str(loc) for loc in error["loc"])
        mensaje = error["msg"]
        # Traducción básica
        if "value is not a valid integer" in mensaje.lower():
            mensaje = "El valor debe ser un número entero."
        elif "field required" in mensaje.lower():
            mensaje = "Este campo es obligatorio."
        elif "none is not an allowed value" in mensaje.lower():
            mensaje = "No se permite un valor nulo."
        errores_traducidos.append({"campo": campo, "mensaje": mensaje})

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detalle": errores_traducidos},
    )