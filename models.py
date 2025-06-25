from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False
    creada_en: datetime = datetime.now()

class TareaActualizacion(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
