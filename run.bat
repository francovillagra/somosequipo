@echo off
echo 🚀 Levantando la API SomosEquipo...
python-portable\bin\python.exe -m uvicorn main:app --reload
pause
