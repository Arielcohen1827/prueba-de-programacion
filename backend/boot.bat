@echo off
cd /d %~dp0

echo Carpeta actual:
cd

echo Activando entorno...
call venv\Scripts\activate

echo Ejecutando app...
python app.py

pause