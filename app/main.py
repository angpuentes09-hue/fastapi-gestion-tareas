from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routes import usuarios, tareas, actividades

# Importamos los modelos para que SQLModel conozca las tablas
from app.models.modelos import Usuario, Tarea, Actividad


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Gestión de Tareas API",
    description="API para gestión de tareas con usuarios y actividades - PostgreSQL",
    version="1.0.0",
    lifespan=lifespan
)

# Incluir routers
app.include_router(usuarios.router)
app.include_router(tareas.router)
app.include_router(actividades.router)


@app.get("/")
def root():
    return {
        "message": "API de Gestión de Tareas - PostgreSQL",
        "docs": "/docs"
    }
