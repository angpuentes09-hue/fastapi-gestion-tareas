from datetime import date
from sqlmodel import Field, Relationship, SQLModel


class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    correo: str = Field(unique=True, index=True)

    tareas: list["Tarea"] = Relationship(back_populates="usuario")


class Tarea(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    estado: str
    porcentaje_avance: float
    fecha_inicio: date
    fecha_final: date

    usuario_id: int = Field(foreign_key="usuario.id")

    usuario: Usuario | None = Relationship(back_populates="tareas")
    actividades: list["Actividad"] = Relationship(back_populates="tarea")


class Actividad(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    estado: str
    fecha: date
    completada: bool = False

    tarea_id: int = Field(foreign_key="tarea.id")

    tarea: Tarea | None = Relationship(back_populates="actividades")
