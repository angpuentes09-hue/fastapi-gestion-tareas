from fastapi import FastAPI

app = FastAPI(
    title="Gestión de Tareas",
    description="API para gestionar usuarios, tareas y actividades",
    version="1.0.0"
)


@app.get("/")
def inicio():
    return {
        "mensaje": "API de Gestión de Tareas funcionando correctamente"
    }