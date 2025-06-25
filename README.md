# 🧑‍🤝‍👩 SomosEquipo

Aplicación de **gestión colaborativa de tareas** hecha con **Python** y **FastAPI**.

> Este proyecto es parte de mi aprendizaje en desarrollo fullstack, para practicar la construcción de APIs y entornos portables.

---

✅ DOCUMENTACION:

## 🚀 Cómo levantar el servidor

## Como detenerlo

## Como usar los Scripts en Windows y Git Bash

### 🐧 **En Git Bash** (priorizado)

1.  Abre la terminal en la raíz del proyecto (`somosequipo/`)
2.  Ejecuta:

               ./run.sh

Accede a:

    La API en: http://127.0.0.1:8000

    La documentación automática en: http://127.0.0.1:8000/docs

🛑 Para detener el servidor:

                ./stop.sh

🪟 En CMD o PowerShell (Windows):

            1) los archivos *.bat* no son comandos nativos de bash.
            2) En Windows, los .bat son scripts que se ejecutan en CMD o con doble clic en la carpeta.

- Para correr el run.bat, hay varias formas:

            a) Doble click en la carpeta.
            b) Usando CMD (simbolo del sistema + R) o PowerShell, y ejecutar 'run.bat'.
            c) Hacerlo desde Gitbash:

* Si no tengo run.sh o stop.sh:
  Desde Git Bash para llamar a cmd.ex para ejecutarlo:

---> cmd.exe/c run.bat

---

## ⚡ Scripts útiles

En la raíz del proyecto encontrarás los siguientes scripts para facilitar el uso:

- `run.bat`: Inicia automáticamente el servidor FastAPI usando el Python portable.
- `stop.bat`: Detiene cualquier proceso `python.exe` en ejecución que corresponda al servidor.

### ▶️ Ejecutar el servidor

Simplemente haz doble clic en `run.bat` o desde la terminal:

run.bat

---

-- Sin RUN.BAT y STOP.BAT

1. Descargá o clona este repositorio.
2. Tené a mano el Python portable incluido en `python-portable/`: En Github: bjia56/portable-python
3. Desde la raíz del proyecto, ejecutá:

`````bash
./python-portable/bin/python.exe -m uvicorn main:app --reload


✅ Esto levanta el servidor automáticamente en:

    http://127.0.0.1:8000




Informacion util:

```🌐 Endpoints útiles

    Raíz: http://127.0.0.1:8000

    Documentación automática (Swagger): http://127.0.0.1:8000/docs

    Documentación alternativa (Redoc): http://127.0.0.1:8000/redoc




````somosequipo/
├── main.py             # punto de entrada, rutas de FastAPI
├── python-portable/    # Python portable + pip
├── README.md           # este documento
├── venv/               # (opcional) entorno virtual
└── ...                 # más archivos que sumes después

`````

Notas

    Usá Ctrl+C en la terminal para detener el servidor.

    Podés instalar más dependencias con:

./python-portable/bin/python.exe -m pip install <paquete>

Para más detalles, consultá la documentación en http://127.0.0.1:8000/docs cuando el servidor esté corriendo.
