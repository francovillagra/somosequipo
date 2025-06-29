# 🗒️ DEV_NOTES - Avances y notas de desarrollo

# 📌 Descripción general

Bitácora de trabajo y cambios realizados en el proyecto SomosEquipo, una API RESTful con FastAPI para la gestión de tareas colaborativas.

## 🎯 Estado actual (21-Jun-2025)

✅ API funcional y corriendo con FastAPI.

✅ Estructura básica de endpoints CRUD implementados.

✅ Python portable incluido para facilitar ejecución sin instalación global.

✅ Scripts de arranque/parada para Windows (bash y cmd).

✅ Documentación interactiva (Swagger UI) accesible en /docs.

✅ Funcionalidades implementadas

- `GET /tareas`
  Devuelve la lista completa de tareas en memoria.

                Respuesta en formato JSON.

                Sin filtros por ahora (planificado para la próxima etapa).

- `POST /tareas`
  Crea una nueva tarea con ID, título, descripción, estado de completada.

                Valida que el ID no esté duplicado.

- `PUT /tareas/{id}/completar`
  Marca la tarea como completada (cambio de estado booleano).

- `DELETE /tareas/{id}`
  Elimina una tarea por ID.

                Devuelve mensaje de confirmación o error 404 si no existe.

- `PATCH /tareas/{id}`
  Permite actualizar solo algunos campos (parcial) de la tarea.

                Valida existencia de la tarea.

# Configuración y arranque del proyecto

📦 Dependencias
Incluidas en requirements.txt.
Instalación recomendada con Python portable incluido:

./python-portable/bin/python.exe -m pip install -r requirements.txt

# 🚀 Scripts para ejecución

Git Bash / Linux:

    ./run.sh: Inicia el servidor con uvicorn en modo recarga.

    ./stop.sh: Busca y mata procesos uvicorn locales.

CMD Windows:

    run.bat: Inicia el servidor uvicorn.

    stop.bat: Detiene el proceso uvicorn por PID.

# Abrir documentación interactiva:

http://127.0.0.1:8000/docs

- Permite probar endpoints sin necesidad de herramientas externas.

- Generada automáticamente por FastAPI (Swagger UI).

# ✅ Roadmap (Próximos pasos)

    Filtrado en GET /tareas (query param completadas=true/false)

    Asignar usuarios/responsables a tareas

    Autenticación básica (token o HTTP Basic)

    Persistencia en base de datos (SQLite o PostgreSQL)

    Endpoint para obtener tarea por ID

    Tests unitarios y de integración

    Despliegue inicial (Heroku / Azure)

# ✅ Notas personales

    Proyecto pensado para ser auto-contenido y portable.

    Evita requerir permisos de administrador.

    Ideal para ser base de un curso o práctica de desarrollo backend.

# ✍️ Histórico de cambios

- 2025-06-21

  Se implementa DELETE /tareas/{id}.

  Se implementa PATCH /tareas/{id} para actualizaciones parciales.

  Scripts run.sh y stop.sh para Git Bash añadidos.

  Ajustes en .gitignore para ignorar venv y pycache.

- 2025-06-20

  Estructura base del proyecto con FastAPI.

  Endpoints GET, POST y PUT completados.

  Inclusión de Python portable para evitar instalaciones.

# 📌 Mantenimiento

**Franco Villagra**

    Desarrollador Fullstack - Creando soluciones con tecnología.
