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