from pydantic import BaseModel, EmailStr
from datetime import date


class UsuarioCrear(BaseModel):
    nombre: str
    correo: EmailStr


class UsuarioRespuesta(UsuarioCrear):
    id: int


class TareaCrear(BaseModel):
    nombre: str
    descripcion: str
    estado: str
    porcentaje_avance: float
    fecha_inicio: date
    fecha_final: date
    usuario_id: int


class TareaRespuesta(TareaCrear):
    id: int


class ActividadCrear(BaseModel):
    nombre: str
    descripcion: str
    estado: str
    fecha: date
    completada: bool
    tarea_id: int


class ActividadRespuesta(ActividadCrear):
    id: int