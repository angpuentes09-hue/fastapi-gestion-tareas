from pydantic import BaseModel, EmailStr
from datetime import date


# -------------------------
# USUARIO
# -------------------------

class UsuarioCreate(BaseModel):
    nombre: str
    correo: EmailStr


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: EmailStr


# -------------------------
# TAREA
# -------------------------

class TareaCreate(BaseModel):
    nombre: str
    descripcion: str
    estado: str
    avance: float
    fecha_inicio: date
    fecha_final: date
    usuario_id: int


class TareaResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    estado: str
    avance: float
    fecha_inicio: date
    fecha_final: date
    usuario_id: int


# -------------------------
# ACTIVIDAD
# -------------------------

class ActividadCreate(BaseModel):
    nombre: str
    descripcion: str
    estado: str
    fecha: date
    completada: bool


class ActividadResponse(BaseModel):
    id: int
    nombre: str
    descripcion: str
    estado: str
    fecha: date
    completada: bool
    tarea_id: int