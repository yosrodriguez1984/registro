from django.contrib import admin

from app.models import Estudiante, Modalidad, Sede, Horario


@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = "id", "nombre", "siglas"


@admin.register(Modalidad)
class ModalidadAdmin(admin.ModelAdmin):
    list_display = "id", "nombre"


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "sede",
        "dias_clase",
        "hora_inicio",
        "hora_fin",
    )


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "primer_nombre",
        "segundo_nombre",
        "primer_apellido",
        "segundo_apellido",
        "email",
        "telefono",
    )
