from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class Tarea(BaseModel):
    id: int
    titulo: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=500)
    responsable: Optional[str] = Field(None, max_length=100)
    completada: bool = False
    creada_en: datetime = Field(default_factory=datetime.now)

    @validator('responsable', always=True)
    def validar_responsable_si_completada(cls, v, values):
        if values.get('completada') and not v:
            raise ValueError('Debe asignarse un responsable para tareas completadas.')
        return v

class TareaActualizacion(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=500)
    responsable: Optional[str] = Field(None, max_length=100)
