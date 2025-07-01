from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional

from routers.dependencies import verificar_credenciales
from models import Tarea, TareaActualizacion
from storage import guardar_tareas_en_archivo, cargar_tareas_desde_archivo

# 📌 Router para todas las operaciones de tareas
router = APIRouter(
    prefix="/tareas",
    tags=["tareas"],
    dependencies=[Depends(verificar_credenciales)]
)

# 📦 Cargar las tareas almacenadas al arrancar
tareas: List[Tarea] = cargar_tareas_desde_archivo()


# --------------------------------
# 📌 Endpoints
# --------------------------------

@router.get("", response_model=List[Tarea])
def listar_tareas(completadas: Optional[bool] = None):
    """
    Lista todas las tareas o filtra por su estado de completadas.
    """
    if completadas is None:
        return tareas
    return [t for t in tareas if t.completada == completadas]


@router.post("", response_model=Tarea)
def crear_tarea(tarea: Tarea):
    """
    Crea una nueva tarea. Valida ID único.
    """
    if any(t.id == tarea.id for t in tareas):
        raise HTTPException(status_code=400, detail="ID ya existe")
    tareas.append(tarea)
    guardar_tareas_en_archivo(tareas)
    return tarea


@router.put("/{tarea_id}/completar", response_model=Tarea)
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


@router.delete("/{tarea_id}")
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


@router.patch("/{tarea_id}", response_model=Tarea)
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


@router.get("/{tarea_id}", response_model=Tarea)
def obtener_tarea(tarea_id: int):
    """
    Devuelve la tarea con el ID especificado.
    """
    for tarea in tareas:
        if tarea.id == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
