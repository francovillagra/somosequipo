# 📌 SomosEquipo - API de gestión de tareas colaborativas

✅ ¿Qué es este proyecto?

SomosEquipo es una API RESTful construida con FastAPI en Python. Su objetivo es permitir la gestión de tareas en equipo de manera sencilla y colaborativa.

Ideal como base para apps de trabajo en equipo, planificación personal o para aprender arquitectura backend con FastAPI.

# ✅ Funcionalidades actuales

Hasta el momento, la API implementa los siguientes endpoints:

    GET /tareas
    Lista todas las tareas.

    POST /tareas
    Crea una nueva tarea.

    PUT /tareas/{tarea_id}/completar
    Marca una tarea como completada.

    DELETE /tareas/{tarea_id}
    Elimina una tarea por ID.

    PATCH /tareas/{tarea_id}
    Actualiza parcialmente los campos de una tarea (título, descripción).

# ✅ Cómo usar este proyecto

📥 1️⃣ Clonar el repositorio

git clone https://github.com/francovillagra/somosequipo.git
cd somosequipo

# 🐍 2️⃣ Instalación de dependencias

Si usas el Python portable incluido en el repo (recomendado para este proyecto):
./python-portable/bin/python.exe -m pip install -r requirements.txt

📌 Nota: No requiere instalación global de Python si usas la versión portable.

# 🚀 3️⃣ Levantar el servidor

- En Windows (Git Bash recomendado): ./run.sh
- En Windows CMD: run.bat

# 🛑 4️⃣ Detener el servidor

- En Git Bash: ./stop.sh
- En CMD: stop.bat

# 🌐 5️⃣ Probar la API

Abre en tu navegador:
http://127.0.0.1:8000/docs

Incluye documentación interactiva generada automáticamente (Swagger UI) para probar todos los endpoints sin escribir código.

# ✅ Plan a futuro (Roadmap)

🟢 Próximas funcionalidades planeadas:

- Filtro por estado: listar solo tareas completadas o pendientes.

- Asignar usuarios/responsables a tareas.

- Agregar autenticación básica con tokens.

- Persistencia en base de datos (SQLite / PostgreSQL).

- Tests automatizados.

- Documentación más extensa (OpenAPI/Redoc personalizada).

# ✅ Recomendaciones para colaborar

Si quieres contribuir o simplemente mantener tu copia bien organizada:

- Usa ramas para cada funcionalidad nueva.

- Escribe mensajes de commit claros y descriptivos.

- Actualiza el DEV_NOTES.md con cada avance.

- Haz pull antes de push para evitar conflictos.

# 📜 Licencia

Este proyecto es de uso libre para fines educativos y personales. Sentite libre de adaptarlo o mejorarlo.

# 💻 Autor

**Franco Villagra**, Desarrollador Fullstack.
Creando soluciones con tecnología.
