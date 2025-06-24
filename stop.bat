@echo off
echo 🛑 Deteniendo el servidor SomosEquipo...
REM Busca el proceso de python con uvicorn y lo mata
taskkill /F /IM python.exe /T
echo ✅ Servidor detenido.
pause
