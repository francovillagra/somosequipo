from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido mi primer proyecto SomosEquipo!"}