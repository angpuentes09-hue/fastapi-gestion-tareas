from fastapi import APIRouter, HTTPException, status
from app.models.schemas import TareaCreate, TareaResponse
from app.routes.usuarios import usuarios_db
from typing import List

router = APIRouter(prefix="/tareas", tags=["Tareas"])

# Base de datos en memoria
tareas_db = []
tarea_id_counter = 1

@router.post("/", response_model=TareaResponse, status_code=status.HTTP_201_CREATED)
def crear_tarea(tarea: TareaCreate):
    # Validar que el usuario existe
    usuario_existe = any(u["id"] == tarea.usuario_id for u in usuarios_db)
    if not usuario_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    
    nueva_tarea = tarea.model_dump()
    nueva_tarea["id"] = tarea_id_counter
    tareas_db.append(nueva_tarea)
    tarea_id_counter += 1
    return nueva_tarea

@router.get("/", response_model=List[TareaResponse])
def listar_tareas():
    return tareas_db
