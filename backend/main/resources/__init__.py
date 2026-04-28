from .paciente import Paciente as pacienteResource
from .paciente import Pacientes as pacientesResource
from .profesional import Profesional as profesionalResource
from .profesional import Profesionales as profesionalesResource
from .ficha import Ficha as fichaResource
from .ficha import Fichas as fichasResource
from .planes import Plan as planResource
from .planes import Planes as planesResource
from .notificaciones import NotificacionesPaciente as notificaciones_pacienteResource
from .notificaciones import Notificaciones as notificacionesResource
from .notificaciones import Notificacion as notificacionResource
from .login import login as loginResource
from .logout import Logout as logoutResource
from .register import Register as registerResource

# New Resources
from .turno import Turno as turnoResource
from .turno import Turnos as turnosResource
from .evaluacion import Evaluacion as evaluacionResource
from .evaluacion import Evaluaciones as evaluacionesResource
from .ejercicio import Ejercicio as ejercicioResource
from .ejercicio import Ejercicios as ejerciciosResource
from .planes_ejercicio import PlanEjercicio as planEjercicioResource
from .planes_ejercicio import PlanesEjercicios as planesEjerciciosResource
from .especialidad import Especialidad as especialidadResource
from .especialidad import Especialidades as especialidadesResource
