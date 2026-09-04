from fastapi import APIRouter, HTTPException
from app.models.esquemas import TareaCrear, TareaRespuesta
from app.routes.usuarios import usuarios

router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)

tareas = []
contador_id = 1


@router.post("/", response_model=TareaRespuesta, status_code=201)
def crear_tarea(tarea: TareaCrear):
    global contador_id

    usuario_existe = any(
        usuario["id"] == tarea.usuario_id
        for usuario in usuarios
    )

    if not usuario_existe:
        raise HTTPException(
            status_code=404,
            detail="El usuario no existe"
        )

    nueva_tarea = {
        "id": contador_id,
        "nombre": tarea.nombre,
        "descripcion": tarea.descripcion,
        "estado": tarea.estado,
        "porcentaje_avance": tarea.porcentaje_avance,
        "fecha_inicio": tarea.fecha_inicio,
        "fecha_final": tarea.fecha_final,
        "usuario_id": tarea.usuario_id
    }

    tareas.append(nueva_tarea)
    contador_id += 1

    return nueva_tarea


@router.get("/")
def listar_tareas():
    return tareas