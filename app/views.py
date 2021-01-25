from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render
from django.views import View

from app.models import Estudiante, Matricula, Modalidad, Horario, Sede


class MatriculaView(View):
    def get(self, request):

        context = {}

        context["sedes"] = Sede.objects.all()
        context["anyos_estudio"] = Estudiante.ANYO_ESTUDIO_CHOICES
        context["horarios"] = Horario.objects.all().order_by("hora_inicio", "hora_fin", "sede_id")
        context["modalidad"] = Modalidad.objects.all()

        return render(request, template_name="index.html", context=context)

    def post(self, request):

        data = request.POST

        try:
            estudiante = Estudiante.objects.create(
                primer_nombre=data.get("primer_nombre"),
                segundo_nombre=data.get("segundo_nombre"),
                primer_apellido=data.get("primer_apellido"),
                segundo_apellido=data.get("segundo_apellido"),
                fecha_nacimiento=data.get("birthdate"),
                email=data.get("email_usuario"),
                telefono=data.get("telefono_usuario"),
                nombre_colegio=data.get("nombre_colegio"),
                nombre_padre=data.get("nombre_tutor"),
                telefono_padre=data.get("telefono_tutor"),
                anyo_estudio=data.get("anyo_estudio"),
                foto_carnet=request.FILES.get("foto_carnet"),
                copia_identidad=request.FILES.get("cedula_partida"),
                certificado=request.FILES.get("certificado"),
            )
        except (IntegrityError, ValidationError, ValueError) as e:
            return render(request, template_name="index.html", context=data)
        else:
            try:
                matricula = Matricula.objects.create(
                    estudiante=estudiante,
                    horario_id=int(data.get("p_horarios")),
                )
            except IntegrityError:
                return render(request, template_name="index.html", context=data)

        return render(request, template_name="success.html")
