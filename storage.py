import json
from models import Tarea
from typing import List

ARCHIVO_TAREAS = "tareas.json"

def guardar_tareas_en_archivo(tareas: List[Tarea]):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump(
            [json.loads(tarea.model_dump_json()) for tarea in tareas],
            f,
            ensure_ascii=False,
            indent=4
        )

def cargar_tareas_desde_archivo() -> List[Tarea]:
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Tarea(**item) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
