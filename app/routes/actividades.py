from fastapi import APIRouter, HTTPException
from app.models.esquemas import ActividadCrear, ActividadRespuesta
from app.routes.tareas import tareas

router = APIRouter(
    tags=["Actividades"]
)

actividades = []
contador_id = 1


@router.post(
    "/tareas/{tarea_id}/actividades/",
    response_model=ActividadRespuesta,
    status_code=201
)
def crear_actividad(tarea_id: int, actividad: ActividadCrear):
    global contador_id

    tarea_existe = any(
        tarea["id"] == tarea_id
        for tarea in tareas
    )

    if not tarea_existe:
        raise HTTPException(
            status_code=404,
            detail="La tarea no existe"
        )

    nueva_actividad = {
        "id": contador_id,
        "nombre": actividad.nombre,
        "descripcion": actividad.descripcion,
        "estado": actividad.estado,
        "fecha": actividad.fecha,
        "completada": actividad.completada,
        "tarea_id": tarea_id
    }

    actividades.append(nueva_actividad)
    contador_id += 1

    return nueva_actividad


@router.get("/actividades/")
def listar_actividades():
    return actividades


@router.patch("/actividades/{actividad_id}")
def cambiar_completada(actividad_id: int):
    for actividad in actividades:
        if actividad["id"] == actividad_id:
            actividad["completada"] = not actividad["completada"]
            return actividad

    raise HTTPException(
        status_code=404,
        detail="La actividad no existe"
    )