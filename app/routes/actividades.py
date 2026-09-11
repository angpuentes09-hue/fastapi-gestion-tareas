from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models.modelos import Actividad, Tarea
from app.models.esquemas import ActividadCrear, ActividadRespuesta


router = APIRouter(
    tags=["Actividades"]
)


@router.post(
    "/tareas/{tarea_id}/actividades/",
    response_model=ActividadRespuesta,
    status_code=201
)
def crear_actividad(
    tarea_id: int,
    actividad: ActividadCrear,
    session: Session = Depends(get_session)
):
    tarea = session.get(Tarea, tarea_id)

    if not tarea:
        raise HTTPException(
            status_code=404,
            detail="La tarea no existe"
        )

    nueva_actividad = Actividad(
        nombre=actividad.nombre,
        descripcion=actividad.descripcion,
        estado=actividad.estado,
        fecha=actividad.fecha,
        completada=actividad.completada,
        tarea_id=tarea_id
    )

    session.add(nueva_actividad)
    session.commit()
    session.refresh(nueva_actividad)

    return nueva_actividad


@router.get("/actividades/", response_model=list[ActividadRespuesta])
def listar_actividades(
    session: Session = Depends(get_session)
):
    actividades = session.exec(select(Actividad)).all()
    return actividades


@router.patch("/actividades/{actividad_id}", response_model=ActividadRespuesta)
def cambiar_completada(
    actividad_id: int,
    session: Session = Depends(get_session)
):
    actividad = session.get(Actividad, actividad_id)

    if not actividad:
        raise HTTPException(
            status_code=404,
            detail="La actividad no existe"
        )

    # Invierte de True a False y de False a True
    actividad.completada = not actividad.completada

    session.add(actividad)
    session.commit()
    session.refresh(actividad)

    return actividad