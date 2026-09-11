from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models.modelos import Usuario, Tarea
from app.models.esquemas import UsuarioCrear, UsuarioRespuesta


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.post("/", response_model=UsuarioRespuesta, status_code=201)
def crear_usuario(
    usuario: UsuarioCrear,
    session: Session = Depends(get_session)
):
    usuario_existente = session.exec(
        select(Usuario).where(Usuario.correo == usuario.correo)
    ).first()

    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="El correo ya está registrado"
        )

    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo
    )

    session.add(nuevo_usuario)
    session.commit()
    session.refresh(nuevo_usuario)

    return nuevo_usuario


@router.get("/", response_model=list[UsuarioRespuesta])
def listar_usuarios(
    session: Session = Depends(get_session)
):
    usuarios = session.exec(select(Usuario)).all()
    return usuarios


@router.get("/{usuario_id}")
def obtener_usuario(
    usuario_id: int,
    session: Session = Depends(get_session)
):
    usuario = session.get(Usuario, usuario_id)

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="El usuario no existe"
        )

    tareas = session.exec(
        select(Tarea).where(Tarea.usuario_id == usuario_id)
    ).all()

    return {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "tareas": tareas
    }

