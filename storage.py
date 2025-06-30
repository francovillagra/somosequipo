import json
from models import Tarea
from typing import List

ARCHIVO_TAREAS = "tareas.json"

def guardar_tareas_en_archivo(tareas: List[Tarea]):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump([tarea.dict() for tarea in tareas], f, ensure_ascii=False, indent=4)

def cargar_tareas_desde_archivo() -> List[Tarea]:
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return [Tarea(**item) for item in datos]
    except (FileNotFoundError, json.JSONDecodeError):
        print("[⚠️ AVISO] El archivo tareas.json estaba vacío, no existía o estaba corrupto. Reiniciando como lista vacía.")
        # Reescribimos el archivo vacío
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []
