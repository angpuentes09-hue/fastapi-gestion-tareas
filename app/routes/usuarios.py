from fastapi import APIRouter, HTTPException, status
from app.models.schemas import UsuarioCreate, UsuarioResponse
from typing import List

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Base de datos en memoria
usuarios_db = []
usuario_id_counter = 1

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: UsuarioCreate):
    # Validar correo único
    for u in usuarios_db:
        if u["correo"] == usuario.correo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo ya está registrado"
            )
    
    nuevo_usuario = {
        "id": usuario_id_counter,
        "nombre": usuario.nombre,
        "correo": usuario.correo
    }
    usuarios_db.append(nuevo_usuario)
    usuario_id_counter += 1
    return nuevo_usuario

@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios():
    return usuarios_db
