from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request, status

from routers import tareas

app = FastAPI(title="SomosEquipo API")

# Incluimos el router de tareas
app.include_router(tareas.router)

# Handler de errores de validación traducidos
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores_traducidos = []
    for error in exc.errors():
        campo = " ➜ ".join(str(loc) for loc in error["loc"])
        mensaje = error["msg"]
        if "value is not a valid integer" in mensaje.lower():
            mensaje = "El valor debe ser un número entero."
        elif "field required" in mensaje.lower():
            mensaje = "Este campo es obligatorio."
        elif "none is not an allowed value" in mensaje.lower():
            mensaje = "No se permite un valor nulo."
        errores_traducidos.append({"campo": campo, "mensaje": mensaje})

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detalle": errores_traducidos},
    )
