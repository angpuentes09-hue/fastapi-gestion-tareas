from fastapi import APIRouter, HTTPException, status
from app.models.schemas import ActividadCreate, ActividadResponse
from app.routes.tareas import tareas_db
from typing import List

router = APIRouter(prefix="/tareas", tags=["Actividades"])

# Base de datos en memoria
actividades_db = []
actividad_id_counter = 1

@router.post("/{tarea_id}/actividades/", response_model=ActividadResponse, status_code=status.HTTP_201_CREATED)
def crear_actividad(tarea_id: int, actividad: ActividadCreate):
    # Validar que la tarea existe
    tarea_existe = any(t["id"] == tarea_id for t in tareas_db)
    if not tarea_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarea no encontrada"
        )
    
    nueva_actividad = actividad.model_dump()
    nueva_actividad["id"] = actividad_id_counter
    actividades_db.append(nueva_actividad)
    actividad_id_counter += 1
    return nueva_actividad

@router.put("/actividades/{actividad_id}", response_model=ActividadResponse)
def actualizar_estado_actividad(actividad_id: int):
    # Buscar la actividad
    for actividad in actividades_db:
        if actividad["id"] == actividad_id:
            # Cambiar estado completada
            actividad["completada"] = not actividad["completada"]
            return actividad
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Actividad no encontrada"
    )
