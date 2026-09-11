from fastapi import APIRouter, HTTPException
from app.models.esquemas import UsuarioCrear, UsuarioRespuesta

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

usuarios = []
contador_id = 1


@router.post("/", response_model=UsuarioRespuesta, status_code=201)
def crear_usuario(usuario: UsuarioCrear):
    global contador_id

    for existente in usuarios:
        if existente["correo"] == usuario.correo:
            raise HTTPException(
                status_code=400,
                detail="El correo ya está registrado"
            )

    nuevo_usuario = {
        "id": contador_id,
        "nombre": usuario.nombre,
        "correo": usuario.correo
    }

    usuarios.append(nuevo_usuario)
    contador_id += 1

    return nuevo_usuario


@router.get("/")
def listar_usuarios():
    return usuarios


@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int):
    from app.routes.tareas import tareas

    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="El usuario no existe"
        )

    tareas_usuario = [t for t in tareas if t["usuario_id"] == usuario_id]

    return {
        "id": usuario["id"],
        "nombre": usuario["nombre"],
        "correo": usuario["correo"],
        "tareas": tareas_usuario
    }