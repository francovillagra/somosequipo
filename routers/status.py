from fastapi import APIRouter

status_router = APIRouter()

@status_router.get("/status")
def health_check():
    return {
        "status": "ok",
        "message": "API SomosEquipo funcionando correctamente"
    }
