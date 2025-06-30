from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    responsable: str  # 👈 NUEVO: responsable es obligatorio
    completada: bool = False
    creada_en: datetime = datetime.now()

class TareaActualizacion(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    responsable: Optional[str] = None  # 👈 NUEVO: se puede actualizar
