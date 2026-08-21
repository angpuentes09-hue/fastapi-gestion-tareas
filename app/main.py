from fastapi import FastAPI
from app.routes import usuarios, tareas, actividades

app = FastAPI(
    title="Gestión de Tareas API",
    description="API para gestión de tareas con usuarios y actividades - Versión Memoria",
    version="1.0.0"
)

# Incluir routers
app.include_router(usuarios.router)
app.include_router(tareas.router)
app.include_router(actividades.router)

@app.get("/")
def root():
    return {"message": "API de Gestión de Tareas - Versión Memoria", "docs": "/docs"}
