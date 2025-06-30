import json
from typing import List
from models import Tarea

ARCHIVO_TAREAS = "tareas.json"

def guardar_tareas_en_archivo(tareas: List[Tarea]):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        datos = [tarea.dict() for tarea in tareas]
        json.dump(datos, f, ensure_ascii=False, indent=4)

def cargar_tareas_desde_archivo() -> List[Tarea]:
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return [Tarea(**item) for item in datos]
    except FileNotFoundError:
        return []
