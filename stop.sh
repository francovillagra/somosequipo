#!/bin/bash

echo "🛑 Deteniendo el servidor SomosEquipo..."

# Busca y mata procesos que contengan uvicorn
pkill -f "uvicorn main:app" && echo "✅ Servidor detenido." || echo "⚠️ No se encontró un servidor corriendo."
