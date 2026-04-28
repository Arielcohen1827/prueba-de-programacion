@echo off
cd /d %~dp0

echo Carpeta actual:
cd

echo Activando entorno...
call venv\Scripts\activate

echo Instalando requerimientos...
pip install -r requirements.txt

echo Ejecutando app...
python app.py

pause