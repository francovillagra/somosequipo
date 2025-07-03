# 🗒️ DEV_NOTES - Avances y notas de desarrollo

# 📌 Descripción general

Bitácora de trabajo y cambios realizados en el proyecto **SomosEquipo**, una API RESTful con FastAPI para la gestión de tareas colaborativas.

## 🎯 Estado actual (26-Jun-2025)

✅ API funcional y corriendo con FastAPI.

✅ Estructura básica de endpoints CRUD implementados.

✅ Python portable incluido para facilitar ejecución sin instalación global.

✅ Scripts de arranque/parada para Windows (bash y cmd).

✅ Documentación interactiva (Swagger UI) accesible en `/docs`.

✅ Funcionalidades implementadas:

- `GET /tareas`
  Devuelve la lista completa de tareas en memoria.
  Respuesta en formato JSON.
  Permite filtro por parámetro `completadas=true/false`.

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

- `GET /tareas/{id}`
  Obtiene los detalles de una tarea específica por su ID.

# ⚙️ Configuración y arranque del proyecto

📦 Dependencias
Incluidas en `requirements.txt`.
Instalación recomendada con Python portable incluido:

./python-portable/bin/python.exe -m pip install -r requirements.txt

# 📚 Abrir documentación interactiva

Visitar en navegador:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- Permite probar endpoints sin necesidad de herramientas externas.
- Generada automáticamente por FastAPI (Swagger UI).
- Incluye validación en tiempo real.

# ✅ Roadmap (Próximos pasos)

- Asignar usuarios/responsables a tareas
- Validación de campos más robusta (longitud, formato)
- Autenticación básica (token o HTTP Basic)
- Persistencia en base de datos (SQLite o PostgreSQL)
- Endpoint para obtener tarea por ID con formato detallado
- Tests unitarios y de integración
- Modularización en routers/servicios
- Despliegue inicial (Heroku / Azure)

# ✅ Notas personales

- Proyecto pensado para ser auto-contenido y portable.
- Evita requerir permisos de administrador.
- Ideal como base para cursos o prácticas de desarrollo backend.
- Pensado para crecimiento incremental y didáctico.

# ✍️ Histórico de cambios

- 2025-06-26

  - Se implementa DELETE /tareas/{id}.
  - Se implementa PATCH /tareas/{id} para actualizaciones parciales.
  - Scripts run.sh y stop.sh para Git Bash añadidos.
  - Ajustes en .gitignore para ignorar venv y pycache.

- 2025-06-20
  - Estructura base del proyecto con FastAPI.
  - Endpoints GET, POST y PUT completados.
  - Inclusión de Python portable para evitar instalaciones.

---

# 🆕 Cambios y avances (21-Jun-2025)

✅ Limpieza del repositorio:

- Eliminación de versiones viejas y actualización de `.gitignore`.

✅ Montaje y verificación de Python Portable:

- Versión embebida en carpeta `/python-portable`, binarios funcionando.
- Uso recomendado para evitar instalaciones globales.

✅ Scripts multiplataforma:

- `run.bat` / `stop.bat` (Windows CMD).
- `run.sh` / `stop.sh` (Git Bash, Linux, macOS).

✅ Ajustes en documentación:

- Inclusión de uso de scripts.
- Formato de README actualizado.
- Link para el banner del repositorio en GitHub.

✅ Traducción de errores de validación:

- Captura global con FastAPI exception_handler.
- Mensajes claros en español para errores de tipo, campos obligatorios y valores nulos.

✅ Filtros en GET /tareas:

- Query param `completadas=true/false` para respuestas dinámicas.

✅ Persistencia en archivo JSON:

- `storage.py` con funciones de guardar/cargar.
- Manejo de errores por JSON corrupto o vacío.
- Autocuración del archivo en caso de error.

✅ Endpoint PATCH:

- Actualización parcial de campos: título, descripción, responsable.

✅ Endpoint GET by ID:

- `/tareas/{id}` para obtener detalles de una tarea específica.

✅ Validación avanzada en modelos:

- Restricciones de longitud con Pydantic.
- Validación de completada con responsable obligatorio.
- Mensajes de error claros en la documentación Swagger.

✅ Confirmación de push y commits profesionales:

- Uso de convenciones `feat`, `fix`, etc.
- Mensajes descriptivos en español.
- Sincronización de ramas.

✅ Plan futuro documentado en Roadmap:

- Modularización en routers/servicios.
- Persistencia en DB real (SQLite/PostgreSQL).
- Autenticación y usuarios.
- Tests automáticos.
- Despliegue en plataformas cloud.

---

# 🆕 Cambios y avances (01-Jul-2025)

✅ Modularización avanzada:

- Routers independientes: `tareas`, `status`, `dependencies`.
- Limpieza de `main.py` para solo montar routers.
- Mejor organización para mantenimiento y escalabilidad.

✅ Autenticación básica:

- Middleware con dependencia global en router de tareas.
- Usuario/contraseña hardcodeados para pruebas iniciales.
- Protege todos los endpoints de tareas.

✅ Validación de datos en español:

- Handler global para `RequestValidationError`.
- Mensajes de error claros y localizados en Swagger UI.

✅ Persistencia robusta en JSON:

- Soporte para campo `creada_en` con timezone Buenos Aires.
- Conversión a ISO8601 para serialización correcta.
- Manejo de errores por archivo corrupto o vacío con autocuración.

✅ Endpoint PATCH mejorado:

- Modelo `TareaParcial` para actualización parcial.
- Consistencia con almacenamiento en memoria y en disco.
- Validación de campos opcionales.

✅ Scripts multiplataforma actualizados:

- `run.sh`, `stop.sh`, `run.bat`, `stop.bat` para arranque/parada fácil.
- Soporte para Windows CMD y Bash/Linux.

✅ Limpieza de repositorio:

- Eliminación de binarios .pyc y **pycache**.
- Inclusión de .gitignore definitivo.
- Commit profesional con convención `chore`.

✅ Confirmación de merge:

- Rama `refactor/modularizacion-routers` mergeada en `master`.
- Proyecto consolidado con estructura portable y modular.

---

# 🆕 Cambios y avances (03-Jul-2025)

✅ Modularización avanzada:

- Routers independientes: `tareas`, `status`, `dependencies`.
- Limpieza de `main.py` para solo montar routers.
- Mejor organización para mantenimiento y escalabilidad.

✅ Autenticación básica:

- Middleware con dependencia global en router de tareas.
- Usuario/contraseña hardcodeados para pruebas iniciales.
- Protege todos los endpoints de tareas.

✅ Validación de datos en español:

- Handler global para `RequestValidationError`.
- Mensajes de error claros y localizados en Swagger UI.

✅ Persistencia robusta en JSON:

- Soporte para campo `creada_en` con timezone Buenos Aires.
- Conversión a ISO8601 para serialización correcta.
- Manejo de errores por archivo corrupto o vacío con autocuración.

✅ Endpoint PATCH mejorado:

- Modelo `TareaParcial` para actualización parcial.
- Consistencia con almacenamiento en memoria y en disco.
- Validación de campos opcionales.

✅ Scripts multiplataforma actualizados:

- `run.sh`, `stop.sh`, `run.bat`, `stop.bat` para arranque/parada fácil.
- Soporte para Windows CMD y Bash/Linux.

✅ Limpieza de repositorio:

- Eliminación de binarios .pyc y **pycache**.
- Inclusión de .gitignore definitivo.
- Commit profesional con convención `chore`.

✅ Confirmación de merge:

- Rama `refactor/modularizacion-routers` mergeada en `master`.
- Proyecto consolidado con estructura portable y modular.

---

**Franco Villagra**

Desarrollador Fullstack - Creando soluciones con tecnología.
