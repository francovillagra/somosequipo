from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from typing import List, Optional

from models import Tarea, TareaActualizacion
from storage import guardar_tareas_en_archivo, cargar_tareas_desde_archivo

# 📌 Router para todas las operaciones de tareas
router = APIRouter(
    prefix="/tareas",
    tags=["tareas"]
)

# 📦 Cargar las tareas almacenadas al arrancar
tareas: List[Tarea] = cargar_tareas_desde_archivo()


# --------------------------------
# 📌 Endpoints
# --------------------------------

@router.get("/tareas", response_model=List[Tarea])
def listar_tareas(completadas: Optional[bool] = None):
    """
    Lista todas las tareas o filtra por su estado de completadas.
    - Sin parámetros: devuelve todas.
    - completadas=true: solo completadas.
    - completadas=false: solo pendientes.
    """
    if completadas is None:
        return tareas
    return [t for t in tareas if t.completada == completadas]


@router.post("/tareas", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    """
    Crea una nueva tarea. Valida ID único.
    """
    if any(t.id == tarea.id for t in tareas):
        raise HTTPException(status_code=400, detail="ID ya existe")
    tareas.append(tarea)
    guardar_tareas_en_archivo(tareas)
    return tarea


@router.put("/tareas/{tarea_id}/completar", response_model=Tarea)
def completar_tarea(tarea_id: int):
    """
    Marca la tarea como completada.
    """
    for tarea in tareas:
        if tarea.id == tarea_id:
            tarea.completada = True
            guardar_tareas_en_archivo(tareas)
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


@router.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int):
    """
    Elimina la tarea por ID.
    """
    global tareas
    for i, tarea in enumerate(tareas):
        if tarea.id == tarea_id:
            del tareas[i]
            guardar_tareas_en_archivo(tareas)
            return {"detail": f"Tarea {tarea_id} eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


@router.patch("/tareas/{tarea_id}", response_model=Tarea)
def actualizar_tarea(tarea_id: int, cambios: TareaActualizacion):
    """
    Permite actualizaciones parciales en título, descripción o responsable.
    """
    for tarea in tareas:
        if tarea.id == tarea_id:
            if cambios.titulo is not None:
                tarea.titulo = cambios.titulo
            if cambios.descripcion is not None:
                tarea.descripcion = cambios.descripcion
            if cambios.responsable is not None:
                tarea.responsable = cambios.responsable
            guardar_tareas_en_archivo(tareas)
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


@router.get("/tareas/{tarea_id}", response_model=Tarea)
def obtener_tarea(tarea_id: int):
    """
    Devuelve la tarea con el ID especificado.
    """
    for tarea in tareas:
        if tarea.id == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


# --------------------------------
# 📌 Manejo de errores de validación
# --------------------------------

@router.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Traduce errores de validación al español.
    """
    errores_traducidos = []
    for error in exc.errors():
        campo = " ➜ ".join(str(loc) for loc in error["loc"])
        mensaje = error["msg"]
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
