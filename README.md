# Grupo-M — TP2 Programación 1

API REST desarrollada con **Flask** y **Flask-RESTful** para la gestión de una aplicación de kinesiología, con persistencia de datos usando **SQLAlchemy** y **SQLite**.

## Recursos disponibles

| Recurso | Ruta colección | Ruta individual | Métodos |
|---------|---------------|-----------------|---------|
| Pacientes | `/pacientes` | `/paciente/<id>` | GET, POST, PUT, DELETE |
| Profesionales | `/profesionales` | `/profesional/<id>` | GET, POST, PUT, DELETE |
| Especialidades | `/especialidades` | `/especialidad/<id>` | GET, POST, PUT, DELETE |
| Fichas | `/fichas` | `/ficha/<id>` | GET, POST, PUT, DELETE |
| Turnos | `/turnos` | `/turno/<id>` | GET, POST, PUT, DELETE |
| Planes | `/planes` | `/plan/<id>` | GET, POST, PUT, DELETE |
| Planes-Ejercicios | `/planes_ejercicios` | `/plan_ejercicio/<id>` | GET, POST, PUT, DELETE |
| Ejercicios | `/ejercicios` | `/ejercicio/<id>` | GET, POST, PUT, DELETE |
| Evaluaciones | `/evaluaciones` | `/evaluacion/<id>` | GET, POST, PUT, DELETE |
| Notificaciones | `/notificaciones` | `/notificacion/<id>` | GET, POST, PUT, DELETE |
| Notificaciones por Paciente | `/paciente/<id>/notificaciones` | — | GET |
| Login | `/login` | — | POST |
| Logout | `/logout` | — | POST |
| Register | `/register` | — | POST |

## Cómo ejecutar en Windows

### Instalación
```bash
cd backend
install.bat
```

### Iniciar servidor
```bash
cd backend
boot.bat
```

## Cómo ejecutar en Linux

### Instalación
```bash
cd backend
bash install.sh
```

### Iniciar servidor
```bash
cd backend
bash boot.sh
```

El servidor corre en `http://127.0.0.1:5000`

## Colección Postman

El archivo de la colección actualizado se encuentra en:

```
backend/collection/Postman-Actualizado/Grupo - M.postman_collection act.json
```

Contiene todos los endpoints con ejemplos de respuesta (200, 201, 400, 401, 404) para facilitar las pruebas.

