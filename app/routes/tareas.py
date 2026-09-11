from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models.modelos import Tarea, Usuario
# 👇 IMPORTANTE: Importamos TareaConUsuarioRespuesta
from app.models.esquemas import TareaCrear, TareaRespuesta, TareaConUsuarioRespuesta


router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)


@router.post("/", response_model=TareaRespuesta, status_code=201)
def crear_tarea(
    tarea: TareaCrear,
    session: Session = Depends(get_session)
):
    usuario = session.get(Usuario, tarea.usuario_id)

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="El usuario no existe"
        )

    nueva_tarea = Tarea(
        nombre=tarea.nombre,
        descripcion=tarea.descripcion,
        estado=tarea.estado,
        porcentaje_avance=tarea.porcentaje_avance,
        fecha_inicio=tarea.fecha_inicio,
        fecha_final=tarea.fecha_final,
        usuario_id=tarea.usuario_id
    )

    session.add(nueva_tarea)
    session.commit()
    session.refresh(nueva_tarea)

    return nueva_tarea


# 👇 CAMBIO AQUÍ: Cambiamos TareaRespuesta por TareaConUsuarioRespuesta
@router.get("/", response_model=list[TareaConUsuarioRespuesta])
def listar_tareas(
    session: Session = Depends(get_session)
):
    tareas = session.exec(select(Tarea)).all()
    return tareas