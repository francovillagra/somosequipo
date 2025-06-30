from fastapi import FastAPI
from routers import tareas

app = FastAPI(
    title="SomosEquipo API",
    description="API RESTful para gestionar tareas colaborativas.",
    version="1.0.0"
)

# Incluir el router de tareas
app.include_router(tareas.router)
