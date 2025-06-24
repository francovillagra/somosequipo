#!/bin/bash

echo "🚀 Levantando la API SomosEquipo..."
# Ejecuta el servidor usando el Python portable
./python-portable/bin/python.exe -m uvicorn main:app --reload
